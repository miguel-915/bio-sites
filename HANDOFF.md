# Travel Sergeant / Vuela con Rueda websites: handoff brief

Updated Nov 2, 2026. Owner: Miguel Rueda (travelsergeant@gmail.com).

## What exists

Two brands, each with a main homepage and a link-in-bio site. Everything is static HTML with no build step, in one GitHub repo, hosted on Cloudflare Pages.

| Site | Language | Repo folder | Cloudflare Pages project | Status |
|---|---|---|---|---|
| travelsergeant.com | English | `home-en/` | `ts-home` (ts-home.pages.dev) | New design live on preview. Domain still points to the old Carrd site |
| vuelaconrueda.com | Spanish | `home-es/` | `vcr-home` (vcr-home.pages.dev) | New design live on preview. Domain still points to the old Carrd site |
| bio.travelsergeant.com | English | `en/` | `ts-bio` (ts-bio-7ge.pages.dev) | Live |
| bio.vuelaconrueda.com | Spanish | `es/` | `vcr-bio` (vcr-bio.pages.dev) | Live |

## Where it lives

- **Code:** GitHub repo `miguel-915/bio-sites` (private), branch `main`. Every push to `main` redeploys all four Cloudflare projects in about a minute.
- **Cloudflare:** account travelsergeant@gmail.com. The Cloudflare GitHub app only has access to `bio-sites`. Each project has no build command; the build output directory is the folder in the table above.
- **DNS:**
  - GoDaddy (travelsergeant.com): `bio` CNAME points to ts-bio-7ge.pages.dev. The root domain still points to Carrd.
  - Porkbun (vuelaconrueda.com): `bio` CNAME points to vcr-bio.pages.dev. The root domain still points to Carrd.
- **Unused:** Cloudflare projects `travelsergeant-bio` and `vuelaconrueda-bio` (old manual uploads). Safe to delete.

## Main homepages (new, Nov 2)

- **Source of truth:** `scripts/build_home.py`. All copy for both languages lives in the `EN` and `ES` dictionaries at the top. Edit there, run `python3 scripts/build_home.py` from the repo root, then commit and push. Don't hand-edit `home-en/index.html` or `home-es/index.html`; the script overwrites them.
- **Sections, in order:** menu bar with language switch, hero (headline, 2 buttons, stats, photo), first-class photo gallery, "Ways I can help" cards, free guide signup, testimonials, award booking band ($250), 1 on 1 call ($99), card referrals, bootcamp waitlist, free tools, footer.
- **Photos:** `assets/home-hero.jpg` and `assets/home-g1.jpg` to `home-g3.jpg`, copied in from `en/assets/` by the script. Logos: `home-en/assets/logo-white.png`, `home-es/assets/logo.png`.
- **Email forms (Kit):** plain forms that post to `https://app.kit.com/forms/<ID>/subscriptions` and show a confirmation message on the page.
  - EN free guide: 10003006
  - EN bootcamp waitlist: 10002621
  - ES free guide: 10003026
  - ES bootcamp waitlist: 9928000
  - Not yet tested with a real signup. Submit one test email per form and confirm it shows up in Kit.
- **Calendly:** EN https://calendly.com/travelsergeant/45-min-call-sub, ES https://calendly.com/travelsergeant/asesoria
- **To go live:**
  1. In Cloudflare, open `ts-home` → Custom domains → add `travelsergeant.com` (and `www.travelsergeant.com`). Follow the DNS records Cloudflare shows and set them in GoDaddy, replacing the Carrd records.
  2. Do the same for `vcr-home` with `vuelaconrueda.com` (and `www`) in Porkbun.
  3. Check both domains load the new pages, then cancel Carrd.

## Bio sites pages

| English (bio.travelsergeant.com) | Spanish (bio.vuelaconrueda.com) |
|---|---|
| `/` bio page | `/` bio page |
| `/tools/` | `/herramientas/` |
| `/flight-deals/` | `/ofertas-de-vuelos/` |
| `/award-deals/` | `/sweet-spots/` |
| `/points-planner/` | `/planificador/` |
| `/award-booking/` | `/reserva-con-millas/` (menu label "Reserva con puntos") |
| `/gear/` | `/equipaje/` |
| `/privacy/`, `/terms/` | `/privacidad/`, `/terminos/` |

- **Bio page sections:** free guide, free tools, learn with me (award booking, bootcamp waitlist, $99 consult), card referrals.
- **Card referrals:** Chase Sapphire Preferred and Capital One Venture X only.

## Brand

- **Fonts (all pages):** Montserrat (headlines, italic 800 for emphasis), IBM Plex Sans (body), IBM Plex Mono (small labels).
- **Travel Sergeant colors:** dress blue #0A1F33, brass #C9A227, scarlet #C8102E, light background #FBFAF6.
- **Vuela con Rueda colors:** agave #0C3B3C, cempasúchil #F0A824, terracota #C7502B, crema #FAF3E7.
- **Shared numbers:** $500K+ travel booked with points, 10M+ points earned, 52 countries visited.

## Rules Miguel has set

- **No WhatsApp** anywhere: no channels, groups or mentions.
- **No "35 cards" stat**, and no sign-off lines ("Dismissed…" / "¡A volar!").
- **Seats.aero and Rakuten** belong on the tools pages only, never in the card referrals section.
- **Award booking** is Miguel's own service, written in first person ("I"). Never name the booking partner.
- **Language switch** at the top of every page: "Español" on English pages, "English" on Spanish pages. On booking pages it links to the other language's booking page.
- **Copy:** no AI-sounding phrases (for example "no fluff"). Keep Miguel's own wording where it exists.
- **Bootcamp:** 35 video lessons, about 4 hours. Use 35 everywhere, not "30+".

## Affiliate and referral links

- **Chase Sapphire Preferred:** https://www.referyourchasecard.com/19y/UJ0IO0Q1M1
- **Capital One Venture X:** https://i.capitalone.com/GLAjZTPzF
- **Seats.aero (CJ):** https://www.anrdoezrs.net/click-100842706-17075279
- **Roame:** https://roame.travel/?via=miguel. Code MIGUEL gives 10% off the first payment. Last-touch attribution, 30-day window. Not allowed on Reddit or coupon sites.
- **Rakuten:** https://www.rakuten.com/r/MIGUEL13110?eeid=28187 (5,000 Amex points or $50)
- **Rove:** https://www.rove.com/?signup&referralCode=651YT78S (1,500 miles)
- **Find Flights for Me:** https://rekomi.link/njjbr8x5kgwc?p=7a2ec388-fd3d-4e21-ad5e-d8d8e58b0655
- **Straight to the Points:** https://straighttothepoints.co/r/?aid=26337353
- **Savewise:** code MIGUEL saves 20%. **Thrifty Traveler:** code MIGUEL gets $20 off the first year.

## Daily automation

A cloud scheduled task, "Daily deals pages update", runs at 6:05am Mountain every day and auto-publishes. Miguel's computer doesn't need to be on. It edits only four files:

- **`en/award-deals` and `es/sweet-spots`:** refreshes the `const D` award data from seats.aero. Business class only, 90k miles or less one way, under $500 in taxes, 10 results per region and direction.
- **`en/flight-deals` and `es/ofertas-de-vuelos`:** rebuilds teaser tickets from the last 7 days of Going, Thrifty Traveler and Find Flights for Me alert emails in Gmail. Never shows departure cities or exact dates.

It then commits, pushes, checks the live pages and sends a push notification. Don't restructure those four files without updating the task.

Not automated: the tools pages, gear pages, points planner (flight data snapshot from Oct 29, 2026) and the homepages.

## Award booking service

- **Pricing:**
  - $250 per person, flat, one way or roundtrip.
  - $100 deposit per person to start. Nonrefundable, counts toward the fee.
  - $150 balance charged only when flights are booked.
  - If matching flights are found and the client declines, the full fee is due.
  - Client pays airline taxes and fees at booking.
- **Search:** daily checks for up to 90 days. For trips further out, the 90-day window is set closer to the trip.
- **Help levels (same price):** book it yourself (exact flights plus step-by-step list), follow my video (personal click-by-click video), book it together (live screen share, client logs in). Passwords are never requested.
- **Process:** client submits the form → Miguel reviews and confirms → client pays the $100 per person deposit → search starts, options within a few days → if nothing good yet, the request goes on the daily tracker.
- **Intake form:** posts to a Google Apps Script web app:
  https://script.google.com/macros/s/AKfycbx0UzvQVyX1l5tcYzBXR52W_2CmLIvEOmHjrGi7VDn65Qe0zTKuPXYOM4Eu-Glj3jyL_A/exec
  - Adds a row to the Google Sheet "Award Booking Requests" (ID `1L-cGL2h9nzuvoXgIWSC_IVOrjpsLKANELPBBIqrOqEw`) with Status "New", and emails travelsergeant@gmail.com.
  - Help level and book-by deadline go in the Notes column. A hidden "website" field catches spam.
  - Reference copy of the script: `scripts/award-booking-intake.gs`. If you add or rename form fields, keep the form, the script's `FIELDS` map and the sheet headers in sync.

## Open items

1. Point travelsergeant.com and vuelaconrueda.com at the new homepages (steps above), then cancel Carrd.
2. Test each Kit form with a real email.
3. Delete the "TEST - Claude" row in the booking sheet.
4. Create a Stripe payment link for the $100 per person deposit, and optionally one for the $150 balance. Stripe is connected; nothing created yet.
5. Optionally delete the two old Cloudflare projects.
