class LocationWizard extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    this.render();
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        /* استایل‌ها بدون تغییر باقی می‌مانند */
        :host { display: block; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 1000px; margin: 2rem auto; padding: 1rem; background: #f8fafc; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h2 { color: #334155; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }
        .input-section { display: flex; gap: 1rem; margin-bottom: 1rem; }
        .input-group { flex: 1; }
        label { display: block; margin-bottom: 0.5rem; font-weight: 600; color: #475569; }
        input, select { width: 100%; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
        button { background: #4f46e5; color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; font-weight: 600; margin-top: 1.5rem; }
        button:hover { background: #4338ca; }
        .results { margin-top: 2rem; }
        .result-section { margin-bottom: 2rem; background: white; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .result-title { font-weight: 600; color: #334155; margin-bottom: 0.5rem; }
        .image-gallery { display: flex; gap: 1rem; overflow-x: auto; padding: 1rem 0; }
        .image-card { min-width: 200px; border: 1px solid #e2e8f0; border-radius: 4px; overflow: hidden; }
        .image-card img { width: 100%; height: 120px; object-fit: cover; }
        .image-info { padding: 0.5rem; font-size: 0.8rem; }
        .tags-container { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem; }
        .tag { background: #e0e7ff; color: #4f46e5; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem; }
        .gps-point { background: #f0fdf4; border: 1px solid #bbf7d0; padding: 0.5rem; margin-bottom: 0.5rem; border-radius: 4px; font-size: 0.9rem; }
        .predicted-location { background: #eff6ff; border: 1px solid #bfdbfe; padding: 1rem; border-radius: 6px; margin-top: 1rem; font-weight: 600; color: #1e40af; }
      </style>
      
      <h2>Multi-Modal Location Wizard (Fingerprinting)</h2>
      
      <div class="input-section">
        <div class="input-group">
          <label for="image-input">Upload Image</label>
          <input type="file" id="image-input" accept="image/*">
        </div>
        
        <div class="input-group">
          <label for="text-input">Or Enter Text</label>
          <input type="text" id="text-input" placeholder="Enter keywords or description">
        </div>
        
        <div class="input-group">
          <label for="rssi-input">RSSI Value</label>
          <input type="text" id="rssi-input" placeholder="e.g. -85">
        </div>
      </div>
      
      <button id="locate-button">Find Location</button>
      
      <div class="results" id="results-container" hidden>
        <div class="result-section">
          <div class="result-title">Input Image</div>
          <div id="input-image-container"></div>
        </div>
        
        <div class="result-section">
          <div class="result-title">Similar Images Found (KNN k=3)</div>
          <div class="image-gallery" id="similar-images"></div>
        </div>
        
        <div class="result-section">
          <div class="result-title">Hot Keywords</div>
          <div class="tags-container" id="keywords-container"></div>
        </div>
        
        <div class="result-section">
          <div class="result-title">Neighbor GPS Points</div>
          <div class="gps-points" id="gps-points"></div>
        </div>
        
        <div class="result-section">
          <div class="result-title">Predicted Location</div>
          <div class="predicted-location" id="predicted-location"></div>
        </div>
      </div>
    `;

    this.shadowRoot.getElementById('locate-button').addEventListener('click', () => this.processLocation());
  }

  async processLocation() {
    const resultsContainer = this.shadowRoot.getElementById('results-container');
    resultsContainer.hidden = false;

    // نمایش تصویر ورودی
    const inputImage = this.shadowRoot.getElementById('image-input').files[0];
    if (inputImage) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.shadowRoot.getElementById('input-image-container').innerHTML = `
          <div class="image-card">
            <img src="${e.target.result}">
            <div class="image-info">Uploaded Image</div>
          </div>
        `;
      };
      reader.readAsDataURL(inputImage);
    }

    // ساخت FormData برای ارسال به بک‌اند
    const formData = new FormData();
    if (inputImage) {
      formData.append('image', inputImage);
    }
    formData.append('text', this.shadowRoot.getElementById('text-input').value);
    formData.append('rssi', this.shadowRoot.getElementById('rssi-input').value);

    try {
      // ارسال درخواست به بک‌اند
      const response = await fetch('http://127.0.0.1:5000/locate', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      this.displayResults(data);

    } catch (error) {
      console.error("Error contacting backend:", error);
      resultsContainer.innerHTML = `<p style="color: red;">Failed to connect to the backend. Is it running at http://127.0.0.1:5000 ?</p>`;
    }
  }

  displayResults(data) {
    // نمایش تصاویر مشابه
    const similarImagesContainer = this.shadowRoot.getElementById('similar-images');
    similarImagesContainer.innerHTML = '';
    data.similar_images.forEach(neighbor => {
      // مسیر تصویر را برای نمایش در مرورگر اصلاح می‌کنیم
      const imageUrl = `http://127.0.0.1:5000${neighbor.url.split('/').pop()}`;
      similarImagesContainer.innerHTML += `
        <div class="image-card">
          <img src="${imageUrl}" onerror="this.src='placeholder.png'">
          <div class="image-info">
            <div>Distance: ${neighbor.distance.toFixed(2)}</div>
            <div>GPS: ${neighbor.gps.lat.toFixed(6)}, ${neighbor.gps.lon.toFixed(6)}</div>
          </div>
        </div>
      `;
    });

    // نمایش کلمات کلیدی
    const keywordsContainer = this.shadowRoot.getElementById('keywords-container');
    keywordsContainer.innerHTML = '';
    data.keywords.forEach(kw => {
      keywordsContainer.innerHTML += `<span class="tag">${kw.tag} (${kw.count})</span>`;
    });

    // نمایش نقاط GPS همسایه‌ها
    const gpsPointsContainer = this.shadowRoot.getElementById('gps-points');
    gpsPointsContainer.innerHTML = '';
    data.similar_images.forEach((neighbor, i) => {
      gpsPointsContainer.innerHTML += `
        <div class="gps-point">
          Neighbor ${i + 1}: ${neighbor.gps.lat.toFixed(6)}, ${neighbor.gps.lon.toFixed(6)}
        </div>
      `;
    });

    // نمایش موقعیت پیش‌بینی شده
    if (data.predicted_location) {
      this.shadowRoot.getElementById('predicted-location').textContent =
        `Predicted Coordinates: ${data.predicted_location.lat.toFixed(6)}, ${data.predicted_location.lon.toFixed(6)}`;
    }
  }
}

customElements.define('location-wizard', LocationWizard);
