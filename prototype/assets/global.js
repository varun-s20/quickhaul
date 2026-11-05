/* =====================================================================
   Quick Haul: global script (hero prototype, phase B, 2026-11-03)
   Loads deferred on every page, after assets/global.css. No libraries.
   Every block checks for its element first, so one file serves every page.
   ===================================================================== */
(function () {
  'use strict';

  /* ---- config, flags, helpers ---- */
  var PHONE_HREF = 'tel:+16035550142';      /* placeholder number, content/placeholders.md */
  var PHONE_TEXT = '(603) 555-0142';
  /* Placeholder service towns (content/placeholders.md). Lower case, state dropped, for matching. */
  var TOWNS = ['andover', 'dracut', 'haverhill', 'lawrence', 'lowell', 'methuen',
    'derry', 'hudson', 'londonderry', 'nashua', 'pelham', 'salem'];
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ===== Ready flag: start the load sequence once the display face is in =====
     Waiting for fonts stops the headline rows rising in the fallback face and then jumping.
     700ms failsafe so a slow font never holds the page hidden. */
  (function () {
    var done = false;
    function ready() { if (done) return; done = true; root.classList.add('is-ready'); }
    if (reduceMotion) { ready(); return; }
    if (document.fonts && document.fonts.load) {
      Promise.all([
        document.fonts.load('800 1em "Bio Sans"'),
        document.fonts.load('300 1em "Bio Sans"')
      ]).then(function () { requestAnimationFrame(ready); }, ready);
    } else { ready(); }
    setTimeout(ready, 700);
  })();

  /* ===== Menu: a dialog on phones and tablets =====
     The page goes inert behind it, focus moves to the close button and stays in the panel,
     Escape closes, and focus returns to the Menu button. */
  (function () {
    var menu = $('[data-menu]');
    var opener = $('[data-menu-open]');
    if (!menu || !opener) return;
    var closer = $('[data-menu-close]', menu);
    var panel = $('.m-menu__panel', menu);
    var behind = $$('body > *').filter(function (el) { return el !== menu && el.tagName !== 'SCRIPT'; });
    var closeTimer;

    function focusables() {
      return $$('a[href], button:not([disabled])', panel);
    }
    function open() {
      clearTimeout(closeTimer);
      menu.hidden = false;
      behind.forEach(function (el) { el.inert = true; });
      document.body.style.overflow = 'hidden';
      opener.setAttribute('aria-expanded', 'true');
      menu.getBoundingClientRect();          /* commit the start state so the open transition runs */
      menu.classList.add('is-open');
      closer.focus();
    }
    function close() {
      menu.classList.remove('is-open');
      behind.forEach(function (el) { el.inert = false; });
      document.body.style.overflow = '';
      opener.setAttribute('aria-expanded', 'false');
      opener.focus();
      closeTimer = setTimeout(function () { menu.hidden = true; }, reduceMotion ? 0 : 500);
    }
    opener.addEventListener('click', open);
    closer.addEventListener('click', close);
    menu.addEventListener('click', function (e) { if (e.target === menu) close(); });
    menu.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key !== 'Tab') return;
      var items = focusables();
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    /* If the window grows past the menu breakpoint while it is open, close it */
    window.matchMedia('(min-width: 1025px)').addEventListener('change', function (mq) {
      if (mq.matches && !menu.hidden) close();
    });
  })();

  /* ===== Ticket: the work order in the hero =====
     Load chips set the "from" price and fill the truck bed; the town field says whether we come out;
     the day chips show the next three days (Sunday skipped). The form itself submits to book.html,
     so no page URL is built in script. */
  (function () {
    var form = $('[data-ticket]');
    if (!form) return;
    var truck = $('[data-truck]');
    var price = $('[data-ticket-price]', form);
    var unit = $('[data-ticket-unit]', form);
    var town = $('[data-ticket-town]', form);
    var note = $('[data-ticket-note]', form);
    var defaultNote = note ? note.textContent : '';

    function setLoad(value) {
      if (truck) truck.style.setProperty('--load', value);
    }

    /* load chips */
    $$('input[name="load"]', form).forEach(function (input) {
      input.addEventListener('change', function () {
        if (!input.checked) return;
        price.textContent = '$' + input.getAttribute('data-price');
        unit.textContent = input.getAttribute('data-unit');
        setLoad(input.getAttribute('data-load'));
      });
    });

    /* first fill: the bed rises to the chip that starts checked (1/8 in the markup), so the price,
       the chip and the drawing always agree (critic r1) */
    function checkedLoad() {
      var c = $('input[name="load"]:checked', form);
      return c ? c.getAttribute('data-load') : '.125';
    }
    if (truck) {
      if (reduceMotion) { setLoad(checkedLoad()); }
      else { setTimeout(function () { setLoad(checkedLoad()); }, 900); }
    }

    /* town suggestions: a listbox we style, in place of the browser's datalist popup (critic r1).
       Combobox pattern: arrows move the active option, Enter or a click picks it, Escape closes. */
    var list = $('[data-ticket-options]', form);
    var options = list ? $$('[role="option"]', list) : [];
    var active = -1;
    function shown() { return options.filter(function (o) { return !o.hidden; }); }
    function setActive(i) {
      var vis = shown();
      options.forEach(function (o) { o.setAttribute('aria-selected', 'false'); });
      active = vis.length ? (i + vis.length) % vis.length : -1;
      if (active < 0) { town.removeAttribute('aria-activedescendant'); return; }
      vis[active].setAttribute('aria-selected', 'true');
      town.setAttribute('aria-activedescendant', vis[active].id);
      vis[active].scrollIntoView({ block: 'nearest' });
    }
    function openList(open) {
      if (!list) return;
      list.hidden = !open;
      town.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (!open) setActive(-1);
    }
    function filterList() {
      var q = town.value.trim().toLowerCase();
      var count = 0;
      options.forEach(function (o) {
        var hit = !q || o.textContent.toLowerCase().indexOf(q) === 0;
        o.hidden = !hit;
        if (hit) count++;
      });
      active = -1;
      openList(count > 0 && q.length > 0);
    }
    function pick(o) {
      town.value = o.textContent;
      openList(false);
      checkTown(true);
    }
    if (list && town) {
      town.addEventListener('input', filterList);
      town.addEventListener('keydown', function (e) {
        var open = !list.hidden;
        if (e.key === 'ArrowDown') { e.preventDefault(); if (!open) filterList(); if (!list.hidden) setActive(active + 1); }
        else if (e.key === 'ArrowUp' && open) { e.preventDefault(); setActive(active - 1); }
        else if (e.key === 'Enter' && open && active > -1) { e.preventDefault(); pick(shown()[active]); }
        else if (e.key === 'Escape' && open) { e.preventDefault(); openList(false); }
      });
      town.addEventListener('blur', function () { setTimeout(function () { openList(false); }, 120); });
      options.forEach(function (o) {
        o.addEventListener('mousedown', function (e) { e.preventDefault(); });   /* keep focus in the field */
        o.addEventListener('click', function () { pick(o); });
      });
    }

    /* town check */
    function checkTown(final) {
      if (!town || !note) return;
      var raw = town.value.trim();
      var name = raw.toLowerCase().replace(/,.*$/, '').replace(/\s+(ma|nh)$/, '').trim();
      if (!name) { note.textContent = defaultNote; return; }
      var hit = TOWNS.filter(function (t) { return t === name; })[0];
      if (hit) {
        note.textContent = 'Yes, we come to ' + raw.replace(/,.*$/, '') + '.';
      } else if (final || (name.length >= 3 && !TOWNS.some(function (t) { return t.indexOf(name) === 0; }))) {
        /* no listed town starts with what was typed: say so with the number, never fall back to the "we cover" line (critic r2) */
        note.textContent = '';
        /* short enough to stay inside the note's two reserved lines at 1100, so the strip never grows (critic r2) */
        note.appendChild(document.createTextNode('Not on our list? '));
        var a = document.createElement('a');
        a.href = PHONE_HREF;
        a.textContent = 'Call ' + PHONE_TEXT;
        note.appendChild(a);
      } else {
        note.textContent = defaultNote;
      }
    }
    if (town) {
      town.addEventListener('input', function () { checkTown(false); });
      town.addEventListener('change', function () { checkTown(true); });
    }

    /* next three days, Sunday skipped. Real availability comes from the booking calendar later. */
    var days = $$('[data-ticket-days] .a-choice', form);
    if (days.length) {
      var names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      var d = new Date();
      var i = 0;
      while (i < days.length) {
        d.setDate(d.getDate() + 1);
        if (d.getDay() === 0) continue;
        var chip = days[i];
        var mm = ('0' + (d.getMonth() + 1)).slice(-2), dd = ('0' + d.getDate()).slice(-2);
        $('.a-choice__input', chip).value = d.getFullYear() + '-' + mm + '-' + dd;
        $('.a-choice__dow', chip).textContent = names[d.getDay()];
        $('.a-choice__num', chip).textContent = d.getDate();
        $('.sr-only', chip).textContent = ' ' + months[d.getMonth()];
        i++;
      }
    }
  })();

  /* ===== Action bar (phones): show Book and Call once the ticket's own buttons have gone under the header =====
     Position is read on every scroll frame, not from an edge-crossing observer, so a jump back to the top
     (Back to top, a reduced-motion jump) hides the bar again (critic r1). The header keeps its own Book now:
     the brief asks for it to stay visible in the sticky header. */
  (function () {
    var bar = $('[data-action-bar]');
    var anchor = $('[data-ticket-action]');
    var header = $('.m-header');
    if (!bar) return;
    if (!anchor) { bar.classList.add('is-shown'); return; }
    var queued = false;
    function update() {
      queued = false;
      var line = header ? header.getBoundingClientRect().bottom : 0;
      var show = anchor.getBoundingClientRect().bottom < line;
      bar.classList.toggle('is-shown', show);
    }
    function queue() { if (!queued) { queued = true; requestAnimationFrame(update); } }
    window.addEventListener('scroll', queue, { passive: true });
    window.addEventListener('resize', queue);
    window.addEventListener('pageshow', queue);
    update();
  })();
})();
