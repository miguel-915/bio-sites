"""Builds the main homepages (travelsergeant.com, vuelaconrueda.com) into home-en/ and home-es/.
Run from the repo root: python3 scripts/build_home.py
"""
import os, shutil, html

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMMON = {
    "chase": "https://www.referyourchasecard.com/19y/UJ0IO0Q1M1",
    "c1": "https://i.capitalone.com/GLAjZTPzF",
}

EN = dict(
    lang="en", dir="home-en", bio="https://bio.travelsergeant.com",
    title="Travel Sergeant | Travel more for less with points and miles",
    desc="I'm Miguel. I teach everyday people how to fly business and first class and stay in five star hotels using credit card points.",
    canonical="https://travelsergeant.com/", alt_lang="es", alt_url="https://vuelaconrueda.com/", alt_label="Español",
    logo="assets/logo-white.png", logo_h=46, ig="https://www.instagram.com/travelsergeant/", ig_handle="@travelsergeant",
    colors=dict(blue="#0A1F33", brass="#C9A227", accent="#C8102E", bg="#FBFAF6", line="#E3DED2", chip="#EFEBE1", muted="#56606B",
                dbg="#07131F", dsurface="#0D1C2C", dink="#EDE9DF", dmuted="#A3ACB6", dline="#1E3247", dchip="#17293D", heroink="#F4F1EA", herosub="#C9CFD6"),
    nav=[("#guide", "Free guide"), ("#booking", "Award booking"), ("#call", "1 on 1 call"), ("#course", "Course"), ("{bio}/tools/", "Tools")],
    eyebrow="Travel more for less",
    h1="Turn credit card points into <em>first class</em> travel.",
    lede="I'm Miguel. I've earned and redeemed millions of points for $500,000 in travel. I teach everyday people how to fly business and first class, stay in five star hotels, and never pay full price again.",
    cta1=("#guide", "Get the free guide"), cta2=("#booking", "Have points? I'll book it"),
    stats=[("$500K+", "travel booked with points"), ("10M+", "points earned"), ("52", "countries visited")],
    photo_alt="Miguel, Travel Sergeant",
    gallery_h="This is what points buy.",
    gallery_sub="Every one of these seats was booked with miles, not cash.",
    gallery_alts=["Etihad First Apartment", "First class suite", "First class suite with bed"],
    help_k="Ways I can help", help_h="Pick where you are right now.",
    help=[
        ("Free", "Points & Miles 101", "A 10 page guide to the basics: how to earn points, how to redeem them, and which cards to start with.", "#guide", "Send me the guide"),
        ("$250 / person", "Award booking, done for you", "You bring the points. I find the seats, send you the exact flights, and help you book them.", "#booking", "See how it works"),
        ("$99", "1 on 1 strategy call", "45 minutes on video. We map out which cards to open, how to earn, and how to book the trip you want.", "#call", "Book my call"),
        ("Coming soon", "Points and Miles Bootcamp", "My A to Z course. 35 video lessons from zero travel cards to booking business class.", "#course", "Join the waitlist"),
    ],
    guide_k="Free guide", guide_h="Points & Miles 101",
    guide_p="A free 10 page guide to the basics: how to earn points, how to redeem them for the most value, and which cards to start with. Enter your email and I'll send it over.",
    guide_form="10003006", guide_btn="Send me the guide", email_ph="Email address", name_ph=None,
    form_ok="Check your inbox. It's on the way.", form_err="That didn't go through. Try again in a minute.",
    quotes_h="What people are saying",
    quotes=[("I relate to u so much. I too am Mexican and sometimes feel wow, I can't believe I'm traveling like this!", "Rosie"),
            ("Next year doing 1st class on JAL. You inspired me.", "Caren"),
            ("I trust your advice more than anyone.", "Keneisha"),
            ("This trip was inspired by your solo travel videos.", "Rafael")],
    book_k="Award booking", book_h="You have the points. I'll find the seats.",
    book_p="Tell me where you want to go and what points you have. I search every day, send you the exact flights, and walk you through booking them yourself, by video, or live on a screen share.",
    book_list=["$250 per person, one way or roundtrip", "$100 deposit to start, counts toward the fee", "Daily search for up to 90 days", "I never ask for your passwords"],
    book_cta=("{bio}/award-booking/", "Start my request"),
    call_k="1 on 1 consultation", call_h="Get a personal game plan for your travel goals.",
    call_p="45 minutes with me on video. We'll map out exactly which cards to open, how to earn, and how to book the trip you actually want: honeymoon, family vacation, bucket list adventure.",
    call_list=["Personalized card strategy based on your spending", "Points earning plan for the next 12 months", "Redemption walkthrough for your dream trip", "Q and A: bring every question you have"],
    call_price="$99", call_unit="45 minutes", call_cta=("https://calendly.com/travelsergeant/45-min-call-sub", "Book my call"),
    cards_k="Card referrals", cards_h="The cards I actually carry.",
    cards_p="These are the cards in my wallet right now. Using my referral links costs you nothing and supports everything I create.",
    cards=[("Chase Sapphire Preferred", "The best starter premium travel card", COMMON["chase"]),
           ("Capital One Venture X", "Simple, powerful, great value", COMMON["c1"])],
    cards_note="Referral links may earn me bonus points at no cost to you. I only recommend cards I use myself.",
    course_k="Coming soon", course_h="Points and Miles Bootcamp",
    course_p="My complete A to Z course, taking you from zero travel cards to booking business class with points. The exact system I use.",
    course_list=["35 video lessons, about 4 hours total", "Which cards to get and in what order", "How to find award availability and book sweet spots", "Real booking walkthroughs, start to finish"],
    course_form="10002621", course_btn="Join the waitlist", course_small="Join the waitlist for launch updates and early bird pricing.",
    tools_k="Free tools", tools_h="Use what I use.",
    tools=[("{bio}/award-deals/", "Award deals", "Business class seats open right now, by region."),
           ("{bio}/flight-deals/", "Flight deals", "The best cash fares from the alerts I follow."),
           ("{bio}/points-planner/", "Points planner", "Pick your card and balance and see what you could book."),
           ("{bio}/tools/", "My tool kit", "The search tools and alerts I use for every trip.")],
    foot_tag="Travel more for less using points and miles.",
    foot_links=[("{bio}/", "All links"), ("{bio}/privacy/", "Privacy"), ("{bio}/terms/", "Terms")],
    disclosure="Some links on this site are referral or affiliate links. If you use them, I may earn a commission or bonus points at no extra cost to you. Content is for educational purposes. Credit card decisions are yours. Always read the terms.",
    copy="© 2026 Travel Sergeant. All rights reserved.",
)

ES = dict(
    lang="es", dir="home-es", bio="https://bio.vuelaconrueda.com",
    title="Vuela con Rueda | Viaja más por menos con puntos y millas",
    desc="Soy Miguel. Enseño a gente como tú a volar en business y primera clase y quedarse en hoteles de lujo usando puntos de tarjetas.",
    canonical="https://vuelaconrueda.com/", alt_lang="en", alt_url="https://travelsergeant.com/", alt_label="English",
    logo="assets/logo.png", logo_h=52, ig="https://www.instagram.com/vuelaconrueda/", ig_handle="@vuelaconrueda",
    colors=dict(blue="#0C3B3C", brass="#F0A824", accent="#C7502B", bg="#FAF3E7", line="#E8DCC6", chip="#F2E6D2", muted="#4E5F5E",
                dbg="#062323", dsurface="#0B2E2E", dink="#F3EADB", dmuted="#A9BDB9", dline="#1D4747", dchip="#173B3B", heroink="#FAF3E7", herosub="#CFDCD8"),
    nav=[("#guia", "Guía gratis"), ("#reserva", "Reserva con puntos"), ("#asesoria", "Asesoría"), ("#curso", "Curso"), ("{bio}/herramientas/", "Herramientas")],
    eyebrow="Viaja más por menos",
    h1="Convierte puntos de tarjetas en viajes de <em>primera clase</em>.",
    lede="Soy Miguel. He ganado y usado millones de puntos en $500,000 en viajes. Enseño a gente como tú a volar en business y primera clase, quedarse en hoteles de lujo y no volver a pagar precio completo.",
    cta1=("#guia", "Descarga la guía gratis"), cta2=("#reserva", "¿Tienes puntos? Yo te lo reservo"),
    stats=[("$500K+", "en viajes canjeados"), ("10M+", "puntos ganados"), ("52", "países visitados")],
    photo_alt="Miguel, Vuela con Rueda",
    gallery_h="Esto es lo que compran los puntos.",
    gallery_sub="Cada uno de estos asientos se reservó con millas, no con dinero.",
    gallery_alts=["Etihad First Apartment", "Suite de primera clase", "Suite de primera clase con cama"],
    help_k="Cómo te ayudo", help_h="Empieza donde estás hoy.",
    help=[
        ("Gratis", "Puntos y Millas 101", "Una guía de 10 páginas con lo básico: cómo ganar puntos, cómo canjearlos y con qué tarjetas empezar.", "#guia", "Quiero la guía"),
        ("$250 / persona", "Reserva con puntos, hecha para ti", "Tú pones los puntos. Yo encuentro los asientos, te mando los vuelos exactos y te ayudo a reservarlos.", "#reserva", "Ver cómo funciona"),
        ("$99", "Asesoría 1 a 1", "45 minutos por video. Armamos qué tarjetas abrir, cómo generar puntos y cómo reservar el viaje que quieres.", "#asesoria", "Agendar mi llamada"),
        ("Próximamente", "Bootcamp de Puntos y Millas", "Mi curso de la A a la Z. 35 lecciones en video, de cero tarjetas a volar en business.", "#curso", "Anotarme"),
    ],
    guide_k="Guía gratis", guide_h="Puntos y Millas 101",
    guide_p="Una guía gratis de 10 páginas con lo básico: cómo ganar puntos, cómo canjearlos por el mayor valor y con qué tarjetas empezar. Deja tu correo y te la envío.",
    guide_form="10003026", guide_btn="Quiero la guía", email_ph="Tu correo", name_ph=None,
    form_ok="Revisa tu correo. Ya va en camino.", form_err="No se pudo enviar. Intenta de nuevo en un minuto.",
    quotes_h="Lo que dice la gente",
    quotes=[("Siguiendo tus consejos acumule en algunos meses 90k en millas de AA.", "Junior"),
            ("Como decía mi abuelita, vales un millón. Muchas gracias por las ideas.", "Rafael"),
            ("Gracias por compartir tus tips. La verdad ayudan un buen.", "Grissel"),
            ("Una inspiración para muchos incluyéndome a mi. Quisiera aprender más.", "Lalo")],
    book_k="Reserva con puntos", book_h="Tú tienes los puntos. Yo encuentro los asientos.",
    book_p="Dime a dónde quieres ir y qué puntos tienes. Busco todos los días, te mando los vuelos exactos y te guío para reservarlos tú, con un video o en vivo compartiendo pantalla.",
    book_list=["$250 por persona, solo ida o viaje redondo", "Depósito de $100 para empezar, se aplica al total", "Búsqueda diaria hasta por 90 días", "Nunca te pido tus contraseñas"],
    book_cta=("{bio}/reserva-con-millas/", "Empezar mi solicitud"),
    call_k="Asesoría 1 a 1", call_h="Un plan de juego personal para tus metas de viaje.",
    call_p="45 minutos conmigo por video. Armamos exactamente qué tarjetas abrir, cómo generar puntos y cómo reservar el viaje que quieres: luna de miel, vacaciones en familia, el viaje de tus sueños.",
    call_list=["Estrategia de tarjetas personalizada según tus gastos", "Plan para generar puntos en los próximos 12 meses", "Cómo canjear puntos para tu viaje soñado, paso a paso", "Preguntas y respuestas: trae todas tus dudas"],
    call_price="$99 USD", call_unit="45 minutos", call_cta=("https://calendly.com/travelsergeant/asesoria", "Agendar mi llamada"),
    cards_k="Tarjetas recomendadas", cards_h="Las tarjetas que sí uso.",
    cards_p="Estas son las tarjetas que traigo en mi cartera hoy. Usar mis enlaces de referido no te cuesta nada y apoya todo lo que creo.",
    cards=[("Chase Sapphire Preferred", "La mejor tarjeta premium para empezar", COMMON["chase"]),
           ("Capital One Venture X", "Simple, poderosa, gran valor", COMMON["c1"])],
    cards_note="Los enlaces de referido pueden darme puntos extra sin costo para ti. Solo recomiendo tarjetas que uso personalmente.",
    course_k="Próximamente", course_h="Bootcamp de Puntos y Millas",
    course_p="Mi curso completo de la A a la Z: de cero tarjetas a reservar en business class con puntos. El sistema exacto que yo uso.",
    course_list=["35 lecciones en video, unas 4 horas en total", "Qué tarjetas pedir y en qué orden", "Cómo encontrar disponibilidad y reservar sweet spots", "Reservas reales paso a paso, de principio a fin"],
    course_form="9928000", course_btn="Anotarme", course_small="Entérate primero cuando abra el curso, con un precio de lanzamiento que no se va a repetir.",
    tools_k="Herramientas gratis", tools_h="Usa lo que yo uso.",
    tools=[("{bio}/sweet-spots/", "Sweet spots", "Asientos en business disponibles hoy, por región."),
           ("{bio}/ofertas-de-vuelos/", "Ofertas de vuelos", "Las mejores tarifas en efectivo de las alertas que sigo."),
           ("{bio}/planificador/", "Planificador de puntos", "Elige tu tarjeta y tu saldo y mira qué podrías reservar."),
           ("{bio}/herramientas/", "Mis herramientas", "Los buscadores y alertas que uso en cada viaje.")],
    foot_tag="Viaja más por menos usando puntos y millas.",
    foot_links=[("{bio}/", "Todos los enlaces"), ("{bio}/privacidad/", "Privacidad"), ("{bio}/terminos/", "Términos")],
    disclosure="Algunos enlaces en este sitio son de referido o de afiliado. Si los usas, puedo ganar una comisión o puntos extra sin costo para ti. Contenido con fines educativos. Las decisiones de tarjetas son tuyas. Siempre lee los términos.",
    copy="© 2026 Vuela con Rueda. Todos los derechos reservados.",
)

CHECK = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def u(s, c):
    return s.replace("{bio}", c["bio"])


def ext(href):
    return ' target="_blank" rel="noopener"' if href.startswith("http") else ""


def kit_form(fid, btn, c, idx):
    return f'''<form class="kit" action="https://app.kit.com/forms/{fid}/subscriptions" method="post" data-kit>
          <label class="sr" for="email{idx}">{c["email_ph"]}</label>
          <input id="email{idx}" type="email" name="email_address" placeholder="{c["email_ph"]}" required autocomplete="email">
          <button type="submit" class="btn btn-brass">{btn}</button>
          <p class="form-msg" role="status" aria-live="polite"></p>
        </form>'''


def page(c):
    k = c["colors"]
    li = lambda items: "".join(f"<li>{CHECK}<span>{html.escape(x)}</span></li>" for x in items)
    nav = "".join(f'<a href="{u(h, c)}">{t}</a>' for h, t in c["nav"])
    stats = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in c["stats"])
    help_cards = "".join(
        f'''<a class="help" href="{h}"><span class="tag">{tag}</span><h3>{t}</h3><p>{p}</p><span class="more">{cta} {ARROW}</span></a>'''
        for tag, t, p, h, cta in c["help"])
    gal = "".join(f'<figure><img src="assets/home-g{i+1}.jpg" alt="{a}" loading="lazy" width="640" height="{481 if i == 0 else 856}"></figure>'
                  for i, a in enumerate(c["gallery_alts"]))
    quotes = "".join(f'<blockquote><p>“{html.escape(q)}”</p><cite>{n}</cite></blockquote>' for q, n in c["quotes"])
    cards = "".join(f'''<a class="card" href="{h}" target="_blank" rel="noopener sponsored"><span><b>{t}</b><small>{d}</small></span>{ARROW}</a>'''
                    for t, d, h in c["cards"])
    tools = "".join(f'<a class="tool" href="{u(h, c)}"><b>{t}</b><span>{d}</span></a>' for h, t, d in c["tools"])
    foot = "".join(f'<a href="{u(h, c)}">{t}</a>' for h, t in c["foot_links"])
    ids = dict(en=("guide", "booking", "call", "course"), es=("guia", "reserva", "asesoria", "curso"))[c["lang"]]

    return f'''<!doctype html>
<html lang="{c["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{c["title"]}</title>
<meta name="description" content="{c["desc"]}">
<link rel="canonical" href="{c["canonical"]}">
<link rel="alternate" hreflang="{c["lang"]}" href="{c["canonical"]}">
<link rel="alternate" hreflang="{c["alt_lang"]}" href="{c["alt_url"]}">
<meta property="og:title" content="{c["title"]}">
<meta property="og:description" content="{c["desc"]}">
<meta property="og:url" content="{c["canonical"]}">
<meta property="og:image" content="{c["canonical"]}assets/home-g1.jpg">
<meta name="theme-color" content="{k["blue"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;0,700;0,800;1,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
:root {{
  --blue: {k["blue"]}; --brass: {k["brass"]}; --accent: {k["accent"]};
  --bg: {k["bg"]}; --surface: #FFFFFF; --ink: {k["blue"]}; --muted: {k["muted"]}; --line: {k["line"]}; --chip: {k["chip"]};
  --hero-ink: {k["heroink"]}; --hero-sub: {k["herosub"]};
  --display: "Montserrat", "Avenir Next", "Segoe UI", sans-serif;
  --body: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
  color-scheme: light;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: {k["dbg"]}; --surface: {k["dsurface"]}; --ink: {k["dink"]}; --muted: {k["dmuted"]}; --line: {k["dline"]}; --chip: {k["dchip"]}; color-scheme: dark; }} }}
:root[data-theme="dark"] {{ --bg: {k["dbg"]}; --surface: {k["dsurface"]}; --ink: {k["dink"]}; --muted: {k["dmuted"]}; --line: {k["dline"]}; --chip: {k["dchip"]}; color-scheme: dark; }}

* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 76px; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font: 400 17px/1.6 var(--body); -webkit-font-smoothing: antialiased; }}
img {{ max-width: 100%; display: block; }}
a {{ color: inherit; }}
a:focus-visible, button:focus-visible, input:focus-visible {{ outline: 3px solid var(--brass); outline-offset: 2px; }}
.sr {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }}
.kicker {{ font: 700 12px/1 var(--display); letter-spacing: .16em; text-transform: uppercase; color: var(--brass); margin: 0 0 14px; }}
h1, h2, h3 {{ font-family: var(--display); margin: 0; text-wrap: balance; }}
h2 {{ font-weight: 800; font-size: clamp(28px, 4vw, 42px); line-height: 1.1; letter-spacing: -.01em; }}
section {{ padding-block: clamp(56px, 8vw, 96px); }}

.btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 52px; padding: 0 24px; border-radius: 6px; border: 0;
  font: 700 15px/1 var(--display); letter-spacing: .02em; text-decoration: none; cursor: pointer; transition: transform .15s, background .15s; }}
.btn svg {{ width: 18px; height: 18px; }}
.btn:hover {{ transform: translateY(-1px); }}
.btn-brass {{ background: var(--brass); color: #10202A; }}
.btn-ghost {{ background: transparent; color: var(--hero-ink); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.4); }}
.btn-ghost:hover {{ box-shadow: inset 0 0 0 1.5px var(--brass); }}

/* masthead */
.mast {{ position: sticky; top: 0; z-index: 20; background: color-mix(in srgb, var(--blue) 94%, transparent); backdrop-filter: blur(8px); color: var(--hero-ink); border-bottom: 1px solid rgba(255,255,255,.08); }}
.mast .wrap {{ display: flex; align-items: center; gap: 24px; min-height: 68px; }}
.mast .logo {{ height: {c["logo_h"]}px; width: auto; }}
.mast nav {{ display: flex; gap: 22px; margin-left: auto; font: 600 13px/1 var(--display); letter-spacing: .05em; text-transform: uppercase; }}
.mast nav a {{ text-decoration: none; opacity: .82; }}
.mast nav a:hover {{ opacity: 1; color: var(--brass); }}
.lang {{ font: 700 12px/1 var(--display); letter-spacing: .08em; text-transform: uppercase; text-decoration: none; padding: 9px 12px; border-radius: 999px; box-shadow: inset 0 0 0 1.5px var(--brass); color: var(--brass); white-space: nowrap; }}
@media (max-width: 900px) {{ .mast nav {{ display: none; }} .lang {{ margin-left: auto; }} }}

/* hero */
.hero {{ background: var(--blue); color: var(--hero-ink); padding-block: clamp(40px, 7vw, 88px) 0; overflow: hidden; position: relative; }}
.hero::before {{ content: ""; position: absolute; inset: 0; background: radial-gradient(60% 80% at 85% 20%, color-mix(in srgb, var(--brass) 18%, transparent), transparent 70%); pointer-events: none; }}
.hero .wrap {{ display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, .9fr); gap: clamp(32px, 6vw, 72px); align-items: end; position: relative; }}
.hero h1 {{ font-weight: 800; font-size: clamp(38px, 6.4vw, 72px); line-height: 1.02; letter-spacing: -.02em; margin-bottom: 22px; }}
.hero h1 em {{ font-style: italic; color: var(--brass); }}
.hero .lede {{ font-size: clamp(17px, 1.8vw, 19px); color: var(--hero-sub); max-width: 56ch; margin: 0 0 30px; }}
.ctas {{ display: flex; gap: 12px; flex-wrap: wrap; }}
.stats {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 44px; padding: 22px 0 clamp(40px, 6vw, 72px); border-top: 1px solid rgba(255,255,255,.14); max-width: 560px; }}
.stats b {{ display: block; font: 800 clamp(26px, 3.4vw, 36px)/1 var(--display); color: var(--hero-ink); }}
.stats span {{ display: block; margin-top: 6px; font-size: 13px; color: var(--hero-sub); line-height: 1.35; }}
.portrait {{ position: relative; align-self: end; }}
.portrait img {{ width: 100%; height: auto; aspect-ratio: 4 / 5; object-fit: cover; object-position: center 20%; border-radius: 10px 10px 0 0; }}
.portrait::after {{ content: ""; position: absolute; left: -14px; top: 14px; right: 14px; bottom: 0; border: 2px solid var(--brass); border-bottom: 0; border-radius: 12px 12px 0 0; z-index: -1; }}
.portrait figcaption {{ position: absolute; left: 16px; bottom: 16px; background: var(--blue); color: var(--hero-ink); font: 600 13px/1 var(--display); padding: 10px 12px; border-radius: 6px; display: flex; gap: 8px; align-items: center; }}
.portrait figcaption a {{ text-decoration: none; color: var(--brass); }}
@media (max-width: 820px) {{
  .hero .wrap {{ grid-template-columns: 1fr; }}
  .portrait {{ order: -1; max-width: 260px; }}
  .portrait img {{ border-radius: 10px; aspect-ratio: 4 / 4.4; }}
  .portrait::after {{ bottom: -14px; border-bottom: 2px solid var(--brass); border-radius: 12px; }}
  .stats {{ margin-top: 32px; }}
}}

/* proof gallery */
.proof {{ padding-top: clamp(40px, 6vw, 72px); }}
.proof-head {{ display: flex; justify-content: space-between; align-items: end; gap: 20px; flex-wrap: wrap; margin-bottom: 24px; }}
.proof-head p {{ margin: 0; color: var(--muted); max-width: 40ch; }}
.gallery {{ display: grid; grid-template-columns: 1.35fr 1fr 1fr; gap: 12px; }}
.gallery figure {{ margin: 0; border-radius: 8px; overflow: hidden; background: var(--chip); }}
.gallery img {{ width: 100%; height: auto; aspect-ratio: 4 / 5; object-fit: cover; }}
.gallery figure:first-child img {{ object-position: 70% center; }}
@media (max-width: 700px) {{ .gallery {{ grid-template-columns: 1fr 1fr; }} .gallery figure:first-child {{ grid-column: 1 / -1; }} .gallery figure:first-child img {{ aspect-ratio: 4 / 3; }} }}

/* help cards */
.helps {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin-top: 32px; }}
@media (max-width: 980px) {{ .helps {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
@media (max-width: 560px) {{ .helps {{ grid-template-columns: 1fr; }} }}
.help {{ display: flex; flex-direction: column; gap: 10px; padding: 22px; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; text-decoration: none; transition: border-color .15s, transform .15s; }}
.help:hover {{ border-color: var(--brass); transform: translateY(-2px); }}
.help .tag {{ align-self: flex-start; font: 500 12px/1 var(--mono); padding: 6px 8px; border-radius: 4px; background: var(--chip); color: var(--ink); }}
.help h3 {{ font-weight: 800; font-size: 20px; line-height: 1.2; }}
.help p {{ margin: 0; color: var(--muted); font-size: 15px; flex: 1; }}
.help .more {{ display: inline-flex; align-items: center; gap: 6px; font: 700 14px/1 var(--display); color: var(--ink); }}
.help .more svg {{ width: 16px; height: 16px; color: var(--brass); transition: transform .15s; }}
.help:hover .more svg {{ transform: translateX(3px); }}

/* split blocks */
.split {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: clamp(28px, 6vw, 72px); align-items: center; }}
@media (max-width: 820px) {{ .split {{ grid-template-columns: 1fr; }} }}
.split p.body {{ color: var(--muted); margin: 16px 0 0; max-width: 58ch; }}
.checks {{ list-style: none; padding: 0; margin: 22px 0 0; display: grid; gap: 12px; }}
.checks li {{ display: grid; grid-template-columns: 22px 1fr; gap: 10px; align-items: start; }}
.checks svg {{ width: 20px; height: 20px; color: var(--brass); margin-top: 3px; }}

.panel {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: clamp(22px, 4vw, 34px); }}
.kit {{ display: grid; gap: 10px; }}
.kit input {{ min-height: 52px; padding: 0 16px; border-radius: 6px; border: 1.5px solid var(--line); background: var(--bg); color: var(--ink); font: 400 16px var(--body); }}
.kit input:focus {{ border-color: var(--brass); outline: none; }}
.form-msg {{ margin: 0; min-height: 1.2em; font-size: 14px; color: var(--muted); }}
.form-msg.ok {{ color: var(--ink); font-weight: 600; }}
.fine {{ font-size: 13px; color: var(--muted); margin: 12px 0 0; }}

.guide-cover {{ aspect-ratio: 4 / 5; max-width: 340px; border-radius: 6px; padding: 28px; background: var(--blue); color: var(--hero-ink); display: flex; flex-direction: column; justify-content: space-between;
  box-shadow: 18px 18px 0 var(--brass); margin-inline: auto; }}
.guide-cover small {{ font: 500 12px/1 var(--mono); color: var(--brass); letter-spacing: .08em; }}
.guide-cover b {{ font: italic 800 40px/1 var(--display); }}
.guide-cover span {{ font-size: 14px; color: var(--hero-sub); }}

/* quotes */
.quotes {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin-top: 28px; }}
@media (max-width: 980px) {{ .quotes {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
@media (max-width: 560px) {{ .quotes {{ grid-template-columns: 1fr; }} }}
blockquote {{ margin: 0; padding: 22px; border-radius: 8px; background: var(--chip); display: flex; flex-direction: column; justify-content: space-between; gap: 14px; }}
blockquote p {{ margin: 0; font-size: 16px; }}
cite {{ font: 700 13px/1 var(--display); font-style: normal; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }}

/* booking band */
.band {{ background: var(--blue); color: var(--hero-ink); }}
.band p.body {{ color: var(--hero-sub); }}
.band .checks li {{ color: var(--hero-ink); }}
.price-tag {{ border: 1.5px solid color-mix(in srgb, var(--brass) 60%, transparent); border-radius: 10px; padding: clamp(22px, 4vw, 34px); background: rgba(255,255,255,.04); }}
.price-tag .big {{ font: 800 clamp(48px, 7vw, 72px)/1 var(--display); }}
.price-tag .big small {{ font-size: 18px; font-weight: 600; color: var(--hero-sub); margin-left: 6px; }}

.price {{ display: flex; align-items: baseline; gap: 10px; margin: 26px 0 18px; }}
.price b {{ font: 800 44px/1 var(--display); }}
.price span {{ color: var(--muted); }}

/* cards */
.card-list {{ display: grid; gap: 12px; margin-top: 8px; }}
.card {{ display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: 18px 20px; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; text-decoration: none; transition: border-color .15s; }}
.card:hover {{ border-color: var(--brass); }}
.card b {{ display: block; font: 800 18px/1.2 var(--display); }}
.card small {{ display: block; color: var(--muted); font-size: 14px; margin-top: 4px; }}
.card svg {{ width: 20px; height: 20px; flex: none; color: var(--brass); }}

/* tools */
.tools-row {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 8px; overflow: hidden; margin-top: 28px; }}
@media (max-width: 860px) {{ .tools-row {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
@media (max-width: 480px) {{ .tools-row {{ grid-template-columns: 1fr; }} }}
.tool {{ background: var(--surface); padding: 20px; text-decoration: none; display: grid; gap: 6px; }}
.tool:hover b {{ color: var(--accent); }}
.tool b {{ font: 800 17px/1.2 var(--display); }}
.tool span {{ font-size: 14px; color: var(--muted); }}

.alt {{ background: var(--chip); }}
footer {{ background: var(--blue); color: var(--hero-sub); padding-block: 48px 36px; font-size: 14px; }}
footer .top {{ display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap; padding-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,.12); }}
footer .logo {{ height: {c["logo_h"]}px; width: auto; }}
footer nav {{ display: flex; gap: 18px; flex-wrap: wrap; }}
footer nav a {{ text-decoration: none; color: var(--hero-ink); }}
footer nav a:hover {{ color: var(--brass); }}
footer p {{ margin: 16px 0 0; max-width: 80ch; }}
</style>
</head>
<body>
<header class="mast">
  <div class="wrap">
    <a href="#top" aria-label="{c["title"].split(" |")[0]}"><img class="logo" src="{c["logo"]}" alt="{c["title"].split(" |")[0]}"></a>
    <nav aria-label="Main">{nav}</nav>
    <a class="lang" href="{c["alt_url"]}" hreflang="{c["alt_lang"]}" lang="{c["alt_lang"]}">{c["alt_label"]}</a>
  </div>
</header>

<main id="top">
<section class="hero">
  <div class="wrap">
    <div>
      <p class="kicker">{c["eyebrow"]}</p>
      <h1>{c["h1"]}</h1>
      <p class="lede">{c["lede"]}</p>
      <div class="ctas">
        <a class="btn btn-brass" href="{c["cta1"][0]}">{c["cta1"][1]}</a>
        <a class="btn btn-ghost" href="{c["cta2"][0]}">{c["cta2"][1]} {ARROW}</a>
      </div>
      <div class="stats">{stats}</div>
    </div>
    <figure class="portrait">
      <img src="assets/home-hero.jpg" alt="{c["photo_alt"]}" width="482" height="777">
      <figcaption><a href="{c["ig"]}" target="_blank" rel="noopener">{c["ig_handle"]}</a></figcaption>
    </figure>
  </div>
</section>

<section class="proof">
  <div class="wrap">
    <div class="proof-head"><h2>{c["gallery_h"]}</h2><p>{c["gallery_sub"]}</p></div>
    <div class="gallery">{gal}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <p class="kicker">{c["help_k"]}</p>
    <h2>{c["help_h"]}</h2>
    <div class="helps">{help_cards}</div>
  </div>
</section>

<section class="alt" id="{ids[0]}">
  <div class="wrap split">
    <div class="guide-cover" aria-hidden="true"><small>{c["guide_k"].upper()}</small><b>{c["guide_h"]}</b><span>{c["title"].split(" |")[0]}</span></div>
    <div>
      <p class="kicker">{c["guide_k"]}</p>
      <h2>{c["guide_h"]}</h2>
      <p class="body">{c["guide_p"]}</p>
      <div style="margin-top:24px">{kit_form(c["guide_form"], c["guide_btn"], c, 1)}</div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{c["quotes_h"]}</h2>
    <div class="quotes">{quotes}</div>
  </div>
</section>

<section class="band" id="{ids[1]}">
  <div class="wrap split">
    <div>
      <p class="kicker">{c["book_k"]}</p>
      <h2>{c["book_h"]}</h2>
      <p class="body">{c["book_p"]}</p>
    </div>
    <div class="price-tag">
      <div class="big">$250<small>{"/ person" if c["lang"] == "en" else "/ persona"}</small></div>
      <ul class="checks">{li(c["book_list"])}</ul>
      <a class="btn btn-brass" style="margin-top:26px;width:100%" href="{u(c["book_cta"][0], c)}">{c["book_cta"][1]} {ARROW}</a>
    </div>
  </div>
</section>

<section id="{ids[2]}">
  <div class="wrap split">
    <div>
      <p class="kicker">{c["call_k"]}</p>
      <h2>{c["call_h"]}</h2>
      <p class="body">{c["call_p"]}</p>
    </div>
    <div class="panel">
      <ul class="checks" style="margin-top:0">{li(c["call_list"])}</ul>
      <div class="price"><b>{c["call_price"]}</b><span>/ {c["call_unit"]}</span></div>
      <a class="btn btn-brass" style="width:100%" href="{c["call_cta"][0]}" target="_blank" rel="noopener">{c["call_cta"][1]} {ARROW}</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div>
      <p class="kicker">{c["cards_k"]}</p>
      <h2>{c["cards_h"]}</h2>
      <p class="body">{c["cards_p"]}</p>
    </div>
    <div>
      <div class="card-list">{cards}</div>
      <p class="fine">{c["cards_note"]}</p>
    </div>
  </div>
</section>

<section id="{ids[3]}">
  <div class="wrap split">
    <div>
      <p class="kicker">{c["course_k"]}</p>
      <h2>{c["course_h"]}</h2>
      <p class="body">{c["course_p"]}</p>
      <ul class="checks">{li(c["course_list"])}</ul>
    </div>
    <div class="panel">
      <p style="margin:0 0 16px">{c["course_small"]}</p>
      {kit_form(c["course_form"], c["course_btn"], c, 2)}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="kicker">{c["tools_k"]}</p>
    <h2>{c["tools_h"]}</h2>
    <div class="tools-row">{tools}</div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div class="top">
      <img class="logo" src="{c["logo"]}" alt="">
      <nav aria-label="Footer">{foot}<a href="{c["ig"]}" target="_blank" rel="noopener">Instagram</a><a href="{c["alt_url"]}" lang="{c["alt_lang"]}">{c["alt_label"]}</a></nav>
    </div>
    <p>{c["foot_tag"]}</p>
    <p>{c["disclosure"]}</p>
    <p>{c["copy"]}</p>
  </div>
</footer>

<script>
document.querySelectorAll('form[data-kit]').forEach(f => f.addEventListener('submit', async e => {{
  e.preventDefault();
  const msg = f.querySelector('.form-msg'), btn = f.querySelector('button');
  btn.disabled = true;
  try {{
    await fetch(f.action, {{ method: 'POST', mode: 'no-cors', body: new URLSearchParams(new FormData(f)) }});
    msg.textContent = {c["form_ok"]!r}; msg.className = 'form-msg ok'; f.reset();
  }} catch (err) {{
    msg.textContent = {c["form_err"]!r}; msg.className = 'form-msg'; btn.disabled = false;
  }}
}}));
</script>
</body>
</html>
'''


for c in (EN, ES):
    d = os.path.join(R, c["dir"])
    os.makedirs(os.path.join(d, "assets"), exist_ok=True)
    for f in ["home-hero.jpg", "home-g1.jpg", "home-g2.jpg", "home-g3.jpg"]:
        shutil.copy(os.path.join(R, "en/assets", f), os.path.join(d, "assets", f))
    src_logo = "en/assets/logo-white.png" if c["lang"] == "en" else "es/assets/logo.png"
    shutil.copy(os.path.join(R, src_logo), os.path.join(d, c["logo"]))
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(c))
    print("wrote", c["dir"])
