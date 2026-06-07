// Nav burger toggle
const nav = document.querySelector(".nav");
const burger = document.querySelector(".nav__burger");

burger?.addEventListener("click", () => {
  nav.classList.toggle("open");
});

// Close nav on link click (mobile)
document.querySelectorAll(".nav__links a").forEach((link) => {
  link.addEventListener("click", () => nav.classList.remove("open"));
});

// Active nav link on scroll
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav__links a");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        navLinks.forEach((link) => {
          link.classList.remove("active");
          if (link.getAttribute("href") === "#" + entry.target.id) {
            link.classList.add("active");
          }
        });
      }
    });
  },
  { rootMargin: "-40% 0px -55% 0px" },
);

sections.forEach((s) => observer.observe(s));

// Scroll-reveal for cards
const revealEls = document.querySelectorAll(
  ".proj-card, .exp-card, .stat-card, .skill-group",
);
const revealObs = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
        revealObs.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 },
);

revealEls.forEach((el) => {
  el.style.opacity = "0";
  el.style.transform = "translateY(24px)";
  el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
  revealObs.observe(el);
});
