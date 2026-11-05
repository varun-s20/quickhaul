# Handover: Quick Haul, art direction phase B (2026-11-03)
Prototype: prototype/index.html (navigation, hero and the work-order strip under it). Spec: design/design-spec.md. Tokens: design/tokens.css (pasted into the first :root block of prototype/assets/global.css). Placeholders: content/placeholders.md.

This run picked up an earlier phase B run that was cut off during Critic round 1. That run's spec, tokens, placeholders and prototype were checked against the skill and kept. Its unfinished Critic round left screenshots (prototype/shots/critic-r1/) but no report, so round 1 was run again from the start.

## Critic's last scores (round 2 of 2)
| | Design | Originality | Craft | Functionality | Weighted | Verdict |
|---|---|---|---|---|---|---|
| Round 1 | 8 | 8 | 7 | 8 | 7.8 | FAIL |
| Round 2 | 7.5 | 8 | 7 | 8 | 7.6 | FAIL |

- Both rounds: no copy tells, no design tells, no overlaps. Originality reached the target of 8, and text was readable everywhere it measured (lowest: headline 9.62:1, lede 7.38:1, labels 6.91:1).
- Round 2 scored design lower than round 1 because it tested more widths (1366x768, 1024x768). The strip lost its price and Book now below the fold at common laptop sizes.
- Round 2's fixes below were checked by me in the browser, not by the Critic. The skill stops at 2 rounds, so there is no score after them.
- Critic shots: prototype/shots/critic-r1b/ (round 1), prototype/shots/critic-r2/ (round 2). My check shots: prototype/shots/proto-r0b-*, proto-r1fix-*, proto-r2fix-*.

## What I fixed
Before round 1 (found in the cut-off run's shots):
- From 1025 to 1300px the headline ran into the truck drawing. The copy column is now capped at half the viewport.
- The strip was cramped at 1100 (truncated town hint, chips crowding, call line wrapping).
- On phones the four load chips overflowed at 360. The glyph now sits above the label.

After round 1:
- **Phone action bar.** It is now driven by scroll position, so it hides again after a jump back to the top. It shows once the strip's buttons pass under the header, not 88px late.
- **Phone header.** On phones the top bar scrolls away and only the header sticks: fixed chrome is 117px, down from 149. A 1px shadow covers the seam above the sticky bars.
- **Header Book now.** It has a fixed width on desktop, so its hover no longer pushes the call circle. V9's breathing now happens as a wider gap between label and arrow inside the pill. All header pills are 44px.
- **Menu.** The panel is opaque and wipes down instead of fading, so the hero no longer shows through. The links rise in after it lands. The client's mark replaces the text title.
- **Load chips.** 1/8 starts checked, so the chip, the "$149 for a 1/8 truck" line and the truck fill agree on load.
- **Town field.** The browser's datalist popup is replaced by a styled listbox in the ticket's ruling. It works as a combobox: arrow keys, Enter, Escape and click.
- **Gauge.** Labels are larger (about 14px at 1440, 11px at 1100). The cramped 1/8 label is dropped (the chip names it). Below 1025 the whole gauge hides, not just its labels.
- **Truck drawing.** Strokes went from mid chrome (2.95:1) to chrome at 75% (4.93:1), so the drawing holds its half of the hero.

After round 2 (not re-scored):
- **Strip layout.** The strip is one row of five cells at every desktop width, tightened between 1025 and 1366. It ends at y 731 at 1366x768 and y 749 at 1100x800, so price and Book now are on the first screen.
- **No more jumps.** The town helper keeps two lines reserved, so picking a town no longer moves the strip.
- **Unlisted towns.** A town that is not on the list gets "Not on our list? Call (603) 555-0142" while it is being typed. Before, it fell back to "We cover...", which read as yes.
- **Logo.** It is clipped to a hard circle at the badge edge, so the phone screenshot's wall no longer shows as a pasted tile. It now fills the header cell: 56px at desktop, 50px on phones.
- **Intro order.** The load heap fades in with the truck body, no longer before it.
- **Alignment at 768.** Labels now line up across a row. The button and call link are grouped. The level line starts at the bed edge, so there is no orphan dash at tablet and phone.
- **Wraps.** The lede and helper lines are balanced (no "a call." or "Hampshire" alone on a line), and "1/8 truck" stays together. The headline is capped at 96px on tablet; it was larger at 1024 than at 1440. The town hint is in the light weight so it doesn't read as a typed value.
- **Header Book now on phones.** After round 1, I hid it on phones whenever the action bar shows. Round 2 found that left the header lopsided, and the brief says the sticky header keeps Book Now visible, so I put it back (decision 4).

## What is left
- **1024x768 (iPad landscape).** It still gets the tablet layout: stacked hero, with the strip starting below the fold. Book now is always in the header. A side-by-side hero at 1024 would need the desktop breakpoint moved below the conventions' 1025.
- **Desktop nav.** It has five links. Service area, FAQ and Contact are only in the phone menu, so the footer must carry them when it is built. A sixth link does not fit beside the logo cell at 1100.
- **Logo sharpness.** The logo is a crop of a phone screenshot of a wall mockup. It is sharp at 56px on 2x screens but cannot go larger, and the favicon and footer glyph are blocked until Shawn sends the original file.
- **Fonts.** Roboto Mono still loads from Google Fonts in the prototype; the site build must self-host it as woff2. Bio Sans is served as .otf (no fontTools install). The licence is your decision, recorded in choices.md.
- **Preview label.** Nothing on the page says "design preview with placeholder content" yet (only the meta description does). The brief requires that label before anything goes to Shawn.
- **Leftover files.** Playwright left snapshot logs in projects/quickhaul/.playwright-mcp/ and the studio root .playwright-mcp/. The cut-off run's prototype/shots/critic-r1/ is still there. None of it is published. Delete it when you like.

## What I could not check
- No real phone or touch device. All phone widths ran in desktop Chromium at 1x, so I could not see iOS safe areas or how sharp the logo is on a 2x screen.
- No Safari or Firefox.
- The town listbox was not tested with a screen reader. Its keyboard behaviour was tested with scripted key events only.
- No Critic round after the round 2 fixes, so the scores above are from before them.
- Truewerk using Roboto Mono comes from references/deconstruct/truewerk.md, not checked again live.

## Decisions for Varun
1. **Palette boldness.** Both rounds called the slate, chrome and cream palette near-monochrome: "bold" comes from the type alone. Keep it as picked (palette 1), or allow one stronger accent drawn from the logo for a single role, such as the price figure or the stripe?
2. **Bio Sans delivery.** Approve fontTools (a package install) to convert the .otf files to woff2 for the site build, or ship .otf. Also confirm the web licence before launch.
3. **Media gaps.** Until Shawn sends photos: hairline item drawings in the service cells and no before-and-after section (spec 2c), or leave those cells empty?
4. **Book now twice on phones.** Once a visitor scrolls past the strip, Book now shows in the sticky header and in the bottom action bar. Keep both (the brief asks for it in the header), or make the bottom bar call-only?
5. **Original logo file.** Ask Shawn for the 2.6 MB PNG from Fiverr, or a vector. The mark is capped at about 56px tall, and the favicon and footer glyph need the real file.
