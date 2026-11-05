/* =====================================================================
   Quick Haul: global script (revision rebuild, 2026-11-05)
   Loads deferred on every page, after assets/global.css. Nothing loads after it. No libraries.
   Every block checks for its element first, so one file serves every page. One IIFE, plain ES5: CSS transitions,
   the Web Animations API and IntersectionObserver. The new look's blocks are lifted from prototype/revision/assets/global.js.
   ===================================================================== */
(function () {
  'use strict';

  /* ---- config, flags, helpers ---- */
  var PHONE_HREF = 'tel:+16035550142';      /* placeholder number, content/placeholders.md */
  var PHONE_TEXT = '(603) 555-0142';
  var html = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(selector, ctx) { return (ctx || document).querySelector(selector); }
  function $$(selector, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(selector)); }
  function raf(fn) { var queued = false; return function () { if (queued) { return; } queued = true; window.requestAnimationFrame(function () { queued = false; fn(); }); }; }

  /* ---- load sequence: starts when the headline's font is in, with a failsafe so nothing waits on a slow file ---- */
  (function () {
    var done = false;
    function start() {
      if (done) { return; }
      done = true;
      html.classList.add('is-loaded');
      /* the headline's rows have risen by now (240ms stagger + 1100ms): their mask comes off */
      window.setTimeout(function () { html.classList.add('is-risen'); }, 1500);
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
    var path = window.location.pathname;
    var here = path.split('/').pop() || 'index.html';
    /* a town page sits inside Towns: a visitor from search gets a sign of where it is (critic, hub and towns r1) */
    var inTowns = path.indexOf('/service-area/') !== -1;
    $$('.m-header__link, .m-menu__link').forEach(function (link) {
      var href = link.getAttribute('href');
      if (href === here) { link.setAttribute('aria-current', 'page'); }
      else if (inTowns && href === '../service-area.html') { link.setAttribute('aria-current', 'true'); }
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
    var heroCalls = $$('[data-call-here]');   /* usually one; Book has one in the rail and one in each end state, and at most one is showing */
    var footer = $('.o-footer');
    var bar = $('[data-action-bar]');
    /* is-callReady lifts the CSS start state that stops the number flashing before this block has run */
    if (header && (!footer || !window.IntersectionObserver)) { header.classList.add('is-callReady'); }
    if (!header || !footer || !window.IntersectionObserver) { return; }
    var heroInView = heroCalls.length > 0;
    var footerInView = false;
    /* a form's own button wins over the bar: the bar steps aside while that button sits in the bar's band (critic, Book r2: 8px of Send was under it) */
    var clear = $$('[data-bar-clear]');
    function blocked() {
      if (!bar) { return false; }
      var top = window.innerHeight - bar.offsetHeight;
      /* the service a jump chip just landed on counts too: its own booking link wins over the bar, on a phone of any height, and no other link makes the bar flicker as the page scrolls past (critic, Services r2) */
      return clear.concat($$(':target .a-button, :target .a-link')).some(function (b) {
        var r = b.getBoundingClientRect();
        return r.height > 0 && r.bottom > top && r.top < window.innerHeight;
      });
    }
    function sync() {
      var elsewhere = heroInView || footerInView;
      header.classList.toggle('is-callElsewhere', elsewhere);
      if (bar) { bar.classList.toggle('is-shown', !elsewhere && !blocked()); }
    }
    sync();
    header.classList.add('is-callReady');
    if (clear.length || $('.m-jump')) {
      var later = raf(sync);
      window.addEventListener('scroll', later, { passive: true });
      window.addEventListener('resize', later);
      window.addEventListener('hashchange', later);
      /* errors and step changes move the button with no scroll event */
      document.addEventListener('click', later);
      document.addEventListener('input', later);
    }
    if (heroCalls.length) {
      var callsSeen = [];
      var callWatcher = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          var at = callsSeen.indexOf(entry.target);
          /* coming up the screen, most of a pill has to show, or 40px of something taller like Book's rail: with a sliver in view, neither number could be read (critic, About r1). Going under the header, it counts until it has gone, or the number shows twice (critic, About r2) */
          var box = entry.boundingClientRect;
          var seen = entry.isIntersecting && (box.top < entry.rootBounds.top || entry.intersectionRect.height >= Math.min(box.height * .6, 40));
          if (seen && at < 0) { callsSeen.push(entry.target); }
          if (!seen && at >= 0) { callsSeen.splice(at, 1); }
        });
        heroInView = callsSeen.length > 0;
        sync();
      }, { rootMargin: (-header.offsetHeight) + 'px 0px 0px 0px', threshold: [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1] });
      heroCalls.forEach(function (el) { callWatcher.observe(el); });
    }
    /* the whole footer: the band above carries its own number, and the bar must not sit over the footer's last line at the foot of the page */
    new IntersectionObserver(function (entries) {
      footerInView = entries[0].isIntersecting;
      sync();
    }).observe(footer);
  }());

  /* ---- a town page's every Book link carries its town, not only the page's own: someone who reads to the estimate band and books there shouldn't type it again (critic, hub and towns r1). The chrome stays identical on every page; the page's wrapper says which town. Added to the link's own address, not built ---- */
  (function () {
    var page = $('[data-town-query]');
    if (!page) { return; }
    $$('a[href$="book.html"]').forEach(function (a) {
      a.setAttribute('href', a.getAttribute('href') + '?town=' + page.getAttribute('data-town-query'));
    });
  }());

  /* ---- jump chips on phones: a chip reached by keyboard comes fully into view with its ring. The browser's own focus scroll left it cut off at the row's edge, 38px of "Pricing" at 390 (critic, Services r2). Keyboard only, so a tap doesn't start a second scroll ---- */
  (function () {
    var row = $('.m-jump');
    if (!row || !row.scrollTo) { return; }
    row.addEventListener('focusin', function (event) {
      var link = event.target;
      if (row.scrollWidth <= row.clientWidth || !link.matches(':focus-visible')) { return; }
      var box = link.getBoundingClientRect();
      var frame = row.getBoundingClientRect();
      row.scrollTo({ left: row.scrollLeft + box.left - frame.left - (frame.width - box.width) / 2, behavior: reduced ? 'auto' : 'smooth' });
    });
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
    /* Book only: the line that holds the price, hidden when there's no set price. Home has neither this line nor job chips, and always has a pick */
    var line = $('[data-gauge-line]', section);
    var shown = 1;

    function setLevel(level) {
      /* Lowest load first, so the bed fills before the heap lands on it. In drawing order the top of the pile came first and hung over an empty bed (critic, Book r1) */
      var landing = [];
      items.forEach(function (item) {
        var on = Number(item.getAttribute('data-truck-level')) <= level;
        if (on && item.classList.contains('-off')) { landing.push(item); }
        item.style.transitionDelay = '0ms';
        item.classList.toggle('-off', !on);
      });
      landing.sort(function (a, b) { return a.getAttribute('data-truck-level') - b.getAttribute('data-truck-level'); });
      landing.forEach(function (item, n) { item.style.transitionDelay = reduced ? '0ms' : (180 + n * 45) + 'ms'; });
      svg.setAttribute('data-level', level);
      if (picker) { picker.setAttribute('data-level', level); }
      shown = level;
    }
    /* What the current pick costs. On Book there can be no pick, "Not sure" or a demo job, and then a line takes the price's place (copy.md, Book: load step). Book's prefill sends a change event, so ?load= and ?job= land here too */
    function readout() {
      var input = $('input[name="load"]:checked', section);
      var job = $('input[name="job"]:checked', section);
      var isDemo = !!job && job.value === 'demo';
      var level = input ? Number(input.getAttribute('data-level')) : 0;
      var hasPrice = !!input && !!input.getAttribute('data-price') && !isDemo;
      setLevel(level);
      if (line) { line.hidden = !hasPrice; }
      if (hasPrice) {
        price.textContent = input.getAttribute('data-price');
        unit.textContent = input.getAttribute('data-unit');
      }
      if (isDemo) { note.textContent = note.getAttribute('data-demo'); }
      else { note.textContent = input ? input.getAttribute('data-note') : note.getAttribute('data-empty'); }
      /* an empty truck is decorative (copy.md, Truck labels) */
      if (level) {
        svg.removeAttribute('aria-hidden');
        svg.setAttribute('aria-label', 'The Quick Haul truck carrying ' + input.getAttribute('data-label'));
      } else {
        svg.setAttribute('aria-hidden', 'true');
      }
    }
    $$('input[name="load"], input[name="job"]', section).forEach(function (input) {
      input.addEventListener('change', readout);
    });
    /* also covers a browser restoring the form on Back */
    readout();
    if (shown) { svg.setAttribute('data-level', shown); }
  }());

  /* ---- before and after: two clipped layers. It rests at 50% and eases there from 68% the first time it comes into view, to show it moves.
          The range input takes keyboard and screen readers. The pointer is handled here, because a native range jumps to the finger on any touch:
          on touch nothing moves until the gesture is clearly sideways, so a vertical swipe just scrolls the page ---- */
  $$('[data-compare]').forEach(function (box) {
    var range = $('[data-compare-range]', box);
    var tagBefore = $('.m-compare__tag:not(.-after)', box);
    var tagAfter = $('.m-compare__tag.-after', box);
    var touched = false;
    var dragging = false;
    var undecided = false;
    var startX = 0;
    var startY = 0;
    function set(v) {
      box.style.setProperty('--pos', v + '%');
      /* the slider says what it shows, not a bare number (critic r2) */
      range.setAttribute('aria-valuetext', Math.round(v) === 50 ? 'Half before, half after' : Math.round(v) + ' percent before, ' + (100 - Math.round(v)) + ' percent after');
      /* a tag fades as the divider reaches it, so it's never cut mid-word (critic, Reviews r1) */
      var x = box.clientWidth * v / 100;
      if (tagBefore) { tagBefore.classList.toggle('is-covered', x < tagBefore.offsetLeft + tagBefore.offsetWidth); }
      if (tagAfter) { tagAfter.classList.toggle('is-covered', x > tagAfter.offsetLeft); }
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
    range.addEventListener('keydown', function () { box.classList.remove('is-pointer'); });
    box.addEventListener('pointerdown', function (event) {
      if (event.pointerType === 'mouse' && event.button !== 0) { return; }
      touched = true;
      startX = event.clientX;
      startY = event.clientY;
      if (event.pointerType === 'mouse') {
        event.preventDefault();
        grab(event);
        follow(event.clientX);
        box.classList.add('is-pointer');
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
  });

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

  /* ===== FAQ: a row's height eases open and shut, as the site's other reveals move (critic, Reviews r2: instant reflow read as a jump) =====
     Native details: without JS or with reduced motion they simply open and shut, and find-in-page still opens them.
     The row stays open while it closes, so its answer is clipped away and not dropped. A second click turns it round from where it is. */
  (function () {
    var rows = $$('[data-faq]');
    if (!rows.length) return;
    /* an answer opening under the fold showed nothing but the plus turning to a minus (critic, FAQ r1): the row comes up far enough to show it, never past the header */
    function showWhole(row, height) {
      var bar = $('[data-action-bar]');
      var floor = window.innerHeight - (bar && bar.classList.contains('is-shown') ? bar.offsetHeight : 0) - 16;
      var roof = $('.m-header').getBoundingClientRect().bottom + 8;
      var top = row.getBoundingClientRect().top;
      var over = top + height - floor;
      if (over > 0 && top > roof) { window.scrollBy({ top: Math.min(over, top - roof), behavior: reduced ? 'auto' : 'smooth' }); }
    }
    if (reduced || !rows[0].animate) {
      rows.forEach(function (row) {
        var pressed = false;
        $('summary', row).addEventListener('click', function () { pressed = true; });
        row.addEventListener('toggle', function () {
          if (row.open && pressed) { showWhole(row, row.getBoundingClientRect().height); }
          pressed = false;
        });
      });
      return;
    }
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
        if (going) { showWhole(row, full); }
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
    if (input.hasAttribute('data-email') && v && !EMAIL_RE.test(v)) return input.getAttribute('data-error-format') || input.getAttribute('data-error');
    if (input.hasAttribute('data-phone') && v && v.replace(/\D/g, '').length < 10) return input.getAttribute('data-error');   /* the phone is how Shawn confirms the booking (critic, Book r1) */
    return '';
  }
  function showFieldError(input, message) {
    /* the first id only, so a field can also point at a helper line */
    var note = document.getElementById((input.getAttribute('aria-describedby') || '').split(' ')[0]);
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
    /* one send at a time: a double click or a second Enter on a slow line would send the request twice. aria-busy also dims the button (global.css) */
    if (form.getAttribute('aria-busy') === 'true') { return; }
    form.setAttribute('aria-busy', 'true');
    function settle(then) { return function () { form.removeAttribute('aria-busy'); then(); }; }
    fetch(url, { method: 'POST', body: new FormData(form) }).then(function (r) {
      settle(r.ok ? done : failed)();
    }, settle(failed));
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
          /* "Remove" comes from data-remove on the list, so the word stays in the HTML */
          var removeWord = list.getAttribute('data-remove');
          Array.prototype.forEach.call(input.files, function (f, index) {
            var li = document.createElement('li');
            li.className = 'm-upload__file';
            li.appendChild(document.createTextNode(f.name));
            var remove = document.createElement('button');
            remove.type = 'button';
            remove.className = 'm-upload__remove';
            remove.textContent = removeWord;
            remove.setAttribute('aria-label', removeWord + ' ' + f.name);
            remove.addEventListener('click', function () {
              var keep = new DataTransfer();
              Array.prototype.forEach.call(input.files, function (g, i) { if (i !== index) { keep.items.add(g); } });
              input.files = keep.files;
              input.dispatchEvent(new Event('change'));
            });
            li.appendChild(remove);
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

  /* an optional chip can be taken back: a second press clears it, by mouse, touch or Space. A radio can't do that alone (critic, Book r2) */
  function clearable(radios) {
    radios.forEach(function (r) {
      var wasOn = false;
      r.addEventListener('pointerdown', function () { wasOn = r.checked; });
      function clear() {
        if (wasOn) {
          r.checked = false;
          r.dispatchEvent(new Event('change', { bubbles: true }));
        }
        wasOn = false;
      }
      r.addEventListener('click', clear);
      /* a browser sends no click for Space on a radio that's already on, so it's handled here */
      r.addEventListener('keydown', function (e) { if (e.key === ' ') { wasOn = r.checked; } });
      r.addEventListener('keyup', function (e) {
        /* preventDefault: with the radio off by now, the browser's own keyup would turn it straight back on */
        if (e.key === ' ' && wasOn) { e.preventDefault(); clear(); }
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

    /* the card lands 20px under the header, so its round corners and top line show. Flush, it parked jammed against the bar on every step (critic, Book r1) */
    function landRail(el) {
      var header = $('.m-header');
      var line = header ? (parseFloat(getComputedStyle(header).top) || 0) + header.offsetHeight : 0;
      window.scrollBy({ top: el.getBoundingClientRect().top - line - 20, behavior: reduced ? 'auto' : 'smooth' });
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
          label.className = 'a-choice -light -cal' + (ok ? '' : ' -off');
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
      /* Up and Down go by week, as on any calendar; left and right stay the radios' own (critic, Book r2) */
      grid.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') { return; }
        var days = $$('input[name="day"]', grid);
        var to = days[days.indexOf(e.target) + (e.key === 'ArrowDown' ? 7 : -7)];
        e.preventDefault();
        if (to && !to.disabled) {
          to.checked = true;
          to.focus();
          to.dispatchEvent(new Event('change', { bubbles: true }));
        }
      });
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

    /* ---- prefill ---- */
    function pickRadio(name, value) {
      var r = $$('input[name="' + name + '"]', form).filter(function (x) { return x.value === value; })[0];
      if (!r) return;
      r.checked = true;
      r.dispatchEvent(new Event('change'));
    }
    if (params.load) pickRadio('load', params.load);
    if (params.job) pickRadio('job', params.job);
    var townField = $('[data-book-town]', form);
    if (params.town && townField) townField.value = params.town;

    /* ---- town: the check the helper line promises, as you type (critic, Book r1: it only ran on leaving the field, and a stale yes sat beside new text).
       A state that's typed has to match: "Salem, MA" got Salem, NH's yes (critic, Book r1). While the words could still become a listed town the helper stays; on leaving the field, a listed town is written out in full.
       An unlisted town can still send a request: Shawn answers every one, and the line gives the number. ---- */
    var townNote = $('[data-book-town-note]', form);
    if (townField && townNote) {
      var townList = townField.getAttribute('data-towns').split('|');
      var townPlain = function (s) { return s.toLowerCase().replace(/\./g, '').replace(/,/g, ' ').replace(/\s+/g, ' ').trim(); };
      var findTown = function (plain) {
        var m = plain.match(/^(.*?)(?: (ma|mass|massachusetts|nh|new hampshire))?$/);
        return townList.filter(function (t) {
          var parts = t.toLowerCase().split(', ');
          return parts[0] === m[1] && (!m[2] || parts[1].charAt(0) === m[2].charAt(0));
        })[0];
      };
      var townShown = null;
      var checkBookTown = function (typing) {
        var plain = townPlain(townField.value);
        var hit = plain ? findTown(plain) : '';
        var early = typing && !hit && townList.some(function (t) { return townPlain(t).indexOf(plain) === 0; });
        /* "Salem, N" on its way to "Salem, NH" keeps the yes it already had */
        if (early && plain.indexOf(' ') > 0) { hit = findTown(plain.slice(0, plain.lastIndexOf(' '))) || ''; early = !hit; }
        var verdict = !plain || early ? 'default' : (hit || 'no');
        /* only when the line really changes: it's a live region */
        if (verdict === townShown) { return; }
        townShown = verdict;
        while (townNote.firstChild) townNote.removeChild(townNote.firstChild);
        if (verdict === 'default') { townNote.textContent = townNote.getAttribute('data-default'); return; }
        if (hit) { townNote.textContent = 'Yes, we come to ' + hit + '.'; return; }
        townNote.appendChild(document.createTextNode('Not on our list yet. '));
        var callLink = document.createElement('a');
        callLink.className = 'a-inlineLink';
        callLink.href = PHONE_HREF;
        callLink.appendChild(document.createTextNode('Call '));
        /* the number in its own face and on one line, like every other number (critic, Book r1: it broke across two lines at 1440) */
        var callNumber = document.createElement('span');
        callNumber.className = 'a-num';
        callNumber.textContent = PHONE_TEXT;
        callLink.appendChild(callNumber);
        townNote.appendChild(callLink);
        townNote.appendChild(document.createTextNode(' and ask'));
      };
      townField.addEventListener('input', function () { checkBookTown(true); });
      townField.addEventListener('change', function () {
        checkBookTown(false);
        var hit = findTown(townPlain(townField.value));
        if (hit) { townField.value = hit; }
      });
      checkBookTown(false);
    }

    /* ---- moving on: each step checks only what it needs ---- */
    function stepOk(i) {
      if (i === 0) {
        var good = selected && $('input[name="time"]:checked', form);
        if (dayError) dayError.hidden = !!good;
        /* The line goes beside what's missing and focus goes to it, as the Address step does: at 390 the calendar was a screen above the button that said so (critic, Book r1) */
        if (!good && dayError) {
          var missing = selected ? $('.o-book__chips', steps[0]) : cal;
          missing.parentNode.insertBefore(dayError, missing);
          /* parks clear of the bar with the group's label in view: on the line itself, PICK A DAY sat cut under the header (critic, Book r2) */
          if (selected) { missing.closest('fieldset').scrollIntoView({ block: 'nearest', behavior: reduced ? 'auto' : 'smooth' }); }
          else { landRail(form); }
          var firstChoice = $(selected ? 'input[name="time"]' : 'input[name="day"]:not([disabled])', steps[0]);
          if (firstChoice) { firstChoice.focus({ preventScroll: true }); }
        }
        return !!good;
      }
      return validate(steps[i]);
    }
    $$('[data-book-next]', form).forEach(function (b, i) {
      b.addEventListener('click', function () { if (stepOk(i)) show(i + 1, true); });
    });
    watchFields(form);
    setupUploads(form);

    /* ---- the progress line fills in with the visitor's own answers, the way a work order does, so a day picked in another month or a load that came with a link still shows (critic, Book r2) ---- */
    function showAnswers() {
      $$('[data-book-answer]', form).forEach(function (el) {
        var key = el.getAttribute('data-book-answer');
        var text = '';
        if (key === 'day' && selected) {
          var p = selected.split('-');
          var d = new Date(+p[0], +p[1] - 1, +p[2]);
          text = DAYS[d.getDay()].slice(0, 3) + ', ' + MONTHS[d.getMonth()].slice(0, 3) + ' ' + d.getDate();
        }
        if (key === 'load') {
          var pick = $('input[name="load"]:checked', form);
          text = pick ? pick.nextElementSibling.textContent : '';
        }
        if (key === 'address' && townField) { text = townField.value.split(',')[0].trim(); }
        el.textContent = text;
        el.hidden = !text;
      });
    }
    form.addEventListener('change', showAnswers);
    showAnswers();

    clearable($$('input[name="job"], input[name="where"]', form));   /* Demo hides the price, so it has to be possible to take it back */

    /* ---- sending ---- */
    var card = form.closest('.o-book');
    function finish(state) {
      form.hidden = true;
      state.hidden = false;
      if (card) { card.classList.add('is-finished'); }
      state.focus();
      landRail(state);
    }
    /* the done state parks the truck they filled: a copy of the load step's drawing, as it stands. Decorative: the summary beside it says the same in words */
    function parkTruck() {
      var holder = $('[data-book-done-truck]');
      var gauge = $('[data-truck-gauge]', form);
      if (!holder || !gauge) { return; }
      var copy = gauge.cloneNode(true);
      copy.removeAttribute('data-truck-gauge');
      copy.removeAttribute('role');
      copy.removeAttribute('aria-label');
      copy.setAttribute('aria-hidden', 'true');
      while (holder.firstChild) { holder.removeChild(holder.firstChild); }
      holder.appendChild(copy);
    }
    function setSummary(key, value) {
      var el = $('[data-book-sum="' + key + '"]');
      if (el) { el.textContent = value; el.parentNode.hidden = !value; }
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!stepOk(3)) return;
      var load = $('input[name="load"]:checked', form);
      var time = $('input[name="time"]:checked', form);
      setSummary('day', selected ? longDate(selected) : '');
      setSummary('time', time ? time.value : '');
      setSummary('load', load ? load.nextElementSibling.textContent : '');
      var job = $('input[name="job"]:checked', form);
      var hasPrice = load && load.getAttribute('data-price') && !(job && job.value === 'demo');
      var priceCell = $('[data-book-sum="price"]');
      var noPrice = priceCell.getAttribute('data-none');
      setSummary('price', hasPrice ? load.getAttribute('data-price').replace(/^\$?/, '$') : noPrice);
      setSummary('address', [form.elements.street.value, form.elements.town.value, form.elements.zip.value].map(function (s) { return s.trim(); }).filter(Boolean).join(', '));
      sendForm(form, function () { parkTruck(); finish(doneState); }, function () { finish(failedState); });
    });

    /* copy.md: "Your details are still here, so try again": hiding the form never cleared it */
    var retry = $('[data-book-retry]');
    if (retry) {
      retry.addEventListener('click', function () {
        failedState.hidden = true;
        form.hidden = false;
        if (card) { card.classList.remove('is-finished'); }
        show(current, true);
      });
    }

    show(0, false);
  })();

  /* ===== Request forms (Contact, Commercial): one page, no steps =====
     A failed send keeps what the visitor typed and offers the phone (critic, Book r2: its error state had no way back to the filled form). Success only when the endpoint answered OK. */
  $$('[data-request]').forEach(function (form) {
    var done = $('[data-request-done]');
    var failed = $('[data-request-failed]');
    watchFields(form);
    setupUploads(form);
    clearable($$('[data-clearable]', form));
    /* a field that takes focus keeps its label clear of the sticky chrome (critic, Commercial r2). The browser leaves a field alone once it's on screen, even with its label under the header. Not a chip pressed with the mouse: moving it mid-press would lose the click, as the FAQ's minus did */
    form.addEventListener('focusin', function (e) {
      var header = $('.m-header');
      var field = e.target.closest('.m-field');
      var label = field && $('.a-label, .m-field__label', field);
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
          head.scrollIntoView({ block: 'start', behavior: reduced ? 'auto' : 'smooth' });
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
      if (reduced || !often.animate) { often.classList.toggle('is-open', open); return; }
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
      /* asks the group, not this radio: a second press clears the chip, and How often has to go with it */
      radio.addEventListener('change', function () {
        var on = $('[data-rhythm]:checked');
        set(!!on && on.getAttribute('data-rhythm') === 'regular');
      });
      if (radio.checked) set(radio.getAttribute('data-rhythm') === 'regular');   /* a form the browser refilled on back */
    });
  })();

  /* ===== Service area map: a real street map, loaded only when its slot nears the screen, with a pin per town =====
     Pointing at a town's chip or its pin, or tabbing to the chip, marks both, so the list and the map read as one thing.
     The library and tiles come from outside the site. If any of it fails, the slot shows its towns as chips. */
  (function () {
    var slots = $$('[data-map]');
    var chips = $$('[data-place]');

    function light(place, on) {
      $$('[data-place]').forEach(function (m) { if (m.getAttribute('data-place') === place) { m.classList.toggle('is-lit', on); } });
    }
    function wire(m) {
      var place = m.getAttribute('data-place');
      function lit() { light(place, true); }
      function unlit() { light(place, false); }
      m.addEventListener('mouseenter', lit);
      m.addEventListener('mouseleave', unlit);
      m.addEventListener('focus', lit);
      m.addEventListener('blur', unlit);
    }
    chips.forEach(wire);
    if (!slots.length) { return; }

    var LIB_JS = 'https://cdn.jsdelivr.net/npm/maplibre-gl@4.7.1/dist/maplibre-gl.js';
    var LIB_CSS = 'https://cdn.jsdelivr.net/npm/maplibre-gl@4.7.1/dist/maplibre-gl.css';
    var LIB_JS_SRI = 'sha384-SYKAG6cglRMN0RVvhNeBY0r3FYKNOJtznwA0v7B5Vp9tr31xAHsZC0DqkQ/pZDmj';
    var LIB_CSS_SRI = 'sha384-MinO0mNliZ3vwppuPOUnGa+iq619pfMhLVUXfC4LHwSCvF9H+6P/KO4Q7qBOYV5V';
    var STYLE = 'https://tiles.openfreemap.org/styles/positron';
    /* The two state names sit in room the towns leave, each inside its own state */
    var STATES = [['New Hampshire', -71.15, 42.85], ['Massachusetts', -71.4, 42.612]];
    /* Tints of the site's own slate and cream, so the map belongs to the page */
    var LAND = '#F1E9E5', GREEN = '#E3E2D8', WATER = '#B4BFCC', ROAD = '#FFFFFF', CASING = '#D6D0CC', TEXT = '#4A5263', SLATE = '#343D4E';

    function tint(style, towns) {
      var names = towns.map(function (t) { return t.name; });
      var noise = /^(label_other|label_village|airport|aeroway|railway|highway-name-path|highway-name-minor|road_area_pier|road_pier|highway_path)/;
      style.layers = style.layers.filter(function (l) { return !noise.test(l.id); });
      style.layers.forEach(function (l) {
        var p = l.paint = l.paint || {};
        if (l.id === 'background') { p['background-color'] = LAND; }
        else if (/^(park|landcover_wood)$/.test(l.id)) { p['fill-color'] = GREEN; }
        else if (l.id === 'landuse_residential') { p['fill-color'] = '#ECE3DE'; }
        else if (l.id === 'water') { p['fill-color'] = WATER; }
        else if (l.id === 'waterway') { p['line-color'] = WATER; }
        else if (l.id === 'building') { p['fill-color'] = '#E6DDD8'; p['fill-outline-color'] = '#DBD1CC'; }
        else if (/casing/.test(l.id) && l.type === 'line') { p['line-color'] = CASING; }
        else if (/^highway_/.test(l.id) && l.type === 'line') { p['line-color'] = ROAD; }
        else if (l.id === 'boundary_3') {
          /* the state line, not the county lines: it's what the page is talking about */
          p['line-color'] = ['case', ['==', ['get', 'admin_level'], 4], SLATE, 'rgba(0,0,0,0)'];
          p['line-width'] = 1.5;
          p['line-dasharray'] = [3, 2];
        } else if (l.type === 'symbol' && l.layout && l.layout['text-field']) {
          p['text-color'] = TEXT;
          p['text-halo-color'] = LAND;
          /* our towns get a pin and a name of their own */
          if (/^label_(town|city)/.test(l.id)) { l.filter = ['all', l.filter, ['!', ['in', ['get', 'name:latin'], ['literal', names]]]]; }
        }
      });
      return style;
    }

    function failed(slot) { slot.classList.add('is-failed'); }

    function draw(slot) {
      var towns = $$('[data-map-town]', slot).map(function (a) {
        return { name: a.textContent, slug: a.getAttribute('data-map-town'), href: a.getAttribute('href'), side: a.getAttribute('data-side'), lat: parseFloat(a.getAttribute('data-lat')), lon: parseFloat(a.getAttribute('data-lon')) };
      });
      window.fetch(STYLE).then(function (r) {
        if (!r.ok) { throw new Error('map style'); }
        return r.json();
      }).then(function (style) {
        var gl = window.maplibregl;
        var bounds = new gl.LngLatBounds();
        towns.forEach(function (t) { bounds.extend([t.lon, t.lat]); });
        var map = new gl.Map({ container: slot, style: tint(style, towns), bounds: bounds, fitBoundsOptions: { padding: 60 }, minZoom: 6, maxZoom: 15, attributionControl: { compact: false }, cooperativeGestures: true, dragRotate: false, pitchWithRotate: false, touchPitch: false, fadeDuration: reduced ? 0 : 300 });
        map.touchZoomRotate.disableRotation();
        map.keyboard.disableRotation();
        map.addControl(new gl.NavigationControl({ showCompass: false }), 'top-right');

        /* Frame the towns in whatever room the slot has: on Contact, the room beside the card. A visitor's own pan or zoom is left alone after that */
        var moved = false;
        var band = slot.closest('.o-contactMap');
        var card = band && $('.o-contactMap__card', band);
        function frame() {
          if (moved) { return; }
          var box = slot.getBoundingClientRect();
          var side = Math.max(44, Math.min(96, box.width * .14));
          var left = side;
          if (card) {
            var c = card.getBoundingClientRect();
            if (c.bottom > box.top + 1 && c.right > box.left) { left = c.right - box.left + 56; }
          }
          map.fitBounds(bounds, { padding: { top: 44, bottom: 44, left: left, right: side }, animate: false });
        }
        frame();
        map.on('resize', frame);
        ['dragstart', 'zoomstart'].forEach(function (name) {
          map.on(name, function (e) { if (e.originalEvent || e.isZoomControl) { moved = true; } });
        });
        $$('.maplibregl-ctrl-group button', slot).forEach(function (b) { b.addEventListener('click', function () { moved = true; }); });

        towns.forEach(function (t) {
          var pin = document.createElement('a');
          pin.className = 'm-map__place' + (t.side === 'left' ? ' -left' : t.side === 'top' ? ' -top' : '');
          pin.href = t.href;
          pin.tabIndex = -1;   /* the same towns are real links in the page's list; a dozen more tab stops would only slow the keyboard */
          pin.setAttribute('data-place', t.slug);
          pin.innerHTML = '<span class="m-map__dot"></span><span class="m-map__town"></span>';
          pin.lastChild.textContent = t.name;
          wire(pin);
          new gl.Marker({ element: pin }).setLngLat([t.lon, t.lat]).addTo(map);
          pin.setAttribute('aria-label', t.name);   /* after addTo: the library writes its own "Map marker" over it */
        });
        STATES.forEach(function (s) {
          var tag = document.createElement('span');
          tag.className = 'm-map__state';
          tag.textContent = s[0];
          new gl.Marker({ element: tag }).setLngLat([s[1], s[2]]).addTo(map);
          tag.removeAttribute('aria-label');
          tag.setAttribute('aria-hidden', 'true');
        });

        var ready = false;
        map.once('load', function () { ready = true; slot.classList.add('is-ready'); });
        map.on('error', function () { if (!ready) { map.remove(); failed(slot); ready = true; } });
      }).catch(function () { failed(slot); });
    }

    /* Only pages with a map pay for the library, and only once someone is near it */
    function loadLib(done, fail) {
      if (window.maplibregl) { done(); return; }
      var css = document.createElement('link');
      css.rel = 'stylesheet';
      css.href = LIB_CSS;
      css.integrity = LIB_CSS_SRI;
      css.crossOrigin = 'anonymous';
      document.head.appendChild(css);
      var js = document.createElement('script');
      js.src = LIB_JS;
      js.integrity = LIB_JS_SRI;
      js.crossOrigin = 'anonymous';
      js.onload = done;
      js.onerror = fail;
      document.head.appendChild(js);
    }

    function start() {
      loadLib(function () {
        slots.forEach(function (slot) {
          try { draw(slot); } catch (e) { failed(slot); }
        });
      }, function () { slots.forEach(failed); });
    }
    if (!window.fetch || !('IntersectionObserver' in window)) { slots.forEach(failed); return; }
    var near = new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) {
        near.disconnect();
        start();
      }
    }, { rootMargin: '800px 0px' });
    slots.forEach(function (slot) { near.observe(slot); });
  })();
}());
