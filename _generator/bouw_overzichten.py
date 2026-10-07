# -*- coding: utf-8 -*-
"""De overzichten armaturen.html en diensten.html, en over-ons.html."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *

# ======================================================== armaturen.html
FAQ_ARMATUREN = [
    ("Welk armatuur past bij mijn situatie?", [
        "Geen kabel in de grond: de Solarbolder. Een tunnel of onderdoorgang: een Titan op jouw maten. Straat, plein of speelplaats op een mast: de Citylight. Twijfel je, stuur dan een situatieschets; we denken mee.",
    ]),
    ("Zijn alle armaturen dimbaar?", [
        "Ja. Aan/Uit, DALI of DALI SR, 1-10V, of een Dynadimmer met het standaard 3A-dimregime of een klantspecifiek regime. De Solarbolder regelt zichzelf op zon en daglicht.",
    ]),
    ("Welke garantie geven jullie?", [
        "Vijf jaar op onze armaturen. Ze worden ontworpen en geproduceerd in Nederland.",
    ]),
]

SITUATIES = [
    ("Solarbolder", "Geen kabel, wel licht",
     "Tuinen, parkpaden, plekken bij een monument: overal waar graven duur of ongewenst is. Werkt op zon en daglicht, 365 dagen per jaar."),
    ("Tunnelarmaturen", "Een tunnel met eigen maten",
     "Titan-armaturen op klantspecificatie in RVS en polycarbonaat, slagvast tot IK10, met antigraffiticoating als dat nodig is."),
    ("Paaltop-armaturen", "Straat, plein of speelplaats",
     "De Citylight op de mast: slagvast polycarbonaat en een optiek (T2, T3, T4) die het licht legt waar mensen lopen."),
]

kaarten = "\n".join(
    f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{bestand}">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <span class="panel__meta">{meta}</span>
            <h3 class="panel__title">{kop}</h3>
            <p class="panel__body">{tekst}</p>
            <span class="panel__actie">{icoonknop()}</span>
          </a>
        </div>'''
    for i, ((bestand, _, _, beeld), (meta, kop, tekst)) in enumerate(zip(ARMATUREN, SITUATIES)))

inhoud_armaturen = f'''{patroonhero("01", "armaturen", "Armaturen", "Armaturen")}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">Welk armatuur past waar</h2>
          <div class="article-body content-fit--half">
            <p>Drie armaturen voor drie soorten plekken. Ze delen de techniek: LED in 2200K, 3000K of 4000K, een driver die dimt zoals jij wilt, en een behuizing die tegen een stootje kan. Het verschil zit in de plek waar ze voor gemaakt zijn.</p>
            <p>Past geen van de drie? Tunnelarmaturen maken we op klantspecificatie, en voor bruggen, trappen en bijzondere objecten is er <a href="maatwerk.html">maatwerk</a>.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s03-armaturen">
    <div class="container">
{sectiekop("Kies op situatie", "Drie armaturen")}
      <div class="panel-row panel-row--3">
{kaarten}
      </div>
    </div>
  </section>

{vlakkenrij("04", "gedeeld", "Wat alle armaturen delen", [
    ("Lichtkleur", "Standaard 2200K, 3000K of 4000K. Afwijkende kleuren op aanvraag."),
    ("Sturing", "Aan/Uit, DALI of DALI SR, 1-10V, of een Dynadimmer met dimregime 3A of een eigen regime."),
    ("Materiaal", "Roestvast staal met poedercoating in een RAL-kleur, polycarbonaat venster, slagvast tot IK10."),
    ("Garantie", "Vijf jaar. Ontworpen en geproduceerd in Nederland."),
], subtitel="De techniek", intro="De keuzes die bij elk armatuur terugkomen, zodat je ze maar één keer hoeft te maken.")}

{faq_blok("05", FAQ_ARMATUREN)}

{slotblok("06", "Welk armatuur past bij jouw plek?")}
'''

(UIT / "armaturen.html").write_text(pagina(
    bestand="armaturen.html",
    titel="Armaturen: Solarbolder, tunnelarmaturen en paaltop | De Licht Fabriek",
    omschrijving="Drie LED-armaturen: de offgrid Solarbolder, Titan tunnelarmaturen op maat en het Citylight paaltoparmatuur. 2200K tot 4000K, dimbaar, vijf jaar garantie.",
    namespace="armaturen",
    pagina_css="service.css",
    css_naam="service",
    inhoud=inhoud_armaturen,
    extra_ld=faq_ld(FAQ_ARMATUREN),
), encoding="utf-8")
print("armaturen.html geschreven")

# ========================================================= diensten.html
FAQ_DIENSTEN = [
    ("Retrofit of nieuwe armaturen: hoe kies ik?", [
        "Hangt de behuizing nog goed en past er een geartray in, dan is retrofit meestal de kortste weg: alleen de techniek wordt vernieuwd. Is de behuizing op, of klopt de lichtverdeling niet meer met de plek, dan kijken we naar een nieuw armatuur.",
    ]),
    ("Doen jullie ook de installatie?", [
        "Ja. We plaatsen armaturen en bouwen bestaande armaturen om op locatie, of leveren aan je eigen installateur.",
    ]),
    ("Wat is Thermolight?", [
        "Onze naam voor thermografisch onderzoek: een warmtebeeldopname waarmee we afwijkingen in elektrische installaties en warmtegerelateerde problemen snel zichtbaar maken.",
    ]),
]

DIENST_SITUATIES = [
    ("Retrofit", "Er hangt al een armatuur",
     "LED-geartrays voor tunnelarmaturen, Schréder Valentino en Albany, en ombouw van TL en CDO naar LED. De behuizing blijft, de techniek wordt nieuw."),
    ("Maatwerk", "Er past geen standaardarmatuur",
     "Ontwerp, engineering, productie en installatie van verlichting voor bruggen, trappen, kunstwerken en andere bijzondere objecten."),
    ("Thermolight", "Een installatie vertoont kuren",
     "Thermografisch onderzoek dat afwijkingen in elektrische installaties en warmteproblemen snel en vakkundig zichtbaar maakt."),
]

dienstkaarten = "\n".join(
    f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{bestand}">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <span class="panel__meta">{meta}</span>
            <h3 class="panel__title">{kop}</h3>
            <p class="panel__body">{tekst}</p>
            <span class="panel__actie">{icoonknop()}</span>
          </a>
        </div>'''
    for i, ((bestand, _, _, beeld), (meta, kop, tekst)) in enumerate(zip(DIENSTEN, DIENST_SITUATIES)))

inhoud_diensten = f'''{patroonhero("01", "diensten", "Diensten", "Diensten")}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">Wat we doen naast armaturen maken</h2>
          <div class="article-body content-fit--half">
            <p>Niet elke vraag begint met een leeg plafond. Vaak hangt er al iets dat beter kan, of is er een plek waar niets standaards past. En soms is de vraag niet eens licht, maar warmte: waar wordt het te heet in een installatie?</p>
            <p>Drie diensten voor die drie situaties, alle drie vanuit dezelfde werkplaats in Wormerveer.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s03-diensten">
    <div class="container">
{sectiekop("Kies op situatie", "Drie diensten")}
      <div class="panel-row panel-row--3">
{dienstkaarten}
      </div>
    </div>
  </section>

  <!-- ================= 04 WERKWIJZE ================= -->
  <section class="band background--grey" id="s04-werkwijze">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Werkwijze</span>
          <h2 class="section-heading">Alles onder één dak</h2>
          <p class="article-body" style="margin-top:var(--space-500)">Ontwerp, engineering, productie en installatie gebeuren in eigen huis. Dat is wat de klantwens vertaalt naar een passende oplossing en wat de kwaliteit waarborgt.</p>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
            <li class="trede" style="--trede:0">
              <span class="trede__nummer">01</span>
              <div class="trede__inhoud">
                <h3 class="trede__titel">Ontwerp</h3>
                <p class="trede__tekst">De vraag en de plek worden vertaald naar een lichtontwerp: waar komt het licht, hoeveel, in welke kleur.</p>
              </div>
            </li>
            <li class="trede" style="--trede:1">
              <span class="trede__nummer">02</span>
              <div class="trede__inhoud">
                <h3 class="trede__titel">Engineering</h3>
                <p class="trede__tekst">Module, optiek, driver, voeding en behuizing in 3D en op tekening, inclusief spanning en slagvastheid.</p>
              </div>
            </li>
            <li class="trede" style="--trede:2">
              <span class="trede__nummer">03</span>
              <div class="trede__inhoud">
                <h3 class="trede__titel">Productie</h3>
                <p class="trede__tekst">In de werkplaats in Wormerveer: behuizing, montage, proefopstelling.</p>
              </div>
            </li>
            <li class="trede" style="--trede:3">
              <span class="trede__nummer">04</span>
              <div class="trede__inhoud">
                <h3 class="trede__titel">Installatie</h3>
                <p class="trede__tekst">Plaatsen, ombouwen en inregelen op locatie, of leveren aan je installateur.</p>
              </div>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </section>

{faq_blok("05", FAQ_DIENSTEN)}

{slotblok("06", "Welke dienst past bij jouw vraag?")}
'''

(UIT / "diensten.html").write_text(pagina(
    bestand="diensten.html",
    titel="Diensten: retrofit, maatwerk en thermografie | De Licht Fabriek",
    omschrijving="Bestaande armaturen verledden met LED-geartrays, verlichting op maat voor bruggen en bijzondere objecten, en thermografisch onderzoek. Alles in eigen huis in Wormerveer.",
    namespace="diensten",
    pagina_css="service.css",
    css_naam="service",
    inhoud=inhoud_diensten,
    extra_ld=faq_ld(FAQ_DIENSTEN),
), encoding="utf-8")
print("diensten.html geschreven")

# ========================================================= over-ons.html
FAQ_OVER = [
    ("Waar werken jullie?", [
        "De werkplaats staat aan de Rosbayerweg in Wormerveer. Projecten staan onder meer in Amsterdam, Rotterdam, Hoofddorp en Beverwijk.",
    ]),
    ("Produceren jullie zelf?", [
        "Ja. Ontwerp, engineering en productie gebeuren in eigen huis. Dat is ook waarom we tunnelarmaturen op klantspecificatie kunnen maken en geartrays kunnen engineeren op een bestaand armatuur.",
    ]),
    ("Welke garantie geven jullie?", [
        "Vijf jaar op onze armaturen, die in Nederland worden ontworpen en geproduceerd.",
    ]),
]

# De vier waarden zijn de drie kernpunten van de bronsite (Maatwerk, Duurzaam
# gedacht, Slim licht) plus de badge Made in Holland.
WAARDEN = [
    ("Maatwerk", "Verlichtingsoplossingen op maat, afgestemd op het project, de wensen en de technische eisen."),
    ("Duurzaam gedacht", "Energiezuinige verlichting met een lange levensduur, minimale impact en aandacht voor circulair ontwerp: een behuizing die blijft, techniek die vernieuwd wordt."),
    ("Slim licht", "Verlichting die zich automatisch aanpast, energie bespaart en comfort en efficiëntie verhoogt: Dynadimmer, DALI, 1-10V."),
    ("Made in Holland", "Ontworpen en geproduceerd in Wormerveer, met vijf jaar garantie."),
]

WERKWIJZE = [
    ("Ontwerp", "Elk armatuur begint als tekening. De Citylight is in 3D ontworpen en in een tweede generatie doorontwikkeld.",
     "citylight-ontwerp", "3D-ontwerp van het Citylight-armatuur", "grey"),
    ("Engineering", "Module, optiek, driver en behuizing worden op elkaar en op de plek afgestemd; voor retrofit op het bestaande armatuur.",
     "geartray-ontwerp", "Technische weergave van een vervangende LED-geartray", "white"),
    ("Productie", "In de werkplaats in Wormerveer. Hier brandt een Citylight mini voor het eerst, voordat hij de deur uitgaat.",
     "citylight-mini", "Citylight mini brandend in de werkplaats", "white"),
    ("Installatie en retrofit", "Plaatsen en ombouwen op locatie, met de retrofitmodule en de slimme driver uit eigen productie.",
     "retrofit-module", "LED-retrofitmodule met driver op een montageplaat", "grey"),
]

kaarten_werkwijze = "\n".join(
    beeldkaart(kop, tekst, beeld, alt=alt, kleur=kleur)
    for kop, tekst, beeld, alt, kleur in WERKWIJZE
)

inhoud_over = f'''{paginahero("01", "over", "Over De Licht Fabriek", "Over ons", "schielandhuis-pad")}

  <section class="content-text-side-cta" id="s02-statement">
    <div class="container">
      <div class="content-text-side-cta--container">
        <div class="content-text-side-cta--body">
          <p>De Licht Fabriek: waar de klantwens wordt vertaald naar een passende oplossing. Onze interne engineering en productie waarborgen de gewenste kwaliteit.</p>
        </div>
      </div>
    </div>
  </section>

{vlakkenrij("03", "waarden", "Waar we voor staan", WAARDEN, subtitel="Onze uitgangspunten")}

  <section class="content-block" id="s04-werkwijze">
    <div class="container">
{sectiekop("Werkwijze", "Vier stappen, één adres",
           "Ontwerp, engineering, productie en installatie gebeuren in eigen huis. Zo kan een ontwerp onderweg nog veranderen zonder dat de planning omvalt, en zit de kennis van het armatuur later nog bij dezelfde mensen.")}
      <div class="row g-0">
{kaarten_werkwijze}
      </div>
    </div>
  </section>

  <section class="streamer streamer--employee background--donker" id="s05-bedrijf">
    <div class="container">
      <div class="streamer--employee-row">
        <figure class="streamer--employee-portrait">
          {foto("schielandhuis-bolder-2", maten="(max-width: 991px) 100vw, 40vw")}
        </figure>
        <div class="streamer--employee-panel band">
          <span class="subtitle" style="color:var(--color-white)">Het bedrijf</span>
          <h2 class="streamer--employee-name">Van Wormerveer naar de openbare ruimte</h2>
          <div class="article-body content-fit--half">
            <p>De Licht Fabriek B.V. is gevestigd aan de Rosbayerweg 19 in Wormerveer. Van daaruit maken we LED-verlichting voor openbare verlichting, outdoor en solar: nieuwe armaturen, maatwerk voor bijzondere objecten en geartrays om bestaande armaturen te verledden.</p>
            <p>Onze projecten staan onder meer in Amsterdam, Rotterdam, Hoofddorp en Beverwijk: tunnels, bruggen, pleinen en tuinen. Op wat we maken geven we vijf jaar garantie.</p>
          </div>
          <div>
            {knop("Bekijk de projecten", "projecten.html", "secondary")}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s06-samenwerking">
    <div class="container">
{sectiekop("Samenwerking", "Met ontwerpers en opdrachtgevers",
           "Een goed armatuur ontstaat zelden alleen. We werken met lichtontwerpers, architecten, gemeenten en installateurs; de Solarbolder is daar het voorbeeld van.")}
      <div class="panel-row panel-row--3">
        <div>
          <div class="panel panel--grey">
            <span class="panel__meta">Ontwerpbureau</span>
            <h3 class="panel__title">Atelier LEK</h3>
            <p class="panel__body">De Solarbolder is bedacht en ontworpen door Iris Dijkstra van Atelier LEK. Samen hebben we het idee omgezet in een duurzaam gefabriceerde bolder die in Nederland wordt geproduceerd. <a href="http://www.atelierlek.nl" rel="noopener">atelierlek.nl</a></p>
          </div>
        </div>
        <div>
          <div class="panel">
            <span class="panel__meta">Lichtontwerpers en architecten</span>
            <h3 class="panel__title">Van ontwerp naar product</h3>
            <p class="panel__body">Een ontwerp van buiten werken we uit tot een armatuur dat te maken, te plaatsen en te onderhouden is, zonder dat het ontwerp zijn vorm verliest.</p>
          </div>
        </div>
        <div>
          <div class="panel panel--grey">
            <span class="panel__meta">Gemeenten en installateurs</span>
            <h3 class="panel__title">Van beheer naar uitvoering</h3>
            <p class="panel__body">Voor beheerders van openbare verlichting en hun installateurs maken we armaturen en geartrays die passen in de bestaande sturing en het bestaande onderhoud.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

{faq_blok("07", FAQ_OVER)}

{slotblok("08", "Kennismaken?")}
'''

(UIT / "over-ons.html").write_text(pagina(
    bestand="over-ons.html",
    titel="Over ons | De Licht Fabriek",
    omschrijving="De Licht Fabriek B.V. in Wormerveer ontwerpt, engineert en produceert LED-verlichting voor openbare ruimte, outdoor en solar. Maatwerk, duurzaam, Made in Holland.",
    namespace="over-ons",
    pagina_css="over-ons.css",
    css_naam="over-ons",
    inhoud=inhoud_over,
    extra_ld=faq_ld(FAQ_OVER),
), encoding="utf-8")
print("over-ons.html geschreven")
