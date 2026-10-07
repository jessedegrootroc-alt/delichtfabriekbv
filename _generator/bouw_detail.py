# -*- coding: utf-8 -*-
"""Eén template voor de detailpagina's van armaturen en diensten.

   De pagina's delen de kop (paginahero), het statement en de staart (FAQ,
   kenmerkenband, CTA). Daartussen kiest elke pagina zelf welke blokken er
   staan en in welke volgorde (cfg["volgorde"]), zodat een productpagina met
   specificaties er anders uitziet dan een dienstpagina met een beeldverhaal,
   zonder dat er een tweede visuele taal ontstaat."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat
from iconen import icoon as _icoon

# Namen in de iconenset (assets/iconen/), per voordeel; zie iconen.py.
ICONEN = {
    "zon": "sun", "lamp": "lightbulb", "blad": "leaf", "schild": "shield-check",
    "sleutel": "wrench", "liniaal": "ruler-pen", "schuif": "sliders-2", "pin": "map-pin",
    "klok": "clock", "recycle": "recycle", "stekker": "plug", "thermometer": "thermometer",
    "tandwiel": "gear", "certificaat": "award-certificate", "bliksem": "bolt", "oog": "eye",
    "hand": "handshake", "lagen": "layers", "hamer": "hammer", "vrachtwagen": "truck",
    "vinkje": "check", "lijst": "list-check", "zoek": "magnifier", "doel": "target",
    "cirkel": "arrows-rotate-center", "helderheid": "brightness", "maan": "moon",
    "paneel": "solar-panel", "meter": "gauge-2", "contrast": "contrast", "slot": "lock",
}


def icoon(naam):
    return _icoon(ICONEN[naam], klasse="voordeel__icoon", maat=24)


def situatiekaarten(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">Situatie {i + 1:02d}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (titel, tekst) in enumerate(items))


def stappen(items, label):
    return "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{i + 1:02d}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{titel}</h3>
            <p class="trede__tekst">{tekst}</p>
            {f'<p class="trede__gedrag"><span>{label}</span> {extra}</p>' if extra else ''}
          </div>
        </li>''' for i, (titel, tekst, extra) in enumerate(items))


def voordelen(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            {icoon(ico)}
            <h3 class="voordeel__titel">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (ico, titel, tekst) in enumerate(items))


def specpanelen(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'} spec">
            <span class="panel__meta">{meta}</span>
            <h3 class="panel__title spec__titel">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (meta, titel, tekst) in enumerate(items))


def detailpagina(cfg):
    nr = [1]

    def volgend():
        nr[0] += 1
        return f"{nr[0]:02d}"

    blokken = [paginahero("01", "introductie", cfg["eyebrow"], cfg["h1"], cfg["hero_foto"],
                          positie=cfg.get("hero_positie"), hoog=True)]

    for sectie in cfg["volgorde"]:
        n = volgend()
        if sectie == "statement":
            label, href = cfg.get("statement_knop", ("Bespreek je project", "contact.html"))
            blokken.append(f'''  <!-- ================= {n} STATEMENT ================= -->
  <section class="content-text-side-cta" id="s{n}-statement">
    <div class="container">
      <div class="content-text-side-cta--container">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
{cfg["intro"]}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop(label, href)}
          </div>
        </div>
      </div>
    </div>
  </section>''')

        elif sectie == "situaties":
            s = cfg["situaties"]
            blokken.append(f'''  <!-- ================= {n} WANNEER ================= -->
  <section class="content-block" id="s{n}-wanneer">
    <div class="container">
{sectiekop(s.get("subtitel", "Herkenbaar?"), s["kop"], s.get("intro"))}
      <div class="panel-row panel-row--3">
{situatiekaarten(s["items"])}
      </div>
    </div>
  </section>''')

        elif sectie == "aanpak":
            a = cfg["aanpak"]
            blokken.append(f'''  <!-- ================= {n} AANPAK ================= -->
  <section class="band background--grey" id="s{n}-aanpak">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">{a.get("subtitel", "Zo werken we")}</span>
          <h2 class="section-heading">{a["kop"]}</h2>
          <p class="article-body" style="margin-top:var(--space-500)">{a["intro"]}</p>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{stappen(a["stappen"], a.get("label", "Jij levert"))}
          </ol>
        </div>
      </div>
    </div>
  </section>''')

        elif sectie == "voordelen":
            v = cfg["voordelen"]
            blokken.append(f'''  <!-- ================= {n} VOORDELEN ================= -->
  <section class="content-block" id="s{n}-voordelen">
    <div class="container">
{sectiekop(v.get("subtitel", "Wat het oplevert"), v["kop"], v.get("intro"))}
      <div class="panel-row panel-row--4">
{voordelen(v["items"])}
      </div>
    </div>
  </section>''')

        elif sectie == "specs":
            s = cfg["specs"]
            kolommen = "panel-row--3" if len(s["items"]) % 3 == 0 and len(s["items"]) % 4 else "panel-row--4"
            blokken.append(f'''  <!-- ================= {n} SPECIFICATIES ================= -->
  <section class="content-block" id="s{n}-specificaties">
    <div class="container">
{sectiekop(s.get("subtitel", "Opties en uitvoeringen"), s["kop"], s.get("intro"))}
      <div class="panel-row {kolommen}">
{specpanelen(s["items"])}
      </div>
    </div>
  </section>''')

        elif sectie == "beeldtekst":
            b = cfg["beeldtekst"]
            knop_html = knop(*b["knop"]) if b.get("knop") else ""
            blokken.append(f'''  <!-- ================= {n} BEELD EN TEKST ================= -->
  <section class="content-text-side-visual background--white" id="s{n}-{b.get("ident", "toelichting")}">
    <div class="container">
      <div class="row gx-0">
        <article class="col-lg-4 col-12">
          <div class="content-text-side-visual--stack content-text-side-visual--article">
            <h2>{b["kop"]}</h2>
            <div class="content-text-side-visual--body content-fit--quarter">
{b["tekst"]}
            </div>
            {knop_html}
          </div>
        </article>
      </div>
    </div>
    <div class="content-text-side-visual--visual content-fit--half">
      {foto(b["foto"], maten="(max-width: 991px) 100vw, 48vw")}
    </div>
  </section>''')

        elif sectie == "galerij":
            g = cfg["galerij"]
            if g.get("kolommen") == 3:
                # Drie kleinere panelen met de foto erboven, voor een reeks
                # voorbeelden die geen eigen verhaal vertellen.
                kaarten = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'} panel--beeld">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_3)}
            </figure>
            <span class="panel__meta">{meta}</span>
            <h3 class="panel__title">{kop}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (meta, kop, tekst, beeld) in enumerate(g["items"]))
                raster = f'<div class="panel-row panel-row--3">\n{kaarten}\n      </div>'
            else:
                kleuren = ("grey", "white", "white", "grey")
                kaarten = "\n".join(
                    beeldkaart(kop, tekst, beeld, meta=meta, kleur=kleuren[i % 4])
                    for i, (meta, kop, tekst, beeld) in enumerate(g["items"]))
                raster = f'<div class="row g-0">\n{kaarten}\n      </div>'
            blokken.append(f'''  <!-- ================= {n} IN BEELD ================= -->
  <section class="content-block" id="s{n}-{g.get("ident", "in-beeld")}">
    <div class="container">
{sectiekop(g.get("subtitel", "In beeld"), g["kop"], g.get("intro"))}
      {raster}
    </div>
  </section>''')

        elif sectie == "projecten":
            blokken.append(projectenblok(n, cfg["projecten"], kop=cfg.get("projecten_kop", "Uit de praktijk")))

        elif sectie == "faq":
            blokken.append(faq_blok(n, cfg["faq"]))

        elif sectie == "slot":
            blokken.append(slotblok(n, cfg["contact_kop"], cfg.get("contact_tekst")))
            nr[0] += 1

        else:
            raise ValueError(f"onbekende sectie {sectie!r} in {cfg['bestand']}")

    inhoud = "\n\n".join(blokken) + "\n"

    ld = cfg.get("ld") or {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": cfg["service_type"],
        "name": _plat(cfg["h1"]),
        "description": cfg["omschrijving"],
        "areaServed": "NL",
        "provider": {"@type": "Organization", "name": BEDRIJF_JURIDISCH},
    }
    extra_ld = json.dumps(ld, ensure_ascii=False, indent=2)
    if cfg.get("faq"):
        extra_ld += "\n</script>\n<script type=\"application/ld+json\">\n" + faq_ld(cfg["faq"])

    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"],
        titel=cfg["titel"],
        omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"],
        pagina_css="service.css",
        css_naam="service",
        inhoud=inhoud,
        extra_ld=extra_ld,
    ), encoding="utf-8")
    print(cfg["bestand"], "geschreven")


def product_ld(naam, omschrijving, beeld, extra=None):
    """Product-structuurdata voor de drie armaturen."""
    d = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": naam,
        "description": omschrijving,
        "brand": {"@type": "Brand", "name": BEDRIJF},
        "manufacturer": {"@type": "Organization", "name": BEDRIJF_JURIDISCH},
        "image": f"{BASIS}/assets/foto/{beeld}-{FOTOS[beeld][1]}.webp",
        "countryOfOrigin": "NL",
    }
    if extra:
        d.update(extra)
    return d
