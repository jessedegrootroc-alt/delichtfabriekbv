# -*- coding: utf-8 -*-
"""Het projectenoverzicht met filters en de statische projectpagina's.

   Alle gegevens staan in PROJECTEN (schil.py) en komen van de bijschriften
   van de projectfoto's op de bronsite. De pagina's zijn platte HTML; er is
   geen database en geen beheeromgeving."""
import sys, pathlib, json, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat
from iconen import icoon as _icoon

VINKJE = f'<span class="filter-pil__vink" aria-hidden="true">{_icoon("check", maat=14)}</span>'


def filtergroep(label, naam, waarden, alles):
    pillen = [f'''          <button type="button" class="filter-pil is-actief" data-filter="{naam}" data-waarde="alles" aria-pressed="true">
            {VINKJE}<span>{alles}</span>
          </button>''']
    for sleutel, tekst in waarden:
        pillen.append(f'''          <button type="button" class="filter-pil" data-filter="{naam}" data-waarde="{sleutel}" aria-pressed="false">
            {VINKJE}<span>{tekst}</span>
          </button>''')
    return f'''        <div class="filter-groep" role="group" aria-label="{label}" data-groep="{naam}">
{chr(10).join(pillen)}
        </div>'''


def kaart(p):
    product_naam = PRODUCTEN[p["product"]][0]
    meta2 = p["plaats"] or TOEPASSINGEN[p["toepassing"]]
    return f'''        <article class="case-kaart" data-toepassing="{p["toepassing"]}" data-product="{p["product"]}">
          <a class="case-kaart__link hover--icon" href="project-{p["slug"]}.html">
            <figure class="case-kaart__beeld">
              {foto(p["beeld"], maten="(max-width: 767px) 100vw, (max-width: 1199px) 50vw, 33vw", alt="")}
            </figure>
            <div class="case-kaart__inhoud">
              <div class="case-kaart__meta">
                <span class="case-kaart__label">{product_naam}</span>
                <span class="case-kaart__label">{meta2}</span>
              </div>
              <h2 class="case-kaart__titel">{p["titel"]}</h2>
              <p class="case-kaart__tekst">{p["kort"]}</p>
              <div class="case-kaart__voet">
                <span class="case-kaart__lees">Bekijk het project</span>
                {icoonknop("", "button--secundair")}
              </div>
            </div>
          </a>
        </article>'''


# ====================================================================== overzicht
def overzicht():
    FAQ = [
        ("Staat mijn soort project er niet bij?", [
            "De projecten hier zijn een greep. Tunnelarmaturen maken we op klantspecificatie en voor bijzondere objecten doen we maatwerk, dus een vraag die hier niet tussen staat is geen bezwaar. Stuur een foto of tekening van de plek.",
        ]),
        ("Kan ik een project bezoeken?", [
            "De meeste projecten staan in de openbare ruimte en zijn vrij te bekijken, bijvoorbeeld de Solarbolders in de tuin van het Schielandhuis in Rotterdam of de brug bij Buikslotermeer in Amsterdam. Vraag ons gerust naar een adres.",
        ]),
        ("Leveren jullie ook buiten de Randstad?", [
            "Ja. De projecten hier staan onder meer in Amsterdam, Rotterdam, Hoofddorp en Beverwijk, maar de werkplaats in Wormerveer levert door het hele land.",
        ]),
    ]

    inhoud = f'''{patroonhero("01", "projecten", "Projecten", "Projecten")}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">Gerealiseerde projecten</h2>
          <div class="article-body content-fit--half">
            <p>Tunnels, bruggen, straten, tuinen en een enkel kunstwerk: dit is wat er hangt en staat. Per project wat er is toegepast en met welke techniek. Filter op toepassing of op product.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s03-projecten">
    <div class="container">
      <div class="cases-overzicht__filters">
{filtergroep("Filter projecten op toepassing", "toepassing", list(TOEPASSINGEN.items()), "Alle toepassingen")}
{filtergroep("Filter projecten op product", "product", [(k, v[0]) for k, v in PRODUCTEN.items()], "Alle producten")}
      </div>

      <p class="cases-overzicht__telling" role="status" aria-live="polite"></p>

      <div class="cases-overzicht__raster" id="projectRaster">
{chr(10).join(kaart(p) for p in PROJECTEN)}
      </div>

      <p class="cases-overzicht__leeg" hidden>Geen projecten die aan beide filters voldoen. Zet er een terug op &lsquo;alle&rsquo;.</p>
    </div>
  </section>

{faq_blok("04", FAQ)}

{slotblok("05", "Zit jouw plek hier nog niet tussen?")}
'''

    (UIT / "projecten.html").write_text(pagina(
        bestand="projecten.html",
        titel="Projecten | De Licht Fabriek",
        omschrijving="Gerealiseerde projecten van De Licht Fabriek: tunnelverlichting, brug- en trapverlichting, Citylight-armaturen, Solarbolders en retrofit naar LED in Amsterdam, Rotterdam, Hoofddorp en Beverwijk.",
        namespace="projecten",
        pagina_css="projecten.css",
        css_naam="projecten",
        inhoud=inhoud,
        scripts=["projecten.js"],
        extra_ld=faq_ld(FAQ),
    ), encoding="utf-8")
    print("projecten.html geschreven")


# ================================================================ detailpagina
def kenmerken(items):
    return "\n".join(f'''        <div class="kerncijfer">
          <span class="kerncijfer__label">{label}</span>
          <p class="kerncijfer__getal">{waarde}<span class="kerncijfer__eenheid">{eenheid}</span></p>
        </div>''' for label, waarde, eenheid in items)


def bleed(sleutel):
    return f'''  <figure class="case-bleed">
    {foto(sleutel, maten="100vw")}
  </figure>'''


def detailpagina(p):
    product_naam, product_link = PRODUCTEN[p["product"]]
    toepassing = TOEPASSINGEN[p["toepassing"]]
    label = f'Project · {toepassing}' + (f' · {p["plaats"]}' if p["plaats"] else '')
    alineas = "\n".join(f"              <p>{a}</p>" for a in p["inleiding"])
    punten = "\n".join(f"            <li>{x}</li>" for x in p["punten"])
    beelden = p["beelden"]
    bleed1 = bleed(beelden[0]) if beelden else ""
    bleed2 = bleed(beelden[1]) if len(beelden) > 1 else ""
    extra = "\n".join(bleed(b) for b in beelden[2:])

    # Het formulier onderaan krijgt het onderwerp dat bij het product hoort.
    onderwerp = {"titan": "tunnelarmaturen", "citylight": "paaltop-armaturen", "solarbolder": "solarbolder",
                 "geartray": "retrofit", "maatwerk": "maatwerk"}[p["product"]]

    verwant = "\n".join(projectrij(project(s), grijs=(i % 2 == 0)) for i, s in enumerate(p["verwant"]))

    inhoud = f'''  <!-- ================= 01 KOP ================= -->
  <section class="service-hero" id="s01-introductie" data-header-theme="light">
    <div class="service-hero--beeld" aria-hidden="true">
      {foto(p["beeld"], laden="eager", maten="100vw", alt="")}
      <span class="service-hero--sluier"></span>
    </div>
    <div class="container">
      <div class="service-hero--inner">
        <span class="subtitle" style="color:var(--color-white)">{label}</span>
        <h1 class="service-hero--titel">{p["titel"]}</h1>
        <div class="hero--actions">
          {knop(f"Over de {product_naam.split(' ')[0] if p['product'] != 'maatwerk' else 'maatwerk'}", product_link, "secondary")}
          {knop("Bespreek je project", "contact.html")}
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 02 KENMERKEN ================= -->
  <section class="band background--white" id="s02-kenmerken">
    <div class="container">
      <div class="kerncijfers">
{kenmerken(p["kenmerken"])}
      </div>
    </div>
  </section>

  <!-- ================= 03 HET PROJECT ================= -->
  <section class="band background--white" id="s03-project">
    <div class="container">
      <div class="case-lead">
{alineas}
      </div>
    </div>
  </section>

  <!-- ================= 04 TOEGEPAST ================= -->
  <section class="band background--grey case-blok" id="s04-toegepast">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">Wat is toegepast</h2>
        <div class="case-blok__body">
          <ul class="case-lijst" role="list">
{punten}
          </ul>
        </div>
      </div>
    </div>
  </section>

{bleed1}

  <!-- ================= 05 PRODUCT ================= -->
  <section class="band background--white case-blok" id="s05-product">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">{product_naam}</h2>
        <div class="case-blok__body">
          <p>{PRODUCT_TEKST[p["product"]]}</p>
          <p style="margin-top:var(--space-600)">{knop(f"Alles over {product_naam.split(' ')[0] if p['product'] != 'maatwerk' else 'maatwerk'}", product_link, "secundair")}</p>
        </div>
      </div>
    </div>
  </section>

{bleed2}
{extra}

  <!-- ================= 06 VERWANT ================= -->
  <section class="cases-grid" id="s06-verwant">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Verwante projecten</h2>
        {knop("Alle projecten", "projecten.html", "secundair")}
      </div>
      <div class="cases-grid__list">
{verwant}
      </div>
    </div>
  </section>

{contactblok("07", onderwerp, kop="Een vergelijkbare plek?",
             intro="Vertel kort om welke locatie het gaat en wat er nu hangt of staat. We denken mee over wat er past.")}
'''

    omschrijving = _plat(p["kort"])
    (UIT / f'project-{p["slug"]}.html').write_text(pagina(
        bestand=f'project-{p["slug"]}.html',
        titel=f'{_plat(p["titel"])} | Projecten | De Licht Fabriek',
        omschrijving=omschrijving,
        namespace="project",
        pagina_css="projecten.css",
        css_naam="projecten",
        inhoud=inhoud,
        actief="projecten.html",
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "CreativeWork",
            "name": _plat(p["titel"]),
            "description": omschrijving,
            "image": f'{BASIS}/assets/foto/{p["beeld"]}-{FOTOS[p["beeld"]][1]}.webp',
            "creator": {"@type": "Organization", "name": BEDRIJF_JURIDISCH},
            **({"locationCreated": {"@type": "Place", "name": p["plaats"]}} if p["plaats"] else {}),
        }, ensure_ascii=False, indent=2),
    ), encoding="utf-8")


PRODUCT_TEKST = {
    "titan": "De Titan is ons tunnelarmatuur op klantspecificatie: een behuizing van roestvast staal met poedercoating, een venster van polycarbonaat (transparant, boomschors of opaal) en een LED-module in de uitvoering HE of UHE. Slagvast tot IK10, optioneel met antigraffiticoating, in 2200K, 3000K of 4000K en dimbaar via Aan/Uit, DALI, 1-10V of Dynadimmer.",
    "citylight": "De Citylight is ons paaltoparmatuur voor straat, plein en speelplaats: duurzaam, slagvast polycarbonaat, efficiënte LED en aanpasbare optieken (T2, T3, T4) voor een gelijkmatige lichtspreiding. In 2200K, 3000K of 4000K en dimbaar via Aan/Uit, DALI, 1-10V of Dynadimmer.",
    "solarbolder": "De Solarbolder is een offgrid staand armatuur dat 365 dagen per jaar licht geeft op alleen zon en daglicht. Bedacht en ontworpen door Iris Dijkstra van Atelier LEK, samen met De Licht Fabriek uitgewerkt en in Nederland geproduceerd in RVS, terrazzo en duurzame elektronica.",
    "geartray": "Met een LED-geartray vervangen we alleen de binnenkant van een bestaand armatuur: LED-module, driver en waar nodig optiek en venster. De behuizing blijft hangen. Er zijn geartrays voor tunnelarmaturen en voor de Schréder Valentino en Albany, en we bouwen TL en CDO om naar LED.",
    "maatwerk": "Voor plekken waar geen standaardarmatuur past, ontwerpen, engineeren en produceren we er een: leuningverlichting, grondspots, aanlichting, een UV-A lichtbak. Alles in eigen huis in Wormerveer, op extra lage spanning waar dat moet.",
}


if __name__ == "__main__":
    overzicht()
    for p in PROJECTEN:
        detailpagina(p)
    print(f"{len(PROJECTEN)} projectpagina's geschreven")
