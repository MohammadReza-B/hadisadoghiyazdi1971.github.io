// static/script.js
let jobs = [];
let crews = [];
let currentPlan = null;

// DOM references
const jobsTableBody = () => document.querySelector("#jobsTable tbody");
const crewsTableBody = () => document.querySelector("#crewsTable tbody");
const planContent = document.getElementById("planContent");
const planStatus = document.getElementById("planStatus");

// پارامترهای کاری
const WORKING_PARAMS = {
  startHour: 8.0,
  endHour: 14.0,
  maxWorkingHours: 6,
  travelTimeBetweenJobs: 1.0,
  breakTime: 0.5
};


// مرکز نقشه روی مشهد
const mashhadCenter = [36.29872222222222, 59.60872222222223];
const map = L.map('map').setView(mashhadCenter, 14);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom: 18}).addTo(map);

let marker = null;
map.on('click', e => {
  const lat = e.latlng.lat.toFixed(6);
  const lon = e.latlng.lng.toFixed(6);
  document.getElementById("jobLat").value = lat;
  document.getElementById("jobLon").value = lon;
  if (marker) map.removeLayer(marker);
  marker = L.marker([lat, lon]).addTo(map);
});

// helpers
function renderJobs() {
  const assignedJobs = currentPlan ? getAllAssignedJobs() : [];
  
  const rows = jobs.map(j => {
    const isAssigned = assignedJobs.includes(j.id);
    const rowClass = isAssigned ? 'table-success' : '';
    
    return `
      <tr class="${rowClass}">
        <td>${j.id}</td>
        <td>${j.priority}</td>
        <td>${j.estimated_person_hours}</td>
        <td>${j.address || 'ندارد'}</td>
        <td>${j.lat ? j.lat.toFixed(4) : '---'}</td>
        <td>${j.lon ? j.lon.toFixed(4) : '---'}</td>
        <td>${(j.constraints||[]).join(", ") || 'هیچ'}</td>
        <td>
          ${isAssigned ? '<span class="badge bg-success">✓ تخصیص‌یافته</span>' : ''}
          <button class="btn btn-sm btn-outline-danger" onclick="deleteJob('${j.id}')">
            <i class="fa fa-trash"></i>
          </button>
        </td>
      </tr>
    `;
  }).join("");
  jobsTableBody().innerHTML = rows;
}

function getAllAssignedJobs() {
  if (!currentPlan || !currentPlan.plan) return [];
  
  const assignedJobs = [];
  for (const gid of Object.keys(currentPlan.plan)) {
    for (const day of Object.keys(currentPlan.plan[gid])) {
      currentPlan.plan[gid][day].forEach(assignment => {
        if (!assignedJobs.includes(assignment.job_id)) {
          assignedJobs.push(assignment.job_id);
        }
      });
    }
  }
  return assignedJobs;
}

function renderCrews() {
  const rows = crews.map(c => `
    <tr>
      <td>
        <input type="checkbox" class="crew-checkbox" value="${c.id}">
      </td>
      <td>${c.id}</td>
      <td>${c.label || '---'}</td>
      <td>${c.members_count}</td>
      <td>${c.daily_capacity_hours}</td>
      <td>${(c.skills||[]).join(", ") || 'هیچ'}</td>
      <td>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteCrew('${c.id}')">
          <i class="fa fa-trash"></i>
        </button>
      </td>
    </tr>
  `).join("");
  crewsTableBody().innerHTML = rows;
  updateDeleteButtonState();
}

// Add job
document.getElementById("jobForm").addEventListener("submit", e => {
  e.preventDefault();
  const consEls = document.querySelectorAll(".constraint-chk");
  const constraints = Array.from(consEls).filter(c=>c.checked).map(c=>c.value);
  const job = {
    id: document.getElementById("jobId").value.trim(),
    address: document.getElementById("jobAddress").value.trim(),
    lat: parseFloat(document.getElementById("jobLat").value) || null,
    lon: parseFloat(document.getElementById("jobLon").value) || null,
    priority: parseInt(document.getElementById("jobPriority").value),
    estimated_person_hours: parseFloat(document.getElementById("jobHours").value),
    constraints: constraints
  };
  if (constraints.includes("requires_crane")) job.requires = "crane";
  jobs.push(job);
  renderJobs();
  e.target.reset();
});

// Add crew
document.getElementById("crewForm").addEventListener("submit", e => {
  e.preventDefault();
  const crew = {
    id: document.getElementById("crewId").value.trim(),
    label: document.getElementById("crewLabel").value.trim(),
    members_count: parseInt(document.getElementById("crewMembers").value),
    daily_capacity_hours: parseFloat(document.getElementById("crewPerMemberCap").value),
    skills: document.getElementById("crewSkills").value.split(",").map(s=>s.trim()).filter(Boolean),
    base_lat: 36.317054,
    base_lon: 59.473879
  };
  crews.push(crew);
  renderCrews();
  e.target.reset();
});

// Generate plan
document.getElementById("generatePlan").addEventListener("click", async () => {
  planStatus.innerHTML = "<div class='text-muted'>در حال ارسال درخواست...</div>";
  planContent.innerHTML = "";
  try {
    const payload = {
      jobs: jobs,
      groups: crews.map(c => ({
        ...c,
        daily_capacity_hours: (c.members_count * c.daily_capacity_hours)
      })),
      working_params: WORKING_PARAMS
    };
    const res = await fetch("/api/plan", {method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify(payload)});
    if (!res.ok) {
      const txt = await res.text();
      planStatus.innerHTML = `<div class='text-danger'>خطا: ${res.status} ${txt}</div>`;
      return;
    }
    const data = await res.json();
    currentPlan = data;
    planStatus.innerHTML = "<div class='text-success'>برنامه تولید شد.</div>";
    document.getElementById("exportExcel").disabled = false;
    renderPlan(data);
  } catch (err) {
    planStatus.innerHTML = `<div class='text-danger'>خطا در ارتباط: ${err.message}</div>`;
    console.error(err);
  }
});

// Render plan with maps and details
function renderPlan(result) {
  if (!result || !result.plan) {
    planContent.innerHTML = "<div class='text-danger'>خروجی نامعتبر.</div>";
    return;
  }
  
  let html = "";
  
  // نمایش کارهای تخصیص یافته
  for (const gid of Object.keys(result.plan)) {
    const group = crews.find(c => c.id === gid) || {label: gid, members_count: 1};
    const groupState = result.group_state[gid];
    
    html += `<div class="card mb-3 assignment-card">`;
    html += `<div class="card-header bg-primary text-white">`;
    html += `<h6 class="mb-0">${group.label || gid} (${gid}) - ${group.members_count} نفر</h6>`;
    html += `</div>`;
    html += `<div class="card-body p-0">`;
    
    const days = result.plan[gid];
    let hasAssignment = false;
    
    for (const day of Object.keys(days)) {
      const assignments = days[day];
      if (assignments.length === 0) continue;
      
      hasAssignment = true;
      html += `<div class="p-3 border-bottom">`;
      html += `<h6 class="text-success">${day}</h6>`;
      
      // دکمه مشاهده نقشه
      html += `<div class="mb-2">`;
      html += `<button class="btn btn-sm btn-outline-primary" onclick="openMapView('${gid}', '${day}')">`;
      html += `<i class="fa fa-map-marker"></i> مشاهده نقشه مسیر`;
      html += `</button>`;
      html += `</div>`;
      
      html += `<table class="table table-sm mb-0"><thead class="table-light"><tr>
        <th>کار</th>
        <th>آدرس</th>
        <th>اولویت</th>
        <th>ساعت شروع</th>
        <th>مدت</th>
        <th>موقعیت</th>
        <th>نقشه</th>
      </tr></thead><tbody>`;
      
      for (const item of assignments) {
        const job = jobs.find(j => j.id === item.job_id) || {};
        const coords = job.lat && job.lon ? `${job.lat.toFixed(4)}, ${job.lon.toFixed(4)}` : '---';
        const mapLink = job.lat && job.lon ? 
          `<button class="btn btn-sm btn-outline-secondary" onclick="openLocationInMap(${job.lat}, ${job.lon}, '${job.id}')">
             <i class="fa fa-map-pin"></i>
           </button>` : '---';
        
        html += `
          <tr>
            <td>${item.job_id}</td>
            <td>${job.address || '---'}</td>
            <td><span class="badge bg-${getPriorityBadgeColor(job.priority)}">${job.priority || '---'}</span></td>
            <td>${formatHour(item.start)}</td>
            <td>${item.duration_elapsed || item.duration || 0} ساعت</td>
            <td>${coords}</td>
            <td>${mapLink}</td>
          </tr>
        `;
      }
      
      html += `</tbody></table>`;
      html += `<div class="mt-2 text-muted small">`;
      html += `مجموع نفر-ساعت: ${groupState[day].used_person_hours.toFixed(1)} | `;
      html += `ساعت پایان: ${formatHour(groupState[day].last_end_time)}`;
      html += `</div>`;
      html += `</div>`;
    }
    
    if (!hasAssignment) {
      html += `<div class="p-3 text-muted text-center">هیچ کاری به این گروه تخصیص نیافته است</div>`;
    }
    
    html += "</div></div>";
  }
  
  // نمایش کارهای تخصیص‌نشده
  if (result.unassigned && result.unassigned.length > 0) {
    html += `<div class="card border-warning unassigned-card">`;
    html += `<div class="card-header bg-warning text-dark">`;
    html += `<h6 class="mb-0">کارهای تخصیص‌نشده (${result.unassigned.length} مورد)</h6>`;
    html += `</div>`;
    html += `<div class="card-body">`;
    
    result.unassigned.forEach(jobId => {
      const job = jobs.find(j => j.id === jobId) || {};
      const priorityColor = getPriorityBadgeColor(job.priority);
      html += `<div class="mb-2 p-2 border rounded">`;
      html += `<strong>${jobId}</strong>`;
      html += ` <span class="badge bg-${priorityColor}">اولویت ${job.priority || '---'}</span>`;
      html += `<div class="text-muted small">آدرس: ${job.address || 'آدرس نامشخص'}</div>`;
      html += `<div class="text-muted small">ساعت‌نفر: ${job.estimated_person_hours || '---'}`;
      if (job.constraints && job.constraints.length > 0) {
        html += ` | قیود: ${job.constraints.join(', ')}`;
      }
      if (job.lat && job.lon) {
        html += ` | موقعیت: ${job.lat.toFixed(4)}, ${job.lon.toFixed(4)}`;
      }
      html += `</div>`;
      html += `</div>`;
    });
    
    html += `</div></div>`;
  }
  
  planContent.innerHTML = html;
}

function getPriorityBadgeColor(priority) {
  switch(priority) {
    case 1: return 'danger';
    case 2: return 'warning';
    case 3: return 'success';
    default: return 'secondary';
  }
}

// format numeric hour like 7.25 => 07:15
function formatHour(h) {
  if (h === null || h === undefined) return "---";
  const hh = Math.floor(h);
  const mm = Math.round((h - hh) * 60);
  return `${String(hh).padStart(2,"0")}:${String(mm).padStart(2,"0")}`;
}

// Delete job from database
async function deleteJob(jobId) {
  if (confirm(`آیا از حذف کار ${jobId} مطمئن هستید؟`)) {
    try {
      const res = await fetch(`/api/jobs/${jobId}`, { method: 'DELETE' });
      if (res.ok) {
        jobs = jobs.filter(j => j.id !== jobId);
        renderJobs();
        alert(`کار ${jobId} حذف شد`);
      } else {
        const error = await res.json();
        alert(`خطا در حذف کار: ${error.error}`);
      }
    } catch (err) {
      alert('خطا در ارتباط با سرور');
    }
  }
}

// Delete crew from database
async function deleteCrew(crewId) {
  if (confirm(`آیا از حذف گروه ${crewId} مطمئن هستید؟`)) {
    try {
      const res = await fetch(`/api/groups/${crewId}`, { method: 'DELETE' });
      if (res.ok) {
        crews = crews.filter(c => c.id !== crewId);
        renderCrews();
        alert(`گروه ${crewId} حذف شد`);
      } else {
        const error = await res.json();
        alert(`خطا در حذف گروه: ${error.error}`);
      }
    } catch (err) {
      alert('خطا در ارتباط با سرور');
    }
  }
}

// حذف گروه‌های انتخاب شده از دیتابیس
document.getElementById('deleteSelectedCrews').addEventListener('click', async () => {
  const selectedCrews = Array.from(document.querySelectorAll('.crew-checkbox:checked'))
    .map(cb => cb.value);
  
  if (selectedCrews.length > 0 && confirm(`آیا از حذف ${selectedCrews.length} گروه انتخاب شده مطمئن هستید؟`)) {
    try {
      let deletedCount = 0;
      for (const crewId of selectedCrews) {
        const res = await fetch(`/api/groups/${crewId}`, { method: 'DELETE' });
        if (res.ok) {
          deletedCount++;
        }
      }
      
      if (deletedCount > 0) {
        await loadInitialData();
        alert(`✅ ${deletedCount} گروه حذف شد`);
      }
    } catch (err) {
      alert('خطا در حذف گروه‌ها');
    }
  }
});

// ذخیره در دیتابیس
document.getElementById('saveJobsToDB').addEventListener('click', async () => {
  try {
    const res = await fetch("/api/jobs", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({jobs: jobs})
    });
    const result = await res.json();
    if (res.ok) {
      alert(result.message || `✅ ${jobs.length} کار در دیتابیس ذخیره شد`);
      await loadInitialData();
    } else {
      alert('خطا در ذخیره کارها: ' + (result.error || 'خطای ناشناخته'));
    }
  } catch (err) {
    alert('خطا در ارتباط با سرور');
  }
});

document.getElementById('saveCrewsToDB').addEventListener('click', async () => {
  try {
    const res = await fetch("/api/groups", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({groups: crews})
    });
    const result = await res.json();
    if (res.ok) {
      alert(result.message || `✅ ${crews.length} گروه در دیتابیس ذخیره شد`);
      await loadInitialData();
    } else {
      alert('خطا در ذخیره گروه‌ها: ' + (result.error || 'خطای ناشناخته'));
    }
  } catch (err) {
    alert('خطا در ارتباط با سرور');
  }
});

// مدیریت انتخاب گروه‌ها برای حذف
function updateDeleteButtonState() {
  const checkboxes = document.querySelectorAll('.crew-checkbox:checked');
  const deleteBtn = document.getElementById('deleteSelectedCrews');
  deleteBtn.disabled = checkboxes.length === 0;
}

document.addEventListener('change', (e) => {
  if (e.target.classList.contains('crew-checkbox')) {
    updateDeleteButtonState();
  }
});

// Export to Excel

document.getElementById('exportExcel').addEventListener('click', async () => {
  const btn = document.getElementById('exportExcel');
  if (!currentPlan) {
    alert('ابتدا برنامه را تولید کنید');
    return;
  }
  btn.disabled = true;
  btn.innerText = 'در حال ساخت اکسل...';
  try {
    await exportToExcel(currentPlan);
    alert('✅ فایل اکسل با موفقیت تولید و دانلود شد.');
  } catch (err) {
    alert('خطا در تولید فایل اکسل: ' + (err.message || err));
  }
  btn.disabled = false;
  btn.innerText = 'دانلود اکسل برنامه';
});

async function fetchRouteDataForGroupDay(gid, day) {
  try {
    const res = await fetch(`/api/map-data?group=${encodeURIComponent(gid)}&day=${encodeURIComponent(day)}`);
    if (!res.ok) return null;
    const data = await res.json();
    return data;
  } catch (err) {
    return null;
  }
}

async function exportToExcel(plan) {
  const workbook = XLSX.utils.book_new();
  
  // ورق پارامترها
  const paramsData = [
    ['پارامترهای برنامه‌ریزی'],
    [],
    ['پارامتر', 'مقدار', 'توضیحات'],
    ['ساعت شروع کار', decimalToTime(WORKING_PARAMS.startHour), 'ساعت شروع کار روزانه'],
    ['ساعت پایان کار', decimalToTime(WORKING_PARAMS.endHour), 'ساعت پایان کار روزانه'],
    ['حداکثر ساعت کاری', WORKING_PARAMS.maxWorkingHours, 'حداکثر ساعت مجاز کار در روز'],
    ['زمان انتقال بین کارها', WORKING_PARAMS.travelTimeBetweenJobs, 'زمان جابجایی بین کارها (ساعت)'],
    ['زمان استراحت', WORKING_PARAMS.breakTime, 'زمان استراحت بین کارها (ساعت)'],
    [],
    ['گروه‌های کاری'],
    ['شناسه گروه', 'نام', 'تعداد نفرات', 'ظرفیت روزانه (ساعت)', 'مهارت‌ها'],
    ...crews.map(c => [c.id, c.label || '', c.members_count, c.daily_capacity_hours, (c.skills||[]).join(', ')])
  ];
  
  const paramsSheet = XLSX.utils.aoa_to_sheet(paramsData);
  XLSX.utils.book_append_sheet(workbook, paramsSheet, 'پارامترها');
  
  // ایجاد ورق برای هر گروه
  // prepare batch request: collect all group/day pairs
  const batchItems = [];
  for (const gid of Object.keys(plan.plan)) {
    for (const day of Object.keys(plan.plan[gid])) {
      if ((plan.plan[gid][day] || []).length > 0) batchItems.push({group: gid, day: day});
    }
  }

  // fetch batch route data in one call
  let batchMap = {}; // key: `${gid}|||${day}` -> response item
  if (batchItems.length > 0) {
    try {
      const res = await fetch('/api/map-data/batch', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({items: batchItems})
      });
      if (res.ok) {
        const json = await res.json();
        if (json && Array.isArray(json.items)) {
          json.items.forEach(it => {
            const key = `${it.group}|||${it.day}`;
            batchMap[key] = it;
          });
        }
      }
    } catch (err) {
      console.warn('Batch route fetch failed', err);
    }
  }

  for (const gid of Object.keys(plan.plan)) {
    const group = crews.find(c => c.id === gid) || {label: gid};
    const worksheet_data = [];
    
    worksheet_data.push(['برنامه هفتگی گروه: ' + (group.label || gid)]);
    worksheet_data.push([]);
    
    for (const day of Object.keys(plan.plan[gid])) {
      const assignments = plan.plan[gid][day];
      if (assignments.length === 0) continue;

      worksheet_data.push([`روز: ${day}`]);
      worksheet_data.push(['کار', 'آدرس', 'اولویت', 'ساعت شروع', 'مدت (ساعت)', 'نفر-ساعت', 'موقعیت جغرافیایی', 'مسافت طی شده (کیلومتر)']);

      // get route data from batchMap if available
      const batchKey = `${gid}|||${day}`;
      const routeData = batchMap[batchKey] || null;
      let jobRouteMap = {};
      let routeTotal = null;
      if (routeData && routeData.jobs && Array.isArray(routeData.jobs)) {
        // sort jobs to match assignments order
        const jobsSorted = assignments.map(a => routeData.jobs.find(j => j.id === a.job_id));
        jobsSorted.forEach(j => {
          if (j) jobRouteMap[j.id] = typeof j.route_distance_km !== 'undefined' ? j.route_distance_km : (typeof j.distance_km !== 'undefined' ? j.distance_km : null);
        });
        if (typeof routeData.route_total_km !== 'undefined') routeTotal = routeData.route_total_km;
      }

      // get ordered job ids for this day (to match OSRM legs)
      const orderedJobIds = assignments.map(a => a.job_id);
      let sumRoute = 0;
      // Add a virtual row for base -> first destination if possible
      if (routeData && routeData.jobs && Array.isArray(routeData.jobs) && routeData.jobs.length > 0 && typeof routeData.jobs[0].route_distance_km !== 'undefined') {
        const firstJob = routeData.jobs[0];
        worksheet_data.push([
          'پایگاه → اولین مقصد',
          firstJob.address || '',
          '',
          '',
          '',
          '',
          (firstJob.lat && firstJob.lon) ? {
            f: `=HYPERLINK("http://maps.google.com/maps?q=${firstJob.lat},${firstJob.lon}", "${firstJob.lat}, ${firstJob.lon}")`,
            v: `${firstJob.lat}, ${firstJob.lon}`,
            t: 's'
          } : '',
          firstJob.route_distance_km
        ]);
        if (typeof firstJob.route_distance_km === 'number') sumRoute += firstJob.route_distance_km;
      }
      for (let idx = 0; idx < assignments.length; idx++) {
        const item = assignments[idx];
        const job = jobs.find(j => j.id === item.job_id) || {};
        let coordsCell = '';
        if (job.lat && job.lon) {
          coordsCell = {
            f: `=HYPERLINK("http://maps.google.com/maps?q=${job.lat},${job.lon}", "${job.lat}, ${job.lon}")`,
            v: `${job.lat}, ${job.lon}`,
            t: 's'
          };
        }
        // For jobs, show only the segment from the previous job (not the base).
        // Rules:
        // - We add a virtual row for base -> first job above. Therefore the first job row must NOT repeat that distance.
        // - If there's only one job for the day, the virtual row contains the only OSRM leg and the job row distance should be empty/zero.
        // - For days with multiple jobs, job rows should show legs 1..N-1 (i.e., routeData.jobs[1] belongs to second job, etc.).
        let distanceKm = '';
        if (routeData && routeData.jobs && Array.isArray(routeData.jobs)) {
          // routeData.jobs contains legs attached to jobs where route_distance_km for index i is the leg that ends at job i
          if (routeData.jobs.length === 1) {
            // single-job day: virtual row shows base->first, so leave job row empty
            distanceKm = (idx === 0) ? '' : (routeData.jobs[idx] && typeof routeData.jobs[idx].route_distance_km !== 'undefined' ? routeData.jobs[idx].route_distance_km : '');
          } else {
            // multiple-job day: only jobs after the first should display a segment (job at idx>0)
            distanceKm = (idx > 0 && routeData.jobs[idx] && typeof routeData.jobs[idx].route_distance_km !== 'undefined') ? routeData.jobs[idx].route_distance_km : '';
          }
        } else if (jobRouteMap[item.job_id] !== undefined) {
          // fallback: if we have a mapping (older payloads) use it but still avoid duplicating the first leg
          distanceKm = (idx === 0 && routeData && routeData.jobs && routeData.jobs.length === 1) ? '' : jobRouteMap[item.job_id];
        } else if (typeof item.distance_km !== 'undefined') {
          distanceKm = item.distance_km;
        }
        if (typeof distanceKm === 'number') sumRoute += distanceKm;
        worksheet_data.push([
          item.job_id,
          job.address || '',
          job.priority || '',
          formatHour(item.start),
          item.duration_elapsed || item.duration || 0,
          item.person_hours || 0,
          coordsCell || '',
          distanceKm
        ]);
      }
      // add summary row: sum of legs and (if available) route_total_km from OSRM
      worksheet_data.push([]);
      worksheet_data.push(['', '', '', '', '', '', 'جمع مسافت بخش‌ها (km):', sumRoute]);
      if (routeTotal !== null) {
        worksheet_data.push(['', '', '', '', '', '', 'مجموع مسیر OSRM (km):', routeTotal]);
        if (Math.abs(sumRoute - routeTotal) > 0.01) {
          worksheet_data.push(['', '', '', '', '', '', '⚠️ اختلاف مجموع بخش‌ها و OSRM:', (sumRoute - routeTotal).toFixed(3)]);
        }
      }
      worksheet_data.push([]);
    }
    
    const worksheet = XLSX.utils.aoa_to_sheet(worksheet_data);
    XLSX.utils.book_append_sheet(workbook, worksheet, group.label || gid);
  }
  
  // ورق کارهای تخصیص‌نشده
  if (plan.unassigned && plan.unassigned.length > 0) {
    const unassigned_data = [['کارهای تخصیص‌نشده'], []];
    unassigned_data.push(['کار', 'آدرس', 'اولویت', 'ساعت-نفر', 'قیود', 'موقعیت']);
    
    plan.unassigned.forEach(jobId => {
      const job = jobs.find(j => j.id === jobId) || {};
      let coordsCell = '';
      if (job.lat && job.lon) {
        coordsCell = {
          f: `=HYPERLINK("http://maps.google.com/maps?q=${job.lat},${job.lon}", "${job.lat}, ${job.lon}")`,
          v: `${job.lat}, ${job.lon}`,
          t: 's'
        };
      }
      
      unassigned_data.push([
        jobId,
        job.address || '',
        job.priority || '',
        job.estimated_person_hours || '',
        (job.constraints || []).join(', '),
        coordsCell || ''
      ]);
    });
    
    const unassigned_ws = XLSX.utils.aoa_to_sheet(unassigned_data);
    XLSX.utils.book_append_sheet(workbook, unassigned_ws, 'تخصیص‌نشده‌ها');
  }
  
  const fileName = `program_haftegi_${new Date().toLocaleDateString('fa-IR')}.xlsx`;
  XLSX.writeFile(workbook, fileName);
}

// Show dataset (from server)
document.getElementById("showDatasetBtn").addEventListener("click", async () => {
  try {
    const res = await fetch("/api/dataset");
    const d = await res.json();
    const html = `<h6>Jobs (server)</h6><pre>${JSON.stringify(d.jobs||[], null, 2)}</pre><h6>Groups (server)</h6><pre>${JSON.stringify(d.groups||[], null, 2)}</pre>`;
    planContent.innerHTML = html;
  } catch (err) {
    planContent.innerHTML = `<div class='text-danger'>خطا در دریافت دیتاست: ${err.message}</div>`;
  }
});

// توابع مدیریت پارامترها
function loadWorkingParams() {
  const saved = localStorage.getItem('workingParams');
  if (saved) {
    Object.assign(WORKING_PARAMS, JSON.parse(saved));
  }
  updateParamsForm();
}

function saveWorkingParams() {
  const form = document.getElementById('paramsForm');
  WORKING_PARAMS.startHour = timeToDecimal(form.startTime.value);
  WORKING_PARAMS.endHour = timeToDecimal(form.endTime.value);
  WORKING_PARAMS.maxWorkingHours = parseFloat(form.maxHours.value);
  WORKING_PARAMS.travelTimeBetweenJobs = parseFloat(form.travelTime.value);
  WORKING_PARAMS.breakTime = parseFloat(form.breakTime.value);
  
  localStorage.setItem('workingParams', JSON.stringify(WORKING_PARAMS));
  
  const modal = bootstrap.Modal.getInstance(document.getElementById('paramsModal'));
  if (modal) modal.hide();
  
  // also save default base inputs if present
  const dbLat = document.getElementById('defaultBaseLat');
  const dbLon = document.getElementById('defaultBaseLon');
  if (dbLat && dbLon) {
    localStorage.setItem('defaultBaseLat', dbLat.value);
    localStorage.setItem('defaultBaseLon', dbLon.value);
  }

  alert('پارامترها ذخیره شدند');
}

function updateParamsForm() {
  const form = document.getElementById('paramsForm');
  if (form) {
    form.startTime.value = decimalToTime(WORKING_PARAMS.startHour);
    form.endTime.value = decimalToTime(WORKING_PARAMS.endHour);
    form.maxHours.value = WORKING_PARAMS.maxWorkingHours;
    form.travelTime.value = WORKING_PARAMS.travelTimeBetweenJobs;
    form.breakTime.value = WORKING_PARAMS.breakTime;
  }
}

// load/save default base coordinates
function saveDefaultBase() {
  const lat = document.getElementById('defaultBaseLat').value;
  const lon = document.getElementById('defaultBaseLon').value;
  localStorage.setItem('defaultBaseLat', lat);
  localStorage.setItem('defaultBaseLon', lon);
  alert('پارامترها ذخیره شدند');
}

function loadDefaultBase() {
  const lat = localStorage.getItem('defaultBaseLat');
  const lon = localStorage.getItem('defaultBaseLon');
  if (lat && lon) {
    const elat = document.getElementById('defaultBaseLat');
    const elon = document.getElementById('defaultBaseLon');
    if (elat) elat.value = lat;
    if (elon) elon.value = lon;
  }
}

function timeToDecimal(timeStr) {
  const [hours, minutes] = timeStr.split(':').map(Number);
  return hours + (minutes / 60);
}

function decimalToTime(decimal) {
  const hours = Math.floor(decimal);
  const minutes = Math.round((decimal - hours) * 60);
  return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}`;
}


// توابع نقشه - اینها را در script.js اضافه یا جایگزین کنید
function openMapView(groupId, day) {
    const url = `/map-view?group=${encodeURIComponent(groupId)}&day=${encodeURIComponent(day)}`;
    window.open(url, '_blank', 'width=1200,height=800');
}

function openLocationInMap(lat, lon, jobId) {
    const url = `/map-view?lat=${lat}&lon=${lon}&job=${encodeURIComponent(jobId)}`;
    window.open(url, '_blank', 'width=1200,height=800');
}

// بارگذاری اولیه داده‌ها از دیتابیس
async function loadInitialData() {
  try {
    const jobsRes = await fetch("/api/jobs");
    const jobsData = await jobsRes.json();
    jobs = jobsData.jobs || [];
    
    const groupsRes = await fetch("/api/groups");
    const groupsData = await groupsRes.json();
    crews = groupsData.groups || [];
    
    renderJobs();
    renderCrews();
    loadWorkingParams();
  } catch (err) {
    console.error("Error loading initial data:", err);
  }
}

// initial render
loadInitialData();
loadDefaultBase();