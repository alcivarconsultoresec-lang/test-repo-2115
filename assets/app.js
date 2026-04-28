const $ = (q, ctx = document) => ctx.querySelector(q);
const $$ = (q, ctx = document) => Array.from(ctx.querySelectorAll(q));

// Safety first: content must never depend on scroll animation to be visible.
// This avoids blank text on mobile browsers if IntersectionObserver delays or fails.
$$('.reveal').forEach(el => el.classList.add('is-visible'));

const year = $('#year');
if (year) year.textContent = new Date().getFullYear();

const progressBar = $('#progressBar');
const updateProgress = () => {
  if (!progressBar) return;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  const pct = total > 0 ? (window.scrollY / total) * 100 : 0;
  progressBar.style.width = `${pct}%`;
};
window.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();

const menuToggle = $('#menuToggle');
const mobileDrawer = $('#mobileDrawer');
if (menuToggle && mobileDrawer) {
  menuToggle.addEventListener('click', () => {
    const open = mobileDrawer.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(open));
  });
  $$('#mobileDrawer a').forEach(link => link.addEventListener('click', () => {
    mobileDrawer.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
  }));
}

// Progressive reveal remains decorative only; all content is already visible.
if ('IntersectionObserver' in window) {
  const revealItems = $$('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  revealItems.forEach(item => revealObserver.observe(item));
}

const counters = $$('[data-counter]');
if ('IntersectionObserver' in window) {
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = Number(el.dataset.counter || 0);
      const duration = 1150;
      const start = performance.now();
      const tick = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target);
        if (progress < 1) requestAnimationFrame(tick);
        else el.textContent = target;
      };
      requestAnimationFrame(tick);
      counterObserver.unobserve(el);
    });
  }, { threshold: 0.3 });
  counters.forEach(counter => counterObserver.observe(counter));
} else {
  counters.forEach(el => { el.textContent = el.dataset.counter || '0'; });
}

$$('.spotlight-card').forEach(card => {
  card.addEventListener('pointermove', (event) => {
    const rect = card.getBoundingClientRect();
    card.style.setProperty('--mx', `${event.clientX - rect.left}px`);
    card.style.setProperty('--my', `${event.clientY - rect.top}px`);
  });
});

const tabs = $$('.compare-tab');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const view = tab.dataset.view;
    tabs.forEach(t => t.classList.toggle('active', t === tab));
    $$('.compare-panel').forEach(panel => panel.classList.toggle('active', panel.dataset.panel === view));
  });
});

const canvas = $('#flowCanvas');
if (canvas) {
  canvas.style.zIndex = '0';
  canvas.style.pointerEvents = 'none';
  const ctx = canvas.getContext('2d');
  let particles = [];
  const density = window.matchMedia('(max-width: 720px)').matches ? 26 : 58;

  const resize = () => {
    const rect = canvas.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.floor(rect.width * dpr);
    canvas.height = Math.floor(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    particles = Array.from({ length: density }, () => ({
      x: Math.random() * rect.width,
      y: Math.random() * rect.height,
      vx: (Math.random() - 0.5) * 0.28,
      vy: (Math.random() - 0.5) * 0.28,
      r: Math.random() * 1.6 + 0.5
    }));
  };

  const draw = () => {
    const rect = canvas.getBoundingClientRect();
    ctx.clearRect(0, 0, rect.width, rect.height);
    particles.forEach((p, i) => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < -10 || p.x > rect.width + 10) p.vx *= -1;
      if (p.y < -10 || p.y > rect.height + 10) p.vy *= -1;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(125,227,255,0.5)';
      ctx.fill();
      for (let j = i + 1; j < particles.length; j++) {
        const q = particles[j];
        const dx = p.x - q.x;
        const dy = p.y - q.y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < 105) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = `rgba(125,227,255,${0.1 * (1 - d / 105)})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }
    });
    requestAnimationFrame(draw);
  };

  resize();
  window.addEventListener('resize', resize);
  draw();
}

$$('[data-wa]').forEach(el => {
  el.addEventListener('click', () => {
    const text = encodeURIComponent(el.getAttribute('data-wa'));
    window.open(`https://wa.me/593979716053?text=${text}`, '_blank');
  });
});