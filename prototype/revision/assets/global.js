/* ===== Quick Haul: revision prototype, global JS (round 2, 2026-11-04) =====
   Loads after global.css. One file for every page: each block checks its element is there. One IIFE, plain ES5, no libraries: CSS transitions, the Web Animations API and IntersectionObserver. */
(function () {
  'use strict';

  var html = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(selector, root) { return (root || document).querySelector(selector); }
  function $$(selector, root) { return Array.prototype.slice.call((root || document).querySelectorAll(selector)); }

  /* ---- load sequence: starts when the headline's font is in, with a failsafe so nothing waits on a slow file ---- */
  (function () {
    var done = false;
    function start() {
      if (done) { return; }
      done = true;
      html.classList.add('is-loaded');
      rollIn();
    }
    if (document.fonts && document.fonts.load) {
      Promise.all([document.fonts.load('800 100px "Bio Sans"'), document.fonts.load('300 100px "Bio Sans"')]).then(start, start);
      window.setTimeout(start, 700);
    } else {
      start();
    }
  }());

  /* ---- the truck backs in from the right once and parks on the fold, the way a junk truck backs into a yard. Coming from the right it never crosses the words (critic r2).
          Its wheels turn by exactly the distance it travels, the other way round, so they never skid. The tail dips a little as it brakes, then settles ---- */
  function rollIn() {
    var svg = $('[data-truck-roll]');
    if (!svg || reduced || !svg.animate) { return; }
    var holder = svg.parentNode;
    var rect = holder.getBoundingClientRect();
    var distance = window.innerWidth - rect.left + 60;
    var wheelRadius = 60 * rect.width / 1064;    /* the drawing's tyre radius, on screen */
    var turn = distance / wheelRadius * 180 / Math.PI;
    var timing = { duration: 2100, easing: 'cubic-bezier(.18, .72, .24, 1)', delay: 180, fill: 'backwards' };

    holder.animate([{ transform: 'translateX(' + distance + 'px)' }, { transform: 'translateX(0)' }], timing);
    $$('.m-truck__spin', svg).forEach(function (wheel) {
      wheel.animate([{ transform: 'rotate(' + turn + 'deg)' }, { transform: 'rotate(0deg)' }], timing);
    });
    $$('.m-truck__body', svg).forEach(function (body) {
      body.animate([
        { transform: 'rotate(0deg)', offset: 0 },
        { transform: 'rotate(-.55deg)', offset: .5 },
        { transform: 'rotate(.14deg)', offset: .78 },
        { transform: 'rotate(0deg)', offset: 1 }
      ], { duration: 1100, delay: 1150, easing: 'ease-out' });
    });
  }

  /* ---- the current page's link in the header and menu, read from the address, so the chrome stays identical on every page ---- */
  (function () {
    var here = window.location.pathname.split('/').pop() || 'index.html';
    $$('.m-header__link, .m-menu__link').forEach(function (link) {
      if (link.getAttribute('href') === here) { link.setAttribute('aria-current', 'page'); }
    });
  }());

  /* ---- the logo settles into the bar over the first 32px of scroll. Tied to the scroll position, not a timer, so a hard flick can't catch it half way and sit it on a heading (critic r2-2).
          32px is short enough on every layout: the logo is back inside the bar before the first heading can reach it. With reduced motion it just switches, at 12px ---- */
  (function () {
    var header = $('[data-header]');
    if (!header) { return; }
    var last = -1;
    function settle() {
      var y = Math.max(window.pageYOffset, 0);
      var settled = reduced ? (y > 12 ? 1 : 0) : Math.min(y / 32, 1);
      if (settled === last) { return; }
      last = settled;
      header.style.setProperty('--logoSettled', settled);
    }
    settle();
    window.addEventListener('scroll', settle, { passive: true });
  }());

  /* ---- header states and the phone's call bar. The number shows once per screen (Varun: stop saying it again and again):
          the first screen's pill (data-call-here, on a hero or banner that carries one) while it's on screen, the header or the phone's bar in the middle of the page, the footer's at the end ---- */
  (function () {
    var header = $('[data-header]');
    var heroCall = $('[data-call-here]');
    var footer = $('.o-footer');
    var bar = $('[data-action-bar]');
    if (!header || !footer || !window.IntersectionObserver) { return; }
    var heroInView = !!heroCall;
    var footerInView = false;
    function sync() {
      var elsewhere = heroInView || footerInView;
      header.classList.toggle('is-callElsewhere', elsewhere);
      if (bar) { bar.classList.toggle('is-shown', !elsewhere); }
    }
    sync();
    if (heroCall) {
      new IntersectionObserver(function (entries) {
        heroInView = entries[0].isIntersecting;
        sync();
      }, { rootMargin: (-header.offsetHeight) + 'px 0px 0px 0px' }).observe(heroCall);
    }
    new IntersectionObserver(function (entries) {
      footerInView = entries[0].isIntersecting;
      sync();
    }).observe(footer);
  }());

  /* ---- menu: a real dialog. Inert page, focus trap, Escape, focus returns to the button ---- */
  (function () {
    var menu = $('[data-menu]');
    var opener = $('[data-menu-open]');
    if (!menu || !opener) { return; }
    var others = [$('[data-header]'), $('#main'), $('.o-estimate'), $('.o-footer'), $('[data-action-bar]')];

    function setInert(on) {
      others.forEach(function (el) { if (el) { el.inert = on; } });
    }
    function focusables() {
      return $$('a[href], button:not([disabled])', menu);
    }
    function close() {
      menu.hidden = true;
      opener.setAttribute('aria-expanded', 'false');
      setInert(false);
      document.body.style.overflow = '';
      opener.focus();
    }
    opener.addEventListener('click', function () {
      menu.hidden = false;
      opener.setAttribute('aria-expanded', 'true');
      setInert(true);
      document.body.style.overflow = 'hidden';
      focusables()[0].focus();
    });
    $$('[data-menu-close]', menu).forEach(function (el) { el.addEventListener('click', close); });
    /* a link to a spot on the page you're already on (Pricing, on Services) doesn't load a new page, so the menu has to close itself */
    $$('a[href]', menu).forEach(function (el) { el.addEventListener('click', close); });
    menu.addEventListener('click', function (event) { if (event.target === menu) { close(); } });
    menu.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') { close(); return; }
      if (event.key !== 'Tab') { return; }
      var items = focusables();
      var first = items[0];
      var last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    });
  }());

  /* ---- priced by the load: pick a pill, the load lands in the truck piece by piece, the body sits a little lower, the price follows.
          CSS transitions, not keyframes, so tapping quickly through the pills retargets instead of restarting ---- */
  (function () {
    var section = $('[data-gauge]');
    if (!section) { return; }
    var svg = $('[data-truck-gauge]', section);
    var picker = $('[data-load-picker]', section);
    var items = $$('[data-truck-level]', svg);
    var price = $('[data-gauge-price]', section);
    var unit = $('[data-gauge-unit]', section);
    var note = $('[data-gauge-note]', section);
    var shown = 1;

    function setLevel(level) {
      var entering = 0;
      items.forEach(function (item) {
        var on = Number(item.getAttribute('data-truck-level')) <= level;
        var wasOff = item.classList.contains('-off');
        if (on && wasOff) {
          item.style.transitionDelay = reduced ? '0ms' : (180 + entering * 45) + 'ms';
          entering += 1;
        } else {
          item.style.transitionDelay = '0ms';
        }
        item.classList.toggle('-off', !on);
      });
      svg.setAttribute('data-level', level);
      if (picker) { picker.setAttribute('data-level', level); }
      shown = level;
    }
    $$('input[name="load"]', section).forEach(function (input) {
      input.addEventListener('change', function () {
        if (!input.checked) { return; }
        setLevel(Number(input.getAttribute('data-level')));
        price.textContent = input.getAttribute('data-price');
        unit.textContent = input.getAttribute('data-unit');
        note.textContent = input.getAttribute('data-note');
        svg.setAttribute('aria-label', 'The Quick Haul truck carrying ' + input.getAttribute('data-label'));
      });
    });
    /* a browser restoring the form on Back keeps the pick: match the truck to it */
    var picked = $('input[name="load"]:checked', section);
    if (picked && picked.getAttribute('data-level') !== '1') {
      setLevel(Number(picked.getAttribute('data-level')));
      price.textContent = picked.getAttribute('data-price');
      unit.textContent = picked.getAttribute('data-unit');
      note.textContent = picked.getAttribute('data-note');
    }
    if (shown) { svg.setAttribute('data-level', shown); }
  }());

  /* ---- before and after: two clipped layers. It rests at 50% and eases there from 68% the first time it comes into view, to show it moves.
          The range input takes keyboard and screen readers. The pointer is handled here, because a native range jumps to the finger on any touch:
          on touch nothing moves until the gesture is clearly sideways, so a vertical swipe just scrolls the page ---- */
  (function () {
    var box = $('[data-compare]');
    if (!box) { return; }
    var range = $('[data-compare-range]', box);
    var touched = false;
    var dragging = false;
    var undecided = false;
    var startX = 0;
    var startY = 0;
    function set(v) {
      box.style.setProperty('--pos', v + '%');
      /* the slider says what it shows, not a bare number (critic r2) */
      range.setAttribute('aria-valuetext', Math.round(v) + ' percent before, ' + (100 - Math.round(v)) + ' percent after');
    }
    function follow(x) {
      var rect = box.getBoundingClientRect();
      var v = Math.max(0, Math.min(100, (x - rect.left) / rect.width * 100));
      range.value = v;
      set(v);
    }
    function grab(event) {
      dragging = true;
      undecided = false;
      box.classList.add('is-dragging');
      try { box.setPointerCapture(event.pointerId); } catch (e) {}
    }
    function release() {
      dragging = false;
      undecided = false;
      box.classList.remove('is-dragging');
    }
    range.addEventListener('input', function () { touched = true; set(range.value); });
    box.addEventListener('pointerdown', function (event) {
      if (event.pointerType === 'mouse' && event.button !== 0) { return; }
      touched = true;
      startX = event.clientX;
      startY = event.clientY;
      if (event.pointerType === 'mouse') {
        event.preventDefault();
        grab(event);
        follow(event.clientX);
        range.focus({ preventScroll: true });
      } else {
        undecided = true;
      }
    });
    box.addEventListener('pointermove', function (event) {
      if (undecided) {
        var dx = Math.abs(event.clientX - startX);
        var dy = Math.abs(event.clientY - startY);
        if (dx > 6 && dx > dy) { grab(event); }
        else if (dy > 6) { undecided = false; }
      }
      if (dragging) { follow(event.clientX); }
    });
    box.addEventListener('pointerup', release);
    box.addEventListener('pointercancel', release);
    set(range.value);
    if (reduced || !window.IntersectionObserver) { return; }
    var observer = new IntersectionObserver(function (entries) {
      if (!entries[0].isIntersecting) { return; }
      observer.disconnect();
      var startTime = null;
      function step(now) {
        if (touched) { return; }
        if (startTime === null) { startTime = now; }
        var t = Math.min((now - startTime) / 1300, 1);
        var eased = 1 - Math.pow(1 - t, 4);
        set(68 + (50 - 68) * eased);
        if (t < 1) { window.requestAnimationFrame(step); }
      }
      set(68);
      window.requestAnimationFrame(step);
    }, { threshold: .45 });
    observer.observe(box);
  }());

  /* ---- in-view reveals, once each; tiles in the same row stagger a little ---- */
  (function () {
    var marked = $$('.a-inview');
    if (reduced || !window.IntersectionObserver) {
      marked.forEach(function (el) { el.classList.add('is-inview'); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, i) {
        if (!entry.isIntersecting) { return; }
        entry.target.style.transitionDelay = (i * 60) + 'ms';
        entry.target.classList.add('is-inview');
        observer.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    marked.forEach(function (el) { observer.observe(el); });
  }());
}());
