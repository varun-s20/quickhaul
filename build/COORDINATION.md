# Parallel rebuild: who writes what (set by the Studio Lead, 2026-11-05, Varun's rule)

Two developer sessions work at once. They never write the same file.

## Owners
- Shared-parts owner (the homepage session, log: logs/build-home-v2.log): everything shared. That means design/tokens.css, site/assets/global.css, global.js, fonts, the truck set and block art, site/src/partials/*, site/data/*, site/tools/*, the sitemap, build/progress.md, content/placeholders.md, review-log.md, and src/pages/index.body.html.
- Pages session (log: logs/build-pages-v2-*.log): only the page files of the pages it builds, and only in the staging folder site/src/pages-v2/ until the move-in step. Its own notes go to build/progress-pages-v2.md, new placeholders to content/placeholders-add-pages.md, review-log lines to logs/review-pages-v2.md.

## Queue for shared changes
A pages session never edits a shared file. If a page needs something shared (a new block, a CSS rule, a partial change, a data field, a new truck art), it writes one file build/requests/NNN-<page>.md: what is needed, why, exact change, and which OTHER pages it would touch. The shared-parts owner (later the integrator) applies requests one at a time, in number order, and after each one reruns the checks on every affected page and notes the result at the bottom of the request file. A request is closed only when its affected pages still pass.

## Gates
1. Phase P1 (now): the pages session only writes page bodies, page.json and schema sources into site/src/pages-v2/ from content/copy.md and the pattern in design/revision.md and prototype/revision/. No building, no browser, no QA, no edits outside its own files. Needs the shared parts only as reading: where a block does not exist yet, it uses the prototype's markup and files a request.
2. Phase P2 (starts only when the homepage session has finished and said the shared parts are frozen): move the staged pages into src/pages/ one batch at a time, run tools/build.py, QA, Critic per page. Only one session builds at a time.
3. Integration review: a final developer run at the highest effort applies open requests, runs tools/check.py and build.py --check on the whole site, QA on every page, then the Critic scores the whole site. Anything that broke another page is fixed there, not left.

## Ports and logs
Preview ports: homepage session 8820, pages session 8841, integrator 8850. Never kill another session's server.
