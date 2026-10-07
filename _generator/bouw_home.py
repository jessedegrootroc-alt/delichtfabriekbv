# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat

FAQ = [
    ("Maken jullie ook armaturen op maat?", [
        "Ja. Tunnelarmaturen ontwerpen en produceren we in eigen beheer op klantspecificatie, en voor bruggen, trappen en bijzondere objecten maken we verlichting die er niet uit de catalogus is: leuningverlichting op 48V, grondspots in een trap, een UV-A lichtbak voor een restauratieatelier.",
        "Alles gebeurt in eigen huis in Wormerveer: ontwerp, engineering, productie en installatie.",
    ]),
    ("Kunnen bestaande armaturen worden omgebouwd naar LED?", [
        "Ja. Met een LED-geartray vervangen we alleen de binnenkant: module, driver en waar nodig optiek en venster. De behuizing blijft hangen. Er zijn geartrays voor tunnelarmaturen en voor de Schréder Valentino en Albany, en we bouwen TL en CDO om naar LED.",
    ]),
    ("Welke lichtkleuren en sturingen leveren jullie?", [
        "Standaard 2200K, 3000K en 4000K; afwijkende kleuren op aanvraag. Voor de sturing: Aan/Uit, DALI of DALI SR, 1-10V, of een Dynadimmer met het standaard 3A-dimregime of een klantspecifiek regime.",
    ]),
]

# De drie getallen en waar ze vandaan komen:
# - 5 jaar garantie: de badge "Made in Holland, vijf jaar garantie" op de bronsite;
# - 200 lumen per watt: bijschrift "vervangende geartray zeer efficiënt 200 lumen per watt";
# - 365 dagen: "De Solarbolder ... geeft 365 dagen per jaar licht in de duisternis".
CIJFERS = [
    ("5", "jaar garantie", "Op onze armaturen, ontworpen en gemaakt in Nederland."),
    ("200", "lumen per watt", "Het rendement van onze efficiëntste LED-geartray voor bestaande armaturen."),
    ("365", "dagen per jaar licht", "De Solarbolder werkt op zon en daglicht, zonder aansluiting op het net."),
]

HOME_PROJECTEN = ["brug-buikslotermeer-amsterdam", "solarbolder-schielandhuis-rotterdam", "verledden-tunnel-geartray-22w"]

INTROS_ARMATUREN = [
    "Een staand armatuur dat alleen zon en daglicht nodig heeft. Ontwerp van Atelier LEK, gemaakt in Nederland in RVS en terrazzo.",
    "In eigen beheer ontworpen en geproduceerd op klantspecificatie. Slagvast tot IK10, optioneel met antigraffiticoating.",
    "Het Citylight-armatuur voor straat, plein en speelplaats: slagvast polycarbonaat en een optiek die het licht legt waar het hoort.",
]
armaturen = "\n".join(aanbodkaart(i, a, intro, "Armatuur")
                      for i, (a, intro) in enumerate(zip(ARMATUREN, INTROS_ARMATUREN)))

diensten = "\n".join(fotokaart(i, d) for i, d in enumerate(DIENSTEN))

projecten = "\n".join(projectrij(project(s), grijs=(i % 2 == 0)) for i, s in enumerate(HOME_PROJECTEN))

cijfers = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <p class="usp__getal" data-telop="{getal}">{getal}</p>
            <p class="usp__label">{label}</p>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (getal, label, tekst) in enumerate(CIJFERS))

inhoud = f'''  <!-- ================= 01 INTRODUCTIE ================= -->
  <section class="hero" id="s01-introductie" data-header-theme="light">
    <div class="hero--beeld" aria-hidden="true">
      {foto("hero-tunnel-titan", laden="eager", maten="100vw")}
      <span class="hero--sluier"></span>
    </div>
    <div class="container hero--container">
      <div class="hero--content">
        <span class="subtitle" style="color:var(--color-white)">LED-verlichting voor openbare ruimte, outdoor en solar</span>
        <h1 class="hero--title">Licht dat past bij de plek</h1>
        <div class="hero--intro article-body">
          <p>De Licht Fabriek ontwerpt, engineert en produceert LED-verlichting voor tunnels, bruggen, straten en pleinen: armaturen op maat, de offgrid Solarbolder en LED-geartrays om bestaande armaturen te verledden.</p>
          <p>Gemaakt in Wormerveer, met vijf jaar garantie.</p>
        </div>
        <div class="hero--actions">
          {knop("Bespreek je project", "contact.html")}
          {knop("Bekijk de projecten", "projecten.html", "secondary")}
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 02 WAT WE DOEN ================= -->
  <section class="content-text-side-cta" id="s02-wat-we-doen">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
              <p>Een tunnel heeft andere maten dan de vorige, een brugleuning moet veilig op lage spanning, en een armatuur dat nog goed hangt hoeft niet weg omdat de lamp verouderd is. Daarom maken we verlichting op de vraag: ontwerp, engineering en productie in eigen huis, en de techniek erin die dimt, lang meegaat en tegen een stootje kan.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 03 EEN PARTIJ ================= -->
  <section class="content-text-side-visual background--white" id="s03-eigen-huis">
    <div class="container">
      <div class="row gx-0">
        <article class="col-lg-4 col-12">
          <div class="content-text-side-visual--stack content-text-side-visual--article">
            <h2>Van vraag tot armatuur, onder één dak</h2>
            <div class="content-text-side-visual--body content-fit--quarter">
              <p>De klantwens wordt vertaald naar een passende oplossing. Onze interne engineering en productie waarborgen de kwaliteit: het ontwerp wordt in 3D uitgewerkt, de behuizing in RVS of polycarbonaat gemaakt, de LED-module en de driver gemonteerd en ingeregeld op het dimregime dat jij wilt.</p>
              <p>Daarna plaatsen we het armatuur, of leveren we het aan je installateur. Komt er later een vraag, dan zit de kennis van het armatuur nog bij dezelfde mensen.</p>
            </div>
            {knop("Lees over onze werkwijze", "over-ons.html")}
          </div>
        </article>
      </div>
    </div>
    <div class="content-text-side-visual--visual added-distance">
      {foto("citylight-2025", maten="(max-width: 991px) calc(100vw - 32px), (max-width: 1199px) calc(100vw - 96px), (max-width: 1352px) 940px, 70vw")}
    </div>
  </section>

  <!-- ================= 04 ARMATUREN ================= -->
  <section class="content-block" id="s04-armaturen">
    <div class="container">
{sectiekop("Armaturen", "Drie armaturen, elk voor een andere plek",
           "Een offgrid bolder voor waar geen kabel ligt, een tunnelarmatuur dat we op jouw maten maken en een paaltoparmatuur voor straat en plein. Alle drie in 2200K, 3000K of 4000K en dimbaar met DALI, 1-10V of Dynadimmer.",
           knop("Alle armaturen", "armaturen.html"))}
      <div class="row g-0">
{armaturen}
      </div>
    </div>
  </section>

  <!-- ================= 05 PROJECTEN ================= -->
  <section class="cases-grid" id="s05-projecten">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Gerealiseerde projecten</h2>
        {knop("Alle projecten", "projecten.html", "secundair")}
      </div>
      <div class="cases-grid__list">
{projecten}
      </div>
    </div>
  </section>

  <!-- ================= 06 CIJFERS ================= -->
  <section class="content-block" id="s06-cijfers">
    <div class="container">
{sectiekop("In cijfers", "Waar je op kunt rekenen")}
      <div class="panel-row panel-row--3">
{cijfers}
      </div>
    </div>
  </section>

  <!-- ================= 07 DIENSTEN ================= -->
  <section class="content-block" id="s07-diensten">
    <div class="container">
{sectiekop("Diensten", "Ook als er al iets hangt",
           "Bestaande armaturen verledden met een geartray, verlichting op maat voor een object waar geen standaardarmatuur past, of een warmtebeeld van een installatie die kuren vertoont.",
           knop("Alle diensten", "diensten.html"))}
      <div class="panel-row panel-row--3">
{diensten}
      </div>
    </div>
  </section>

{quoteslider("08", "reviews", "Wat opdrachtgevers zeggen", "Uit de samenwerking", REVIEWS)}

{faq_blok("09", FAQ, "Wat men meestal eerst vraagt")}

  <!-- ================= 10 OVER DE LICHT FABRIEK ================= -->
  <section class="streamer streamer--employee background--donker" id="s10-over">
    <div class="container">
      <div class="streamer--employee-row">
        <figure class="streamer--employee-portrait">
          {foto("citylight-mini", maten="(max-width: 991px) 100vw, 40vw")}
        </figure>
        <div class="streamer--employee-panel band">
          <span class="subtitle" style="color:var(--color-white)">Over De Licht Fabriek</span>
          <h2 class="streamer--employee-name">Gemaakt in Wormerveer</h2>
          <div class="article-body content-fit--half">
            <p>De Licht Fabriek is een Nederlandse maker van LED-verlichting voor de openbare ruimte, outdoor en solar. Vanuit de werkplaats aan de Rosbayerweg in Wormerveer ontwerpen, engineeren en produceren we armaturen, en bouwen we bestaande armaturen om naar LED.</p>
            <p>We denken in maatwerk, duurzaamheid en slim licht: een armatuur dat past bij het project, lang meegaat en vanzelf terugregelt als er niemand is. Op wat we maken geven we vijf jaar garantie.</p>
          </div>
          <div>
            {knop("Meer over ons", "over-ons.html")}
          </div>
        </div>
      </div>
    </div>
  </section>

{slotblok("11", "Een plek die licht nodig heeft?")}
'''

(UIT / "index.html").write_text(pagina(
    bestand="index.html",
    titel="De Licht Fabriek | LED-verlichting voor openbare ruimte en solar",
    omschrijving="LED-verlichting uit Wormerveer: tunnelarmaturen op maat, de offgrid Solarbolder, Citylight paaltoparmaturen en LED-geartrays voor retrofit. Vijf jaar garantie.",
    namespace="home",
    pagina_css="index.css",
    css_naam="index",
    inhoud=inhoud,
    scripts=["index.js"],
    extra_ld=faq_ld(FAQ),
), encoding="utf-8")

print("index.html geschreven")
