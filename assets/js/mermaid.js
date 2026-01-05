---
---
document.addEventListener("DOMContentLoaded", function () {
  // اگر دوست داری تم روشن/تیره‌ی سایتت به Mermaid وصل بشه، می‌تونی این رو دستی تغییر بدی
  // الان "default" گذاشتم که هم روشن هم تیره اوکی باشه.
  var mjsTheme = "default";

  mermaid.initialize({
    startOnLoad: false,
    theme: mjsTheme
  });

  mermaid.init({
    theme: mjsTheme
  }, '.language-mermaid');
});