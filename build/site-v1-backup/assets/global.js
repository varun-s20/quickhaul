/* =====================================================================
   Quick Haul: global script (site build, 2026-11-04)
   Loads deferred on every page, after assets/global.css. Nothing loads after it. No libraries.
   Every block checks for its element first, so one file serves every page.
   Built from the approved hero prototype (prototype/assets/global.js), extended for the homepage.
   ===================================================================== */
(function () {
  'use strict';

  /* ---- config, flags, helpers ---- */
  var PHONE_HREF = 'tel:+16035550142';      /* placeholder number, content/placeholders.md */
  var PHONE_TEXT = '(603) 555-0142';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function raf(fn) { var queued = false; return function () { if (queued) return; queued = true; requestAnimationFrame(function () { queued = false; fn(); }); }; }

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

  /* ===== Current page: mark the matching nav link from the URL, so the chrome is identical on every page ===== */
  (function () {
    var here = location.pathname.split('/').pop() || 'index.html';
    $$('.m-header__link, .m-menu__link').forEach(function (a) {
      var target = (a.getAttribute('href') || '').split('#')[0];
      if (target === here && a.getAttribute('href').indexOf('#') === -1) a.setAttribute('aria-current', 'page');
    });
  })();

  /* ===== In-view: fade and rise once, as each block reaches the screen =====
     Elements marked .a-inview get .is-inview once, then are no longer watched. Children of a [data-stagger]
     group start 90ms apart (spec 5). Without IntersectionObserver everything simply shows. */
  (function () {
    var items = $$('.a-inview');
    if (!items.length) return;
    $$('[data-stagger]').forEach(function (group) {
      $$('.a-inview', group).forEach(function (el, i) { el.style.transitionDelay = Math.min(i, 6) * 90 + 'ms'; });
    });
    if (reduceMotion || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-inview'); });
      return;
    }
    /* once risen, the reveal classes and delay come off, so the element's own hover and press transitions
       (card washes, tile press) are not overridden or delayed by the reveal */
    function settle(e) {
      if (e.target !== this || e.propertyName !== 'opacity') return;
      this.classList.remove('a-inview', 'is-inview');
      this.style.transitionDelay = '';
      this.removeEventListener('transitionend', settle);
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.addEventListener('transitionend', settle);
        entry.target.classList.add('is-inview');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    /* cards inside a horizontal rail rise with their row: the ones parked off to the right never cross the
       viewport while the page scrolls, so they are revealed when the track arrives, not one by one */
    var tracks = [];
    items.forEach(function (el) {
      var track = el.parentElement && el.parentElement.hasAttribute('data-rail-track') ? el.parentElement : null;
      if (!track) { io.observe(el); return; }
      if (tracks.indexOf(track) === -1) tracks.push(track);
    });
    var rowIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        $$('.a-inview', entry.target).forEach(function (el) {
          el.addEventListener('transitionend', settle);
          el.classList.add('is-inview');
        });
        rowIo.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    tracks.forEach(function (t) { rowIo.observe(t); });
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

    function focusables() { return $$('a[href], button:not([disabled])', panel); }
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

  /* ===== Ticket: the work order under the hero =====
     Load chips set the "from" price and fill the truck bed; the town field says whether we come out;
     the day chips show the next three days (Sunday skipped). The form submits to book.html (GET), so no
     page URL is built in script. Inline errors on submit, tied to the fields (no browser bubbles). */
  (function () {
    var form = $('[data-ticket]');
    if (!form) return;
    var truck = $('[data-truck]');
    var price = $('[data-ticket-price]', form);
    var unit = $('[data-ticket-unit]', form);
    var town = $('[data-ticket-town]', form);
    var note = $('[data-ticket-note]', form);
    var dayNote = $('[data-ticket-day-note]', form);
    var dayCell = $('[data-ticket-day-cell]', form);
    /* a town page's note starts filled in ("Yes, we come to Lowell, MA."); data-default holds what it clears back to */
    var defaultNote = note ? (note.getAttribute('data-default') || note.textContent) : '';

    function setLoad(value) { if (truck) truck.style.setProperty('--load', value); }

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

    /* towns come from the listbox options (generated from data/towns.json), so the list lives in one place */
    var list = $('[data-ticket-options]', form);
    var options = list ? $$('[role="option"]', list) : [];
    function key(s) { return s.toLowerCase().replace(/,.*$/, '').replace(/\s+(ma|nh)$/, '').trim(); }
    var towns = options.map(function (o) { return { key: key(o.textContent), label: o.textContent }; });

    /* town suggestions: a listbox we style, in place of the browser's datalist popup (critic r1).
       Combobox pattern: arrows move the active option, Enter or a click picks it, Escape closes. */
    var active = -1;
    function shown() { return options.filter(function (o) { return !o.hidden; }); }
    function setActive(i) {
      var vis = shown();
      options.forEach(function (o) { o.setAttribute('aria-selected', 'false'); });
      active = (vis.length && i >= 0) ? i % vis.length : -1;   /* -1 clears; ArrowUp wraps by passing the last index */
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
        else if (e.key === 'ArrowUp' && open) { e.preventDefault(); setActive(active <= 0 ? shown().length - 1 : active - 1); }
        else if (e.key === 'Enter' && open && active > -1) { e.preventDefault(); pick(shown()[active]); }
        else if (e.key === 'Escape' && open) { e.preventDefault(); openList(false); }
      });
      town.addEventListener('blur', function () { setTimeout(function () { openList(false); }, 120); });
      options.forEach(function (o) {
        o.addEventListener('mousedown', function (e) { e.preventDefault(); });   /* keep focus in the field */
        o.addEventListener('click', function () { pick(o); });
      });
    }

    /* town check. Copy (content/copy.md): before typing "Start typing to check we come to you";
       on the list "Yes, we come to Lowell, MA."; not on the list "Not on our list yet. Call (603) 555-0142 and ask" */
    function setNote(text, isError) {
      note.textContent = text;
      note.classList.toggle('is-error', !!isError);
    }
    function checkTown(final) {
      if (!town || !note) return;
      town.removeAttribute('aria-invalid');
      var name = key(town.value.trim());
      if (!name) { setNote(defaultNote); return; }
      var hit = towns.filter(function (t) { return t.key === name; })[0];
      if (hit) {
        setNote('Yes, we come to ' + hit.label + '.');
      } else if (final || (name.length >= 3 && !towns.some(function (t) { return t.key.indexOf(name) === 0; }))) {
        /* no listed town starts with what was typed: say so with the number, never fall back to a coverage line */
        setNote('Not on our list yet. ');
        var a = document.createElement('a');
        a.href = PHONE_HREF;
        a.textContent = 'Call ' + PHONE_TEXT;
        note.appendChild(a);
        note.appendChild(document.createTextNode(' and ask'));
      } else {
        setNote(defaultNote);
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
    } else if (dayNote) {
      dayNote.textContent = dayNote.getAttribute('data-empty');   /* "No open days showing. Call us and we'll find one." */
    }
    $$('input[name="day"]', form).forEach(function (input) {
      input.addEventListener('change', function () {
        if (dayCell) dayCell.classList.remove('is-invalid');
        if (dayNote) { dayNote.textContent = ''; dayNote.classList.remove('is-error'); }
      });
    });

    /* submit: town and day are needed. Errors show in the reserved line under each control and take focus. */
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) {
      var firstBad = null;
      if (town && !town.value.trim()) {
        setNote(note.getAttribute('data-error'), true);
        town.setAttribute('aria-invalid', 'true');
        firstBad = town;
      }
      if (!$('input[name="day"]:checked', form) && days.length) {
        dayNote.textContent = dayNote.getAttribute('data-error');
        dayNote.classList.add('is-error');
        dayCell.classList.add('is-invalid');
        firstBad = firstBad || $('input[name="day"]', form);
      }
      if (firstBad) { e.preventDefault(); firstBad.focus(); }
    });
  })();

  /* ===== Action bar (phones): show the call bar once the ticket's own buttons have gone under the header =====
     Position is read on every scroll frame, not from an edge-crossing observer, so a jump back to the top
     (Back to top, a reduced-motion jump) hides the bar again (critic r1). Call-only (Varun, 2b decision 4). */
  (function () {
    var bar = $('[data-action-bar]');
    /* pages with no ticket use the banner, so the bar still never shows on the first screen (spec 4) */
    var anchor = $('[data-ticket-action]') || $('.m-banner');
    var header = $('.m-header');
    if (!bar) return;
    if (!anchor) { bar.classList.add('is-shown'); return; }
    /* a form's own button wins over the bar: the bar steps aside while that button sits in the bar's band (critic, Book r2: 8px of Send was under it) */
    var clear = $$('[data-bar-clear]');
    function blocked() {
      var top = window.innerHeight - bar.offsetHeight;
      return clear.some(function (b) {
        var r = b.getBoundingClientRect();
        return r.height > 0 && r.bottom > top && r.top < window.innerHeight;
      });
    }
    var update = raf(function () {
      var line = header ? header.getBoundingClientRect().bottom : 0;
      bar.classList.toggle('is-shown', anchor.getBoundingClientRect().bottom < line && !blocked());
    });
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    window.addEventListener('pageshow', update);
    /* errors and step changes move the button with no scroll event */
    if (clear.length) { document.addEventListener('click', update); document.addEventListener('input', update); }
    update();
  })();

  /* ===== Rails: horizontal rows of cards (towns, reviews) with square arrows and a progress hairline =====
     Native scrolling with snap; the arrows move one card at a time and disable at the ends. A rail whose
     cards all fit gets .is-static and loses its controls. */
  $$('[data-rail]').forEach(function (rail) {
    var track = $('[data-rail-track]', rail);
    var thumb = $('[data-rail-thumb]', rail);
    var prev = $('[data-rail-prev]', rail);
    var next = $('[data-rail-next]', rail);
    if (!track) return;
    function step() {
      var card = track.firstElementChild;
      return card ? card.getBoundingClientRect().width : track.clientWidth;
    }
    var update = raf(function () {
      var max = track.scrollWidth - track.clientWidth;
      rail.classList.toggle('is-static', max < 2);
      if (max < 2) return;
      var ratio = track.clientWidth / track.scrollWidth;
      var at = track.scrollLeft / max;
      if (thumb) {
        thumb.style.width = (ratio * 100) + '%';
        thumb.style.transform = 'translateX(' + (at * (1 / ratio - 1) * 100) + '%)';
      }
      if (prev) prev.disabled = track.scrollLeft < 2;
      if (next) next.disabled = track.scrollLeft > max - 2;
    });
    function go(dir) {
      track.scrollBy({ left: dir * step(), behavior: reduceMotion ? 'auto' : 'smooth' });
    }
    if (prev) prev.addEventListener('click', function () { go(-1); });
    if (next) next.addEventListener('click', function () { go(1); });
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  /* ===== Before and after: a native range input drives the clip of the after photo =====
     The input covers the frame, so drag, tap and arrow keys all work with no custom pointer code. */
  $$('[data-compare]').forEach(function (frame) {
    var range = $('[data-compare-range]', frame);
    if (!range) return;
    var tagBefore = $('.m-compare__tag.-before', frame);
    var tagAfter = $('.m-compare__tag.-after', frame);
    function set() {
      frame.style.setProperty('--pos', range.value + '%');
      range.setAttribute('aria-valuetext', range.value + '% after');
      /* a tag fades once the divider reaches it, so neither label ever sits on the other side's photo */
      var x = frame.clientWidth * range.value / 100;
      if (tagBefore) tagBefore.classList.toggle('is-covered', x < tagBefore.offsetLeft + tagBefore.offsetWidth);
      if (tagAfter) tagAfter.classList.toggle('is-covered', x > tagAfter.offsetLeft);
    }
    range.addEventListener('input', set);
    window.addEventListener('resize', set);
    set();
  });

  /* ===== Forms: shared validation and sending =====
     Inline errors tied by aria-describedby and aria-invalid (conventions). An error's wording lives on its field in
     data-error, so the copy stays in the HTML. A form only reports success when the endpoint answered OK; with no
     endpoint it fails, and the failure state offers the phone (conventions: no fake success). */
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  function fieldError(input) {
    var v = input.value.trim();
    if (input.hasAttribute('data-either')) {
      var other = document.getElementById(input.getAttribute('data-either'));
      return (v || (other && other.value.trim())) ? '' : input.getAttribute('data-error');
    }
    if (input.hasAttribute('data-required') && !v) return input.getAttribute('data-error');
    if (input.hasAttribute('data-email') && v && !EMAIL_RE.test(v)) return input.getAttribute('data-error');
    if (input.hasAttribute('data-phone') && v && v.replace(/\D/g, '').length < 10) return input.getAttribute('data-error');   /* the phone is how Shawn confirms the booking (critic, Book r1) */
    return '';
  }
  function showFieldError(input, message) {
    var note = document.getElementById(input.getAttribute('aria-describedby'));
    if (message) { input.setAttribute('aria-invalid', 'true'); } else { input.removeAttribute('aria-invalid'); }
    if (note) { note.textContent = message; note.hidden = !message; }
    /* an either-or rule marks both fields, because filling in either one fixes it (critic, Contact r1) */
    var other = input.hasAttribute('data-either') ? document.getElementById(input.getAttribute('data-either')) : null;
    if (other) other.classList.toggle('is-also', !!message);
  }
  /* checks every marked field inside root, shows each error, focuses the first; true when clean */
  function validate(root) {
    var first = null;
    $$('[data-required], [data-email], [data-either]', root).forEach(function (input) {
      var message = fieldError(input);
      showFieldError(input, message);
      if (message && !first) first = input;
    });
    if (first) first.focus();
    return !first;
  }
  /* an error clears as soon as the visitor has fixed it, never while they are still typing a first attempt */
  function watchFields(root) {
    $$('[data-required], [data-email], [data-either]', root).forEach(function (input) {
      function recheck() {
        if (input.getAttribute('aria-invalid') === 'true' && !fieldError(input)) showFieldError(input, '');
      }
      input.addEventListener('input', recheck);
      var other = input.hasAttribute('data-either') ? document.getElementById(input.getAttribute('data-either')) : null;
      if (other) other.addEventListener('input', recheck);   /* an either-or error is fixed by filling in the other field too */
    });
  }
  function sendForm(form, done, failed) {
    var url = window.SITE_FORM_ENDPOINT;
    if (!url || !window.fetch) { failed(); return; }
    fetch(url, { method: 'POST', body: new FormData(form) }).then(function (r) {
      if (r.ok) { done(); } else { failed(); }
    }, failed);
  }
  /* photo fields exist only with a backend: no file input without one (conventions) */
  function setupUploads(root) {
    if (!window.SITE_FORM_ENDPOINT) return;
    $$('[data-needs-endpoint]', root).forEach(function (el) { el.hidden = false; });
    $$('[data-upload]', root).forEach(function (input) {
      var note = $('[data-upload-note]', input.closest('.m-field'));
      var helper = note ? note.textContent : '';
      var list = $('[data-upload-files]', input.closest('.m-field'));
      input.addEventListener('change', function () {
        var bad = Array.prototype.some.call(input.files, function (f) { return !/^image\/(jpeg|png)$/.test(f.type); });
        if (bad) input.value = '';   /* a refused file never travels with the form */
        /* the visitor's own file names, so they can see what is attached (critic, Book r2). Choosing again replaces the set */
        if (list) {
          while (list.firstChild) list.removeChild(list.firstChild);
          Array.prototype.forEach.call(input.files, function (f) {
            var li = document.createElement('li');
            li.textContent = f.name;
            list.appendChild(li);
          });
          list.hidden = !input.files.length;
        }
        if (!note) return;
        note.textContent = bad ? note.getAttribute('data-error') : helper;
        note.classList.toggle('is-error', bad);
      });
    });
  }

  /* ===== Book: the date-first ticket =====
     Steps show one at a time and the progress line tracks them; without JS every step shows, with a native date field.
     Prefills from the query string, because the homepage ticket, the town pages and the Services bands all link here. */
  (function () {
    var form = $('[data-book]');
    if (!form) return;
    var steps = $$('[data-book-step]', form);
    var goes = $$('[data-book-go]', form);
    var progress = $('[data-book-progress]', form);
    var doneState = $('[data-book-done]');
    var failedState = $('[data-book-failed]');
    var current = 0, furthest = 0;
    var params = {};
    location.search.replace(/^\?/, '').split('&').forEach(function (pair) {
      var kv = pair.split('=');
      if (kv[0]) { try { params[kv[0]] = decodeURIComponent((kv[1] || '').replace(/\+/g, ' ')); } catch (e) {} }
    });

    /* the rail lands flush under the sticky chrome, with no scrap of banner or slats between them (critic, Book r1) */
    function landRail(el) {
      var header = $('.m-header');
      var line = header ? (parseFloat(getComputedStyle(header).top) || 0) + header.offsetHeight : 0;
      window.scrollBy({ top: el.getBoundingClientRect().top - line, behavior: reduceMotion ? 'auto' : 'smooth' });
    }
    function show(i, moveFocus) {
      current = i;
      furthest = Math.max(furthest, i);
      steps.forEach(function (s, n) { s.hidden = n !== i; });
      goes.forEach(function (b, n) {
        b.disabled = n > furthest;
        if (n === i) { b.setAttribute('aria-current', 'step'); } else { b.removeAttribute('aria-current'); }
      });
      if (progress) progress.style.setProperty('--done', (i + 1) / steps.length);
      if (moveFocus) {
        var h = $('[data-book-heading]', steps[i]);
        if (h) h.focus();
        landRail(form);
      }
    }
    goes.forEach(function (b) {
      b.addEventListener('click', function () { show(+b.getAttribute('data-book-go'), true); });
    });
    /* Book now, on the booking page: goes to the form instead of reloading and wiping the visitor's answers (critic, Book r1).
       The chrome stays identical on every page; only the click changes here. */
    $$('a[href="book.html"]').forEach(function (a) {
      if (form.contains(a)) return;
      a.addEventListener('click', function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || form.hidden) return;
        e.preventDefault();
        var menuClose = $('[data-menu]:not([hidden]) [data-menu-close]');
        if (menuClose) menuClose.click();
        show(current, false);
        landRail(form);
        var h = $('[data-book-heading]', steps[current]);
        if (h) h.focus();
      });
    });

    /* ---- calendar: real availability comes from the booking system later. Until then every day from tomorrow is open except Sundays (content/placeholders.md, open days) ---- */
    var cal = $('[data-cal]', form);
    var native = $('[data-cal-native]', form);
    var selected = '';
    var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var dayError = $('[data-book-dayerror]', form);
    function iso(d) { return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
    function longDate(value) {
      var p = value.split('-');
      var d = new Date(+p[0], +p[1] - 1, +p[2]);
      return DAYS[d.getDay()] + ', ' + MONTHS[d.getMonth()] + ' ' + d.getDate();
    }
    function isOpen(d, today) { return d > today && d.getDay() !== 0; }
    if (cal) {
      if (native) { native.disabled = true; }
      var grid = $('[data-cal-grid]', cal), title = $('[data-cal-title]', cal), empty = $('[data-cal-empty]', cal);
      var prev = $('[data-cal-prev]', cal), next = $('[data-cal-next]', cal);
      var now = new Date();
      var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      var view = new Date(today.getFullYear(), today.getMonth(), 1);
      var first = new Date(view), last = new Date(view.getFullYear(), view.getMonth() + 2, 1);   /* three months ahead */
      var render = function () {
        title.textContent = MONTHS[view.getMonth()] + ' ' + view.getFullYear();
        while (grid.firstChild) grid.removeChild(grid.firstChild);
        var lead = view.getDay(), open = 0;
        for (var i = 0; i < lead; i++) { grid.appendChild(document.createElement('span')); }
        var d = new Date(view);
        while (d.getMonth() === view.getMonth()) {
          var value = iso(d), ok = isOpen(d, today);
          var label = document.createElement('label');
          label.className = 'a-choice -cal' + (ok ? '' : ' -off');
          var input = document.createElement('input');
          input.className = 'a-choice__input'; input.type = 'radio'; input.name = 'day'; input.value = value;
          input.disabled = !ok;
          input.checked = value === selected;
          var face = document.createElement('span');
          face.className = 'a-choice__face';
          var sr = document.createElement('span');
          sr.className = 'sr-only';
          sr.textContent = DAYS[d.getDay()] + ', ' + MONTHS[d.getMonth()] + ' ';   /* reads "Friday, November 13", the US order (critic, Book r2) */
          face.appendChild(sr);
          face.appendChild(document.createTextNode(d.getDate()));
          label.appendChild(input); label.appendChild(face);
          grid.appendChild(label);
          if (ok) open++;
          d.setDate(d.getDate() + 1);
        }
        empty.hidden = open > 0;
        prev.disabled = view <= first;
        next.disabled = view >= last;
      };
      grid.addEventListener('change', function (e) { selected = e.target.value; dayError.hidden = true; });
      prev.addEventListener('click', function () { view = new Date(view.getFullYear(), view.getMonth() - 1, 1); render(); });
      next.addEventListener('click', function () { view = new Date(view.getFullYear(), view.getMonth() + 1, 1); render(); });
      if (params.day && /^\d{4}-\d{2}-\d{2}$/.test(params.day)) {
        var bits = params.day.split('-');
        var asked = new Date(+bits[0], +bits[1] - 1, +bits[2]);
        if (isOpen(asked, today) && asked < new Date(last.getFullYear(), last.getMonth() + 1, 1)) {
          selected = params.day;
          view = new Date(asked.getFullYear(), asked.getMonth(), 1);
        }
      }
      render();
    }
    $$('input[name="time"]', form).forEach(function (r) { r.addEventListener('change', function () { if (dayError) dayError.hidden = true; }); });

    /* ---- load: the price line follows the chip ---- */
    var priceLine = $('[data-book-price]', form);
    function setPrice() {
      var c = $('input[name="load"]:checked', form);
      if (!c || !priceLine) return;
      priceLine.textContent = c.getAttribute('data-price') ? 'From $' + c.getAttribute('data-price') + ' ' + c.getAttribute('data-unit') : priceLine.getAttribute('data-notsure');
    }
    $$('input[name="load"]', form).forEach(function (r) { r.addEventListener('change', setPrice); });

    /* ---- prefill ---- */
    function pickRadio(name, value) {
      var r = $$('input[name="' + name + '"]', form).filter(function (x) { return x.value === value; })[0];
      if (r) r.checked = true;
    }
    if (params.load) pickRadio('load', params.load);
    if (params.job) pickRadio('job', params.job);
    var townField = $('[data-book-town]', form);
    if (params.town && townField) townField.value = params.town;
    setPrice();

    /* ---- town: the check the error line promises (critic, Book r2). Same list and same approved lines as the homepage ticket.
       An unlisted town can still send a request: Shawn answers every one, and the line gives the number. ---- */
    var townNote = $('[data-book-town-note]', form);
    if (townField && townNote) {
      var townList = townField.getAttribute('data-towns').split('|');
      var townKey = function (s) { return s.toLowerCase().replace(/,.*$/, '').replace(/\s+(ma|nh)$/, '').trim(); };
      var checkBookTown = function () {
        var name = townKey(townField.value);
        var hit = townList.filter(function (t) { return townKey(t) === name; })[0];
        while (townNote.firstChild) townNote.removeChild(townNote.firstChild);
        townNote.hidden = !name;
        if (!name) return;
        if (hit) { townNote.textContent = 'Yes, we come to ' + hit + '.'; return; }
        townNote.appendChild(document.createTextNode('Not on our list yet. '));
        var callLink = document.createElement('a');
        callLink.className = 'm-field__smallLink';
        callLink.href = PHONE_HREF;
        callLink.textContent = 'Call ' + PHONE_TEXT;
        townNote.appendChild(callLink);
        townNote.appendChild(document.createTextNode(' and ask'));
      };
      townField.addEventListener('change', checkBookTown);
      checkBookTown();
    }

    /* ---- moving on: each step checks only what it needs ---- */
    function stepOk(i) {
      if (i === 0) {
        var good = selected && $('input[name="time"]:checked', form);
        if (dayError) dayError.hidden = !!good;
        return !!good;
      }
      return validate(steps[i]);
    }
    $$('[data-book-next]', form).forEach(function (b, i) {
      b.addEventListener('click', function () { if (stepOk(i)) show(i + 1, true); });
    });
    watchFields(form);
    setupUploads(form);

    /* ---- sending ---- */
    function finish(state) {
      form.hidden = true;
      state.hidden = false;
      state.focus();
      landRail(state);
    }
    function setSummary(key, value) {
      var el = $('[data-book-sum="' + key + '"]');
      if (el) el.textContent = value;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!stepOk(3)) return;
      var load = $('input[name="load"]:checked', form);
      var time = $('input[name="time"]:checked', form);
      setSummary('day', selected ? longDate(selected) : '');
      setSummary('time', time ? time.value : '');
      setSummary('load', load ? load.nextElementSibling.textContent : '');
      setSummary('price', load && load.getAttribute('data-price') ? '$' + load.getAttribute('data-price') : priceLine.getAttribute('data-notsure'));
      setSummary('address', [form.elements.street.value, form.elements.town.value, form.elements.zip.value].map(function (s) { return s.trim(); }).filter(Boolean).join(', '));
      sendForm(form, function () { finish(doneState); }, function () { finish(failedState); });
    });

    show(0, false);
  })();

  /* ===== Request forms (Contact, Commercial): one page, no steps =====
     A failed send keeps what the visitor typed and offers the phone (critic, Book r2: its error state had no way back to the filled form). Success only when the endpoint answered OK. */
  $$('[data-request]').forEach(function (form) {
    var done = $('[data-request-done]');
    var failed = $('[data-request-failed]');
    watchFields(form);
    setupUploads(form);
    /* a field that takes focus keeps its label clear of the sticky chrome (critic, Commercial r2). The browser leaves a field alone once it's on screen, even with its label under the header. Not a chip pressed with the mouse: moving it mid-press would lose the click, as the FAQ's minus did */
    form.addEventListener('focusin', function (e) {
      var header = $('.m-header');
      var field = e.target.closest('.m-field');
      var label = field && $('.a-label', field);
      if (!header || !label) return;
      try { if (!e.target.matches(':focus-visible')) return; } catch (err) { return; }
      var over = header.getBoundingClientRect().bottom + 8 - label.getBoundingClientRect().top;
      if (over > 0) window.scrollBy({ top: -over, behavior: 'instant' });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      failed.hidden = true;
      if (!validate(form)) return;
      sendForm(form, function () {
        var head = $('[data-request-head]');
        form.hidden = true;
        done.hidden = false;
        if (head) {
          head.classList.add('is-sent');
          head.scrollIntoView({ block: 'start', behavior: reduceMotion ? 'auto' : 'smooth' });
        }
        done.focus({ preventScroll: !!head });
      }, function () {
        failed.hidden = false;
        failed.focus();
      });
    });
  });

  /* ===== Commercial: How often shows only for regular pickups =====
     Its height eases in and out, as the FAQ rows do, and the row beside it follows. While it doesn't apply the fieldset is disabled, so its choice stays out of the send; choosing Regular pickups again brings the choice back. Without JS it simply stays on show. */
  (function () {
    var often = $('[data-rhythm-often]');
    if (!often) return;
    var shown = false;
    var move = null;
    function set(open) {
      if (open === shown) return;
      shown = open;
      often.disabled = !open;
      if (reduceMotion || !often.animate) { often.classList.toggle('is-open', open); return; }
      /* a negative margin takes the column's gap back as the height runs out, so nothing is left to jump on the last frame */
      var gap = parseFloat(getComputedStyle(often.parentNode).rowGap) || 0;
      /* a second click turns it round from where it is */
      var now = getComputedStyle(often);
      var from = { height: often.getBoundingClientRect().height + 'px', marginTop: move ? now.marginTop : (open ? -gap : 0) + 'px', opacity: move ? now.opacity : (open ? 0 : 1), overflow: 'clip' };
      if (move) { move.onfinish = null; move.cancel(); move = null; }
      often.classList.add('is-open');
      var full = often.getBoundingClientRect().height;
      move = often.animate([from, { height: (open ? full : 0) + 'px', marginTop: (open ? 0 : -gap) + 'px', opacity: open ? 1 : 0, overflow: 'clip' }], { duration: 600, easing: 'cubic-bezier(.22, 1, .36, 1)' });
      move.onfinish = function () {
        move = null;
        often.classList.toggle('is-open', open);
      };
    }
    often.disabled = true;
    $$('[data-rhythm]').forEach(function (radio) {
      radio.addEventListener('change', function () {
        if (radio.checked) set(radio.getAttribute('data-rhythm') === 'regular');
      });
      if (radio.checked) set(radio.getAttribute('data-rhythm') === 'regular');   /* a form the browser refilled on back */
    });
  })();

  /* ===== Reviews: filter the grid by job =====
     Each button's data-filter matches a card's data-job; "All" shows every card. The grid never leaves a gap (hidden, not faded out). Results fade in and the section's height eases to its new size, as everything else on the page moves (critic r2). The grid stays in view under the header because the page gets shorter (critic r1). */
  (function () {
    var box = $('[data-review-filter]');
    if (!box) return;
    var buttons = $$('[data-filter]', box);
    var cards = $$('[data-job]', box);
    var empty = $('[data-review-empty]', box);
    var grid = $('.o-reviews__grid', box);
    var header = $('.m-header');
    function choose(button) {
      var job = button.getAttribute('data-filter');
      var shown = 0;
      var before = box.offsetHeight;
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', b === button ? 'true' : 'false'); });
      cards.forEach(function (c) {
        var match = job === 'All' || c.getAttribute('data-job') === job;
        c.hidden = !match;
        if (match) {
          shown += 1;
          c.classList.add('is-inview');
          if (!reduceMotion && c.animate) c.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, easing: 'ease-out' });
        }
      });
      if (grid) grid.classList.toggle('is-filtered', job !== 'All');
      if (empty) empty.hidden = shown > 0;
      /* overflow clip, not hidden: hidden would make this box the sticky rail's scroller for the length of the move */
      if (!reduceMotion && box.animate) box.animate([{ height: before + 'px', overflow: 'clip' }, { height: box.offsetHeight + 'px', overflow: 'clip' }], { duration: 600, easing: 'cubic-bezier(.22, 1, .36, 1)' });
      var top = box.getBoundingClientRect().top;
      var under = header ? header.getBoundingClientRect().bottom : 0;
      if (top < under) window.scrollBy({ top: top - under, behavior: 'instant' });
    }
    buttons.forEach(function (b) {
      b.addEventListener('click', function () { choose(b); });
    });
  })();

  /* ===== FAQ: a row's height eases open and shut, as the site's other reveals move (critic, Reviews r2: instant reflow read as a jump) =====
     Native details: without JS or with reduced motion they simply open and shut, and find-in-page still opens them.
     The row stays open while it closes, so its answer is clipped away and not dropped. A second click turns it round from where it is. */
  (function () {
    var rows = $$('[data-faq]');
    if (!rows.length || reduceMotion || !rows[0].animate) return;
    rows.forEach(function (row) {
      var answer = $('.m-faq__a', row);
      var going = row.open;
      var move = null;
      row.addEventListener('toggle', function () { if (!move) going = row.open; });
      $('summary', row).addEventListener('click', function (e) {
        e.preventDefault();
        var from = row.getBoundingClientRect().height;
        if (move) { move.onfinish = null; move.cancel(); }
        going = !going;
        row.classList.toggle('is-shut', !going);
        row.open = false;
        var shut = row.getBoundingClientRect().height;
        row.open = true;
        var full = row.getBoundingClientRect().height;
        move = row.animate([{ height: from + 'px', overflow: 'clip' }, { height: (going ? full : shut) + 'px', overflow: 'clip' }], { duration: 700, easing: 'cubic-bezier(.22, 1, .36, 1)' });
        move.onfinish = function () {
          move = null;
          row.open = going;
          row.classList.remove('is-shut');
        };
        if (going) answer.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 700, easing: 'ease-out' });
      });
    });
  })();

  /* ===== Service area map: a town's row and its spot on the map light together =====
     Pointing at either, or tabbing to a row, marks both, so the list and the map read as one thing. */
  (function () {
    var marks = $$('[data-place]');
    if (!marks.length) return;
    function light(place, on) {
      marks.forEach(function (m) { if (m.getAttribute('data-place') === place) m.classList.toggle('is-lit', on); });
    }
    marks.forEach(function (m) {
      var place = m.getAttribute('data-place');
      function lit() { light(place, true); }
      function unlit() { light(place, false); }
      m.addEventListener('mouseenter', lit);
      m.addEventListener('mouseleave', unlit);
      m.addEventListener('focus', lit);
      m.addEventListener('blur', unlit);
    });
  })();

  /* ===== Footer columns: accordion rows on phones, plain columns from 641px =====
     Without JS every list shows. With JS, phones start closed; wider screens always show them. */
  (function () {
    var toggles = $$('[data-footer-toggle]');
    if (!toggles.length) return;
    var phone = window.matchMedia('(max-width: 640px)');
    function listOf(t) { return document.getElementById(t.getAttribute('aria-controls')); }
    function setAll() {
      toggles.forEach(function (t) {
        var open = !phone.matches || t.getAttribute('aria-expanded') === 'true';
        listOf(t).hidden = !open;
      });
    }
    toggles.forEach(function (t) {
      t.addEventListener('click', function () {
        var open = t.getAttribute('aria-expanded') !== 'true';
        t.setAttribute('aria-expanded', open ? 'true' : 'false');
        listOf(t).hidden = !open;
      });
    });
    phone.addEventListener('change', setAll);
    setAll();
  })();
})();
