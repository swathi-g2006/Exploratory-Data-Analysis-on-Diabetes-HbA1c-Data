// Scroll-triggered fade-in animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.feature-card, .hero-content, p')
  .forEach(el => {
    el.classList.add('fade-in');
    observer.observe(el);
  });

// Animate KPI counters
function animateCounter(el, target, suffix = '') {
  let current = 0;
  // Ensure we format string parsing if target has a letter, but simpler logic here using target number
  const step  = Math.ceil(target / 60);
  const timer = setInterval(() => {
    current = Math.min(current + step, target);
    el.textContent = current.toLocaleString() + suffix;
    if (current >= target) clearInterval(timer);
  }, 20);
}

window.addEventListener('load', () => {
  const kpiCard = document.getElementById('kpi-card');
  if (kpiCard) {
    const vals = kpiCard.querySelectorAll('.kpi-val');
    animateCounter(vals[0], 100, 'K+'); // Using 100K+ visual logic
  }
});
