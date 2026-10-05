# -*- coding: utf-8 -*-
"""Genera las páginas de servicio y los casos, y actualiza menú, footer y sitemap.

Uso (desde la carpeta del sitio):  python tools/build.py

- Las páginas nuevas se arman a partir de reparacion-tv-no-enciende.html, así
  comparten el mismo head, formulario, mapa y scripts.
- El menú (navbar) y el footer se reescriben en TODAS las páginas .html.
- Se puede correr las veces que haga falta: el resultado es siempre el mismo.
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).parent))
from contenido import PAGES, EXISTING, MENU, RELATED_EXISTING  # noqa: E402
from casos import CASOS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://electronica-rem.com"
WA_NUMBER = "5491122556308"
TEMPLATE = ROOT / "reparacion-tv-no-enciende.html"
TEMPLATE_WA = "https://wa.me/5491122556308?text=Hola%2C%20mi%20TV%20no%20enciende.%20Quiero%20consultar%20por%20la%20reparaci%C3%B3n"
TODAY = date.today().isoformat()

CASOS_PUB = sorted([c for c in CASOS if c.get("publicado")], key=lambda c: c["fecha"], reverse=True)

PAGES_BY_SLUG = {p["slug"]: p for p in PAGES}


def t(s):
    """Escapa texto para HTML."""
    return html.escape(s, quote=False)


def a(s):
    """Escapa texto para atributos HTML."""
    return html.escape(s, quote=True)


def wa_url(text):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text, safe='')}"


def first_sentence(s):
    return s.split(". ")[0].rstrip(".") + "."


def info(slug):
    """(menú, título de tarjeta, descripción corta) de cualquier página del sitio."""
    if slug in PAGES_BY_SLUG:
        p = PAGES_BY_SLUG[slug]
        return p["nav"], p["crumb"], first_sentence(p["subtitle"])
    _, nav, title, desc = EXISTING[slug]
    return nav, title, desc


def json_ld(data, comment=None):
    body = json.dumps(data, ensure_ascii=False, indent=2)
    prefix = f"<!-- {comment} -->\n  " if comment else ""
    return f'{prefix}<script type="application/ld+json">\n{body}\n  </script>'


def breadcrumb_ld(items):
    return json_ld({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    })


def faq_ld(faqs):
    return json_ld({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}}
            for q, r in faqs
        ],
    }, "FAQ Schema")


# ------------------------------------------------------------------ bloques

def cards_html(cards):
    out = []
    for title, text, href in cards:
        if href:
            out.append(f'        <a href="{a(href)}" class="apple-card"><h3>{t(title)}</h3>\n'
                       f'          <p class="small">{t(text)}</p></a>')
        else:
            out.append(f'        <div class="apple-card"><h3>{t(title)}</h3>\n'
                       f'          <p class="small">{t(text)}</p></div>')
    return '      <div class="grid grid-3 problems-grid">\n' + "\n".join(out) + "\n      </div>"


def section_html(sec, light):
    cls = "section section-light fade-in-section" if light else "section fade-in-section"
    return f'''  <section class="{cls}">
    <div class="container">
      <h2 class="text-center mb-4">{t(sec["h2"])}</h2>
      <p class="text-center text-secondary mb-8">{t(sec["intro"])}</p>
{cards_html(sec["cards"])}
    </div>
  </section>'''


def hero_html(h1, subtitle, wa, crumbs=None):
    crumb_html = ""
    if crumbs:
        parts = []
        for name, href in crumbs:
            parts.append(f'<a href="{a(href)}">{t(name)}</a>' if href else f'<span aria-current="page">{t(name)}</span>')
        crumb_html = '      <nav class="breadcrumbs" aria-label="Ruta de navegación">' + ' <span class="sep">/</span> '.join(parts) + "</nav>\n"
    return f'''<header class="hero fade-in-section">
    <div class="container text-center">
{crumb_html}      <h1>{t(h1)}</h1>
      <p class="subtitle text-secondary">{t(subtitle)}</p>

      <div class="hero-cta">
        <a href="{a(wa)}" class="btn btn-primary" target="_blank">Contactar por WhatsApp</a>
        <a href="#diagnostico" class="btn btn-secondary">Solicitar diagnóstico</a>
      </div>
    </div>
  </header>'''


def cta_html(text, wa):
    return f'''  <section class="section fade-in-section">
    <div class="container text-center">
      <h2 class="mb-4">{t(text)}</h2>
      <div class="hero-cta">
        <a href="{a(wa)}" class="btn btn-primary" target="_blank">Consultar por WhatsApp</a>
        <a href="#diagnostico" class="btn btn-secondary">Solicitar diagnóstico</a>
      </div>
    </div>
  </section>'''


def related_html(slugs, heading="También te puede interesar"):
    cards = [(info(s)[1], info(s)[2], f"/{s}") for s in slugs]
    return section_html({"h2": heading, "intro": "Otras fallas y servicios relacionados.", "cards": cards}, True)


CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>'


def faq_section_html(faqs):
    items = []
    for q, r in faqs:
        items.append(f'''        <div class="faq-item">
          <button class="faq-question">
            <h3>{t(q)}</h3>
            <div class="faq-icon">
              {CHEVRON}
            </div>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-content">
              <p>{t(r)}</p>
            </div>
          </div>
        </div>''')
    return '''<!-- FAQ Section -->
  <section id="faq" class="section section-light fade-in-section">
    <div class="container">
      <h2 class="text-center">Preguntas frecuentes</h2>
      <p class="text-center text-secondary mb-8">Respuestas a las dudas más comunes antes de traer tu equipo.</p>
      <div class="faq-container">
''' + "\n".join(items) + '''
      </div>
    </div>
  </section>'''


BRANDS = {
    "tv": ("Reparamos todas las marcas", [
        ("Samsung", "Samsung-Logo.wine.svg"), ("LG", "LG_Electronics-Logo.wine.svg"), ("Sony", None),
        ("Philips", "Philips-Logo.wine.svg"), ("Panasonic", "Panasonic-Logo.wine.svg"), ("TCL", "TCL_Corporation-Logo.wine.svg"),
        ("Hisense", None), ("Noblex", None), ("JVC", "JVC-Logo.wine.svg"), ("Toshiba", "Toshiba-Logo.wine.svg"),
    ]),
    "monitor": ("Monitores de todas las marcas", [
        ("Samsung", "Samsung-Logo.wine.svg"), ("LG", "LG_Electronics-Logo.wine.svg"), ("Dell", "Dell-Logo.wine.svg"),
        ("BenQ", "BenQ-Logo.wine.svg"), ("Philips", "Philips-Logo.wine.svg"), ("NEC", "NEC-Logo.wine.svg"),
        ("AOC", None), ("ViewSonic", None),
    ]),
    "audio": ("Equipos de audio de todas las marcas", [
        ("Technics", "Technics_(brand)-Logo.wine.svg"), ("Pioneer", "Pioneer_Corporation-Logo.wine.svg"),
        ("Denon", "Denon-Logo.wine.svg"), ("Onkyo", "Onkyo-Logo.wine.svg"), ("JBL", "JBL-Logo.wine.svg"),
        ("Bose", "Bose_Corporation-Logo.wine.svg"), ("Sony", None), ("Audio-Technica", "Audio-Technica-Logo.wine.svg"),
    ]),
}


def brands_html(kind):
    heading, brands = BRANDS[kind]
    items = []
    for name, logo in brands:
        if logo:
            items.append(f'        <div class="brand-item"><img src="/assets/brands/{a(logo)}" alt="{a(name)}" width="120" height="60" loading="lazy"></div>')
        else:
            items.append(f'        <div class="brand-item" style="font-weight:bold; font-size:1.5rem; color:#555;">{t(name)}</div>')
    return f'''<!-- Brands Grid -->
  <section id="brands" class="section fade-in-section">
    <div class="container text-center">
      <h3 class="mb-4">{t(heading)}</h3>
      <div class="brands-grid">
''' + "\n".join(items) + '''
      </div>
    </div>
  </section>'''


# ------------------------------------------------------------ menú y footer

def nav_html(current, cta_inner):
    groups = []
    for label, items in MENU:
        links, active = [], False
        for item in items:
            slug, text = item if isinstance(item, tuple) else (item, info(item)[0])
            is_current = slug == current
            active = active or is_current
            cur = ' aria-current="page"' if is_current else ""
            links.append(f'            <a href="/{slug}"{cur}>{t(text)}</a>')
        cls = "nav-dropdown-toggle is-active" if active else "nav-dropdown-toggle"
        groups.append(f'''        <div class="nav-dropdown">
          <button type="button" class="{cls}" aria-expanded="false">{t(label)}{CHEVRON}</button>
          <div class="nav-dropdown-menu">
''' + "\n".join(links) + '''
          </div>
        </div>''')
    if CASOS_PUB:
        cur = ' aria-current="page" class="is-active"' if current and current.startswith("casos") else ""
        groups.append(f'        <a href="/casos"{cur}>Casos</a>')
    return f'''<nav class="navbar">
    <div class="container">
      <a href="/" class="navbar-brand">Electrónica REM</a>
      <div class="navbar-links" id="nav-menu">
''' + "\n".join(groups) + f'''
      </div>
      <div class="navbar-cta">
        {cta_inner}
        <button type="button" class="nav-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </nav>'''


def footer_html():
    def col(title, items):
        lis = "\n".join(f'            <li><a href="/{s}">{t(txt)}</a></li>' for s, txt in items)
        return f'''        <div class="footer-col">
          <h4>{t(title)}</h4>
          <ul>
{lis}
          </ul>
        </div>'''

    menu = dict(MENU)

    def items(group):
        return [(i if isinstance(i, tuple) else (i, info(i)[1])) for i in menu[group]]

    extra = [("casos", "Casos de reparación")] if CASOS_PUB else []
    return '''<footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>Electrónica REM</h4>
          <p class="small text-secondary">Expertos en diagnóstico y reparación de equipos electrónicos con más de 40 años de trayectoria.</p>
          <ul class="mt-4">
            <li>Av. Pres. Perón 1182</li>
            <li>Ramos Mejía, Provincia de Buenos Aires</li>
            <li><a href="tel:541146503333">011 4650-3333</a></li>
            <li><a href="https://wa.me/5491122556308" target="_blank">WhatsApp 11 2255-6308</a></li>
          </ul>
        </div>
''' + "\n".join([
        col("Servicios", items("Servicios") + extra),
        col("Fallas", items("Fallas")),
        col("Marcas", [(s, "TV " + info(s)[0]) for s in menu["Marcas"]]),
        col("Zonas", [(s, "Service TV " + txt) for s, txt in
                      (i if isinstance(i, tuple) else (i, info(i)[0]) for i in menu["Zonas"])]),
    ]) + '''
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Electrónica REM. Todos los derechos reservados.</p>
        <p>Expertos desde 1983.</p>
      </div>
    </div>
  </footer>'''


NAV_RE = re.compile(r'<nav class="navbar">.*?</nav>', re.S)
CTA_RE = re.compile(r'<div class="navbar-cta">(.*?)</div>', re.S)
TOGGLE_RE = re.compile(r'\s*<button type="button" class="nav-toggle".*?</button>', re.S)
FOOTER_RE = re.compile(r'<footer>.*?</footer>', re.S)


RELATED_RE = re.compile(r'  <!-- Related -->.*?<!-- /Related -->\n\n', re.S)
BRAND_IMG_RE = re.compile(r'(<div class="brand-item"><img )(?![^>]*loading=)')


def add_related(doc, slugs):
    """Agrega (o actualiza) el bloque de páginas relacionadas antes de las marcas."""
    doc = RELATED_RE.sub("", doc)
    block = f"  <!-- Related -->\n{related_html(slugs)}\n  <!-- /Related -->\n\n"
    return doc.replace("  <!-- Brands Grid -->", block + "  <!-- Brands Grid -->", 1)


def apply_chrome(doc, current):
    """Reemplaza navbar y footer, y agrega nav.js."""
    old_nav = NAV_RE.search(doc).group(0)
    cta = TOGGLE_RE.sub("", CTA_RE.search(old_nav).group(1)).strip()
    doc = doc.replace(old_nav, nav_html(current, cta), 1)
    doc = FOOTER_RE.sub(lambda m: footer_html(), doc, count=1)
    doc = BRAND_IMG_RE.sub(lambda m: m.group(1) + 'loading="lazy" decoding="async" ', doc)
    if "/nav.js" not in doc:
        doc = doc.replace("</body>", '  <script src="/nav.js" defer></script>\n</body>', 1)
    return doc


# --------------------------------------------------------------- páginas

def set_meta(doc, url, title, description, og_type="website"):
    sub = [
        (r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{a(description)}">'),
        (r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{a(url)}">'),
        (r'<title>.*?</title>', f'<title>{t(title)}</title>'),
        (r'<meta property="og:type" content="[^"]*">', f'<meta property="og:type" content="{og_type}">'),
        (r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{a(url)}">'),
        (r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{a(title)}">'),
        (r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{a(description)}">'),
        (r'<meta name="twitter:url" content="[^"]*">', f'<meta name="twitter:url" content="{a(url)}">'),
        (r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{a(title)}">'),
        (r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{a(description)}">'),
    ]
    for pattern, repl in sub:
        doc, n = re.subn(pattern, lambda m: repl, doc, count=1)
        assert n == 1, pattern
    return doc


BREADCRUMB_RE = re.compile(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "BreadcrumbList".*?</script>', re.S)
FAQ_LD_RE = re.compile(r'<!-- FAQ Schema -->\s*<script type="application/ld\+json">.*?</script>', re.S)
HERO_RE = re.compile(r'<header class="hero fade-in-section">.*?</header>', re.S)
BODY_RE = re.compile(r'(</header>\n).*?(\n  <!-- Brands Grid -->)', re.S)
BRANDS_RE = re.compile(r'<!-- Brands Grid -->.*?</section>', re.S)
FAQ_RE = re.compile(r'<!-- FAQ Section -->.*?</section>', re.S)


def build_from_template(tpl, *, url, title, description, crumbs, hero, body, wa,
                        faqs=None, brands="tv", extra_ld=None, og_type="website", device=None):
    doc = set_meta(tpl, url, title, description, og_type)
    doc = BREADCRUMB_RE.sub(lambda m: breadcrumb_ld(crumbs), doc, count=1)
    ld_tail = (faq_ld(faqs) if faqs else "") + (("\n  " if faqs else "") + extra_ld if extra_ld else "")
    doc = FAQ_LD_RE.sub(lambda m: ld_tail, doc, count=1)
    doc = HERO_RE.sub(lambda m: hero, doc, count=1)
    doc = BODY_RE.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), doc, count=1)
    doc = BRANDS_RE.sub(lambda m: brands_html(brands), doc, count=1)
    doc = FAQ_RE.sub(lambda m: faq_section_html(faqs) if faqs else "", doc, count=1)
    doc = doc.replace(TEMPLATE_WA, wa)
    if device:
        doc = doc.replace(f'<option value="{device}">', f'<option value="{device}" selected>', 1)
        doc = doc.replace('<option value="" disabled selected>', '<option value="" disabled>', 1)
    return doc


def build_page(tpl, p):
    url = f"{SITE}/{p['slug']}"
    wa = wa_url(p["wa_text"])
    sections = [section_html(s, i % 2 == 0) for i, s in enumerate(p["sections"])]
    body = "\n\n".join(sections + [cta_html(p["cta"], wa), related_html(p["related"])])
    hero = hero_html(p["h1"], p["subtitle"], wa)
    return build_from_template(
        tpl, url=url, title=p["title"], description=p["description"],
        crumbs=[("Inicio", f"{SITE}/"), (p["crumb"], url)],
        hero=hero, body=body, wa=wa, faqs=p["faqs"], brands=p["brands"], device=p.get("device"),
    )


def build_case(tpl, c):
    url = f"{SITE}/casos/{c['slug']}"
    wa = wa_url(f"Hola, vi el caso del {c['marca']} {c['modelo']} y quiero consultar por mi equipo")
    meta = [("Equipo", c["equipo"]), ("Marca", c["marca"]), ("Modelo", c["modelo"])]
    if c.get("zona"):
        meta.append(("Cliente de", c["zona"]))
    if c.get("tiempo"):
        meta.append(("Tiempo de reparación", c["tiempo"]))
    meta_html = "\n".join(f'          <div><dt>{t(k)}</dt><dd>{t(v)}</dd></div>' for k, v in meta)
    fotos = "\n".join(
        f'          <figure><img src="/{a(src)}" alt="{a(alt)}" loading="lazy"><figcaption>{t(alt)}</figcaption></figure>'
        for src, alt in c.get("fotos", [])
    )
    gallery = f'\n        <div class="case-gallery">\n{fotos}\n        </div>' if fotos else ""
    blocks = [("El problema", c["sintoma"]), ("Diagnóstico", c["diagnostico"]),
              ("Reparación", c["reparacion"]), ("Resultado", c["resultado"])]
    prose = "\n".join(f'        <h2>{t(h)}</h2>\n        <p>{t(txt)}</p>' for h, txt in blocks)
    body = f'''  <section class="section section-light fade-in-section">
    <div class="container">
      <article class="case-article">
        <dl class="case-meta">
{meta_html}
        </dl>{gallery}
{prose}
      </article>
    </div>
  </section>

{cta_html("¿Tu equipo tiene una falla parecida? Escribinos", wa)}

{related_html(c["servicios"], "Servicios relacionados")}'''
    fecha = date.fromisoformat(c["fecha"])
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre", "diciembre"]
    fecha_txt = f"{fecha.day} de {meses[fecha.month - 1]} de {fecha.year}"
    hero = hero_html(c["titulo"], c["resumen"], wa,
                     crumbs=[("Inicio", "/"), ("Casos", "/casos"), (f"{c['marca']} {c['modelo']}", None)])
    hero = hero.replace('<p class="subtitle', f'<p class="case-date"><time datetime="{c["fecha"]}">{fecha_txt}</time></p>\n      <p class="subtitle', 1)
    article_ld = json_ld({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": c["titulo"],
        "description": c["resumen"],
        "datePublished": c["fecha"],
        "dateModified": c["fecha"],
        "mainEntityOfPage": url,
        "image": [f"{SITE}/{src}" for src, _ in c.get("fotos", [])] or [f"{SITE}/og-image.jpg"],
        "author": {"@id": f"{SITE}/#negocio"},
        "publisher": {"@id": f"{SITE}/#negocio"},
        "about": {"@type": "Product", "name": f"{c['marca']} {c['modelo']}", "brand": {"@type": "Brand", "name": c["marca"]}},
    }, "Article Schema")
    return build_from_template(
        tpl, url=url, title=f"{c['titulo']} | Electrónica REM", description=c["resumen"],
        crumbs=[("Inicio", f"{SITE}/"), ("Casos de reparación", f"{SITE}/casos"), (c["titulo"], url)],
        hero=hero, body=body, wa=wa, extra_ld=article_ld, og_type="article",
    )


def build_casos_hub(tpl):
    url = f"{SITE}/casos"
    wa = wa_url("Hola, quiero consultar por la reparación de un equipo")
    cards = []
    for c in CASOS_PUB:
        img = ""
        if c.get("fotos"):
            src, alt = c["fotos"][0]
            img = f'<img src="/{a(src)}" alt="{a(alt)}" loading="lazy">'
        cards.append(f'''        <a href="/casos/{a(c["slug"])}" class="apple-card case-card">{img}
          <span class="small text-secondary">{t(c["equipo"])} · {t(c["marca"])} {t(c["modelo"])}</span>
          <h3>{t(c["titulo"])}</h3>
          <p class="small">{t(c["resumen"])}</p></a>''')
    body = f'''  <section class="section section-light fade-in-section">
    <div class="container">
      <div class="grid grid-3 problems-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>

{cta_html("¿Tu equipo tiene una falla? Escribinos", wa)}'''
    hero = hero_html("Casos de reparación",
                     "Equipos reales que pasaron por nuestro taller: qué les pasaba, qué encontramos y cómo los reparamos.", wa)
    return build_from_template(
        tpl, url=url, title="Casos de reparación de TV y electrónica | Electrónica REM",
        description="Casos reales de reparación de TV LED, Smart TV, monitores y equipos de audio en nuestro taller de Ramos Mejía: síntoma, diagnóstico y solución.",
        crumbs=[("Inicio", f"{SITE}/"), ("Casos de reparación", url)],
        hero=hero, body=body, wa=wa,
    )


def build_404(tpl):
    wa = wa_url("Hola, quiero consultar por la reparación de un equipo")
    cards = [(info(s)[1], info(s)[2], f"/{s}") for s in
             ["reparacion-tv-ramos-mejia", "reparacion-tv-no-enciende", "reparacion-tv-sin-imagen",
              "service-smart-tv", "reparacion-monitores", "reparacion-equipos-de-audio"]]
    body = section_html({"h2": "Quizás estabas buscando", "intro": "Nuestros servicios más consultados.", "cards": cards}, True)
    hero = hero_html("No encontramos esta página",
                     "Puede que la dirección haya cambiado. Volvé al inicio o escribinos por WhatsApp y te ayudamos.", wa)
    doc = build_from_template(
        tpl, url=f"{SITE}/404", title="Página no encontrada | Electrónica REM",
        description="La página que buscás no existe. Reparación de TV LED, Smart TV, monitores y audio en Ramos Mejía.",
        crumbs=[("Inicio", f"{SITE}/")], hero=hero, body=body, wa=wa,
    )
    doc = re.sub(r'\s*<link rel="canonical" href="[^"]*">', "", doc, count=1)
    return doc.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n  <meta name="viewport"', 1)


def write(path, doc):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8", newline="\n")


def build_sitemap(slugs):
    urls = [("", "1.0")]
    for s in slugs:
        if s.startswith("casos/"):
            urls.append((s, "0.6"))
        elif s == "casos":
            urls.append((s, "0.7"))
        else:
            urls.append((s, "0.8"))
    body = "\n".join(
        f"  <url>\n    <loc>{SITE}/{s}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{prio}</priority>\n  </url>"
        for s, prio in urls
    )
    write(ROOT / "sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')


def main():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    generated = {}
    for p in PAGES:
        generated[p["slug"]] = build_page(tpl, p)
    # Borra casos que ya no estén publicados.
    casos_dir = ROOT / "casos"
    if casos_dir.exists():
        for f in casos_dir.glob("*.html"):
            if f.stem not in {c["slug"] for c in CASOS_PUB}:
                f.unlink()
    if CASOS_PUB:
        generated["casos"] = build_casos_hub(tpl)
        for c in CASOS_PUB:
            generated[f"casos/{c['slug']}"] = build_case(tpl, c)
    elif (ROOT / "casos.html").exists():
        (ROOT / "casos.html").unlink()

    generated["404"] = build_404(tpl)

    for slug, doc in generated.items():
        write(ROOT / f"{slug}.html", doc)

    for slug, related in RELATED_EXISTING.items():
        f = ROOT / f"{slug}.html"
        write(f, add_related(f.read_text(encoding="utf-8"), related))

    # Menú y footer en todas las páginas.
    all_pages = sorted(ROOT.glob("*.html")) + sorted(casos_dir.glob("*.html"))
    slugs = []
    for f in all_pages:
        rel = f.relative_to(ROOT).with_suffix("").as_posix()
        current = None if rel == "index" else rel
        write(f, apply_chrome(f.read_text(encoding="utf-8"), current))
        if rel not in ("index", "404"):
            slugs.append(rel)

    order = list(EXISTING) + [p["slug"] for p in PAGES]
    slugs.sort(key=lambda s: (order.index(s) if s in order else len(order), s))
    build_sitemap(slugs)
    print(f"OK: {len(generated)} páginas generadas, {len(all_pages)} páginas con menú actualizado.")


if __name__ == "__main__":
    main()
