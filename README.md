# bio-sites

Static pages for the two bio sites, each deployed by its own Cloudflare Pages project.

- `en/` → bio.travelsergeant.com (home, tools, flight-deals, award-deals, points-planner, gear)
- `es/` → bio.vuelaconrueda.com (inicio, herramientas, ofertas-de-vuelos, sweet-spots, equipaje)

No build step: each Cloudflare project serves its folder as-is.

## Main homepages

- `home-en/` → travelsergeant.com (Cloudflare Pages project `ts-home`)
- `home-es/` → vuelaconrueda.com (Cloudflare Pages project `vcr-home`)

Built from `scripts/build_home.py` (all copy for both languages lives in that file). Edit there, run
`python3 scripts/build_home.py` from the repo root, and push. Email forms post to Kit:
EN guide 10003006, EN waitlist 10002621, ES guide 10003026, ES waitlist 9928000.
