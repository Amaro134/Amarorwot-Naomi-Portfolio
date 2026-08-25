function switchTab(tabName) {
  document
    .querySelectorAll(".proj-tab")
    .forEach((t) => t.classList.remove("active"));
  document
    .querySelectorAll(".proj-panel")
    .forEach((p) => p.classList.add("hidden"));
  const tab = document.querySelector(`.proj-tab[data-tab="${tabName}"]`);
  if (tab) tab.classList.add("active");
  const panel = document.getElementById("tab-" + tabName);
  if (panel) panel.classList.remove("hidden");
}

// ---- NAV burger ----
const burger = document.querySelector(".nav__burger");
const nav = document.querySelector(".nav");
if (burger) {
  burger.addEventListener("click", () => nav.classList.toggle("open"));
}

// ---- Smooth close mobile menu on link click ----
document.querySelectorAll(".nav__links a").forEach((link) => {
  link.addEventListener("click", () => nav.classList.remove("open"));
});

// ---- Count-up animation for stat cards ----
function parseValue(str) {
  // Strips non-numeric chars, returns { number, suffix }
  const match = str.match(/([\d.]+)(.*)/);
  if (!match) return { number: 0, suffix: str };
  return { number: parseFloat(match[1]), suffix: match[2].trim() };
}

function animateCount(el, duration = 1800) {
  const original = el.textContent.trim();
  const { number, suffix } = parseValue(original);
  const isInt = Number.isInteger(number);
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = eased * number;
    el.textContent =
      (isInt ? Math.floor(current) : current.toFixed(1)) + suffix;
    if (progress < 1) requestAnimationFrame(update);
    else el.textContent = original; // snap to exact final value
  }

  requestAnimationFrame(update);
}

// Project tab toggle
const tabs = document.querySelectorAll(".proj-tab");
const panels = document.querySelectorAll(".proj-panel");

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.remove("active"));
    panels.forEach((p) => p.classList.add("hidden"));
    tab.classList.add("active");
    document
      .getElementById("tab-" + tab.dataset.tab)
      .classList.remove("hidden");
  });
});

// Trigger count-up when stats scroll into view
const statValues = document.querySelectorAll(".stat-card__value");

const countObs = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateCount(entry.target);
        countObs.unobserve(entry.target); // only animate once
      }
    });
  },
  { threshold: 0.5 },
);

statValues.forEach((el) => countObs.observe(el));
