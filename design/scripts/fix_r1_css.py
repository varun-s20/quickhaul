"""One-off: apply the critic round 1 CSS fixes to prototype/assets/global.css (art director, phase B)."""
import sys

p = sys.argv[1]
s = open(p, encoding='utf-8').read()


def rep(old, new):
    global s
    if old not in s:
        raise SystemExit('not found: ' + old[:70])
    s = s.replace(old, new, 1)


# 5. seam above sticky bars; phones let the top bar scroll away
rep('.m-topbar { position: sticky; top: 0; z-index: 60; display: flex;',
    '.m-topbar { position: relative; z-index: 60; display: flex;')
rep('.m-topbar__line { margin: 0; white-space: nowrap; }',
    '/* Phones: the top bar scrolls away and only the header sticks, so fixed chrome stays near 56px plus the action bar\n'
    '   (critic r1: 149 of 844px with all three). The 1px shadow covers the seam a fractional scroll leaves above a sticky bar. */\n'
    '.m-topbar__line { margin: 0; white-space: nowrap; }')
rep('.m-header { position: sticky; top: var(--h-bar); z-index: 50;',
    '.m-header { position: sticky; top: 0; z-index: 50;')
rep('border-bottom: 1px solid var(--c-rule); background: var(--c-slate); color: var(--c-cream); }\n.m-header__left',
    'border-bottom: 1px solid var(--c-rule); background: var(--c-slate); box-shadow: 0 -1px 0 var(--c-slate); color: var(--c-cream); }\n.m-header__left')

# 3 and 9. header Book now
rep('''.m-header__book { min-height: 4rem; padding: 0 1.6rem; }
.m-header__book .a-button__arrow { display: none; }
@media (hover: hover) and (any-pointer: fine) and (prefers-reduced-motion: no-preference) {
  .m-header__book:hover { padding: 0 2rem; }
}''',
'''/* All three header pieces are 44px. On desktop the pill keeps a fixed width so its hover never pushes the call
   circle (critic r1); V9's breathing happens inside the box as a wider gap between label and arrow. */
.m-header__book { min-height: var(--h-button); padding: 0 1.6rem; transition: opacity var(--d-ui) var(--e-ui), visibility 0s, background-color var(--d-ui) var(--e-ui), transform var(--d-ui) var(--e-ui); }
.m-header__book .a-button__arrow { display: none; }
/* phones: while the action bar shows, its Book now is the one on screen, so the header's steps aside */
@media (max-width: 640px) {
  .is-barShown .m-header__book { opacity: 0; visibility: hidden; transition: opacity var(--d-ui) var(--e-ui), visibility 0s linear var(--d-ui); }
}''')
rep('  .m-header__book { min-height: var(--h-button); padding: 0 2.2rem; }',
    '  .m-header__book { width: 15.6rem; padding: 0; transition: gap var(--d-breathe) var(--e-out), background-color var(--d-ui) var(--e-ui), transform var(--d-ui) var(--e-ui); }')
rep('''@media (min-width: 1025px) and (hover: hover) and (any-pointer: fine) and (prefers-reduced-motion: no-preference) {
  .m-header__book:hover { padding: 0 3rem; }
}''',
'''@media (min-width: 1025px) and (hover: hover) and (any-pointer: fine) and (prefers-reduced-motion: no-preference) {
  .m-header__book:hover { gap: 1.6rem; padding: 0; }
}''')

# 4. menu wipe
rep('''.m-menu { position: fixed; inset: 0; z-index: 200; background: var(--c-scrim); opacity: 0; transition: opacity var(--d-menu) var(--e-out); }
.m-menu.is-open { opacity: 1; }
.m-menu__panel { position: absolute; inset: .8rem; display: flex; flex-direction: column; overflow-y: auto; padding: var(--s-4) var(--s-5) var(--s-6); background: var(--c-cream); color: var(--c-ink); transform: translateY(-1.6rem); transition: transform var(--d-menu) var(--e-out); --c-focus: var(--c-ink); overscroll-behavior: contain; }
.m-menu.is-open .m-menu__panel { transform: none; }''',
'''/* The panel is always opaque and wipes down from the top (a clip, not a fade), so the hero never shows through
   the links (critic r1). The links rise in once it has mostly landed. */
.m-menu { position: fixed; inset: 0; z-index: 200; background: rgba(15, 20, 28, 0); transition: background-color var(--d-menu) var(--e-out); }
.m-menu.is-open { background: var(--c-scrim); }
.m-menu__panel { position: absolute; inset: .8rem; display: flex; flex-direction: column; overflow-y: auto; padding: var(--s-4) var(--s-5) var(--s-6); background: var(--c-cream); color: var(--c-ink); clip-path: inset(0 0 100% 0); transition: clip-path var(--d-menu) var(--e-out); --c-focus: var(--c-ink); overscroll-behavior: contain; }
.m-menu.is-open .m-menu__panel { clip-path: inset(0 0 0 0); }
.m-menu__item, .m-menu__actions, .m-menu__hours { opacity: 0; transform: translateY(.8rem); transition: opacity var(--d-rise) var(--e-out), transform var(--d-rise) var(--e-out); }
.m-menu.is-open .m-menu__item, .m-menu.is-open .m-menu__actions, .m-menu.is-open .m-menu__hours { opacity: 1; transform: none; transition-delay: calc(220ms + var(--i, 0) * 35ms); }
.m-menu__item:nth-child(2) { --i: 1; }
.m-menu__item:nth-child(3) { --i: 2; }
.m-menu__item:nth-child(4) { --i: 3; }
.m-menu__item:nth-child(5) { --i: 4; }
.m-menu__item:nth-child(6) { --i: 5; }
.m-menu__item:nth-child(7) { --i: 6; }
.m-menu__item:nth-child(8) { --i: 7; }
.m-menu__actions { --i: 8; }
.m-menu__hours { --i: 9; }''')
rep('.m-menu__title { font: var(--w-label) var(--t-label)/1 var(--f-mono); letter-spacing: var(--tr-label); text-transform: uppercase; color: var(--c-steel); }',
    '/* the real mark in its own slate cell, the header logo cell at phone size, in place of a text title */\n'
    '.m-menu__logo { width: 6.4rem; height: 5.6rem; border: 0; background: var(--c-slate); --mark: 4.6rem; --c-focus: var(--c-ink); }')

# 7. town listbox
rep('.o-homeTicket__town::-webkit-calendar-picker-indicator { display: none; }   /* the datalist arrow; suggestions still open as you type */\n', '')
rep('.o-homeTicket__note { min-height',
'''/* town suggestions: our own listbox in the ticket's ruling, replacing the browser's datalist popup (critic r1) */
.o-homeTicket__combo { position: relative; }
.o-homeTicket__options { position: absolute; top: 100%; left: 0; right: 0; z-index: 20; max-height: 26.4rem; overflow-y: auto; border: 1px solid var(--c-slate); border-top: 0; background: var(--c-cream); overscroll-behavior: contain; }
.o-homeTicket__option { display: flex; align-items: center; min-height: 4.4rem; padding: 0 var(--s-4); border-bottom: 1px solid var(--c-ruleLight); color: var(--c-ink); font: var(--w-semi) 1.5rem/1 var(--f-display); text-transform: uppercase; letter-spacing: .02em; cursor: pointer; transition: background-color var(--d-ui) var(--e-ui); }
.o-homeTicket__option:last-child { border-bottom: 0; }
.o-homeTicket__option[aria-selected="true"] { background: var(--c-slate); color: var(--c-cream); }
@media (hover: hover) and (any-pointer: fine) {
  .o-homeTicket__option:hover { background: rgba(52, 61, 78, .08); }
  .o-homeTicket__option[aria-selected="true"]:hover { background: var(--c-slate); }
}
.o-homeTicket__note { min-height''')

# 8. gauge
rep('.m-truck__gauge { font: var(--w-label) 13px/1 var(--f-mono); letter-spacing: .06em; fill: var(--c-chrome); }',
    '/* 17 SVG units: about 14px at 1440 (drawing 600 wide) and 11px at 1100 (462 wide), never under the 11px label size */\n'
    '.m-truck__gauge { font: var(--w-label) 17px/1 var(--f-mono); letter-spacing: .04em; fill: var(--c-chrome); }')
rep('.m-truck__gauge { display: none; }\n',
    '.m-truck__gaugeSet { display: none; }   /* below 1025 the labels would be under 9px, so the whole gauge goes with them */\n')
rep('  .m-truck__gauge { display: inline; }', '  .m-truck__gaugeSet { display: inline; }')

# from 641 both bars stick together
rep('  .m-topbar { justify-content: space-between; }',
    '  .m-topbar { position: sticky; top: 0; justify-content: space-between; box-shadow: 0 -1px 0 var(--c-ink); }\n'
    '  .m-header { top: var(--h-bar); }')

# reduced motion
rep('  .m-truck__load, .m-menu, .m-menu__panel, .m-actionBar, .m-actionBar.is-shown { transition: none; }',
    '  .m-truck__load, .m-menu, .m-menu__panel, .m-actionBar, .m-actionBar.is-shown, .m-header__book, .o-homeTicket__option { transition: none; }\n'
    '  .m-menu__item, .m-menu__actions, .m-menu__hours, .m-menu.is-open .m-menu__item, .m-menu.is-open .m-menu__actions, .m-menu.is-open .m-menu__hours { opacity: 1; transform: none; transition: none; }')

open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
