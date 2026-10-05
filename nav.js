// Menú principal: desplegables y menú móvil.
(function () {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;
  const toggle = navbar.querySelector('.nav-toggle');
  const dropdowns = navbar.querySelectorAll('.nav-dropdown');

  function closeDropdowns(except) {
    dropdowns.forEach(d => {
      if (d === except) return;
      d.classList.remove('open');
      d.querySelector('.nav-dropdown-toggle').setAttribute('aria-expanded', 'false');
    });
  }

  dropdowns.forEach(d => {
    const button = d.querySelector('.nav-dropdown-toggle');
    button.addEventListener('click', e => {
      e.stopPropagation();
      const open = !d.classList.contains('open');
      closeDropdowns(d);
      d.classList.toggle('open', open);
      button.setAttribute('aria-expanded', String(open));
    });
  });

  if (toggle) {
    toggle.addEventListener('click', e => {
      e.stopPropagation();
      const open = !navbar.classList.contains('menu-open');
      navbar.classList.toggle('menu-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    });
  }

  function closeAll() {
    closeDropdowns();
    navbar.classList.remove('menu-open');
    if (toggle) {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Abrir menú');
    }
  }

  document.addEventListener('click', e => {
    if (!navbar.contains(e.target)) closeAll();
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeAll();
  });
  // Cerrar el menú al ir a un ancla de la misma página.
  navbar.querySelectorAll('a[href^="#"], a[href^="/#"]').forEach(link => {
    link.addEventListener('click', closeAll);
  });
})();
