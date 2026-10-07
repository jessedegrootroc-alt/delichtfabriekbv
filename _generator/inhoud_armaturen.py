# -*- coding: utf-8 -*-
"""De inhoud van de drie armatuurpagina's. Het skelet staat in bouw_detail.py.
   Feiten: delichtfabriekbv.nl (solarbolder, tunnelarmaturen, paaltop-armaturen)
   en de bijschriften van de projectfoto's; zie work/migration-state.md."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bouw_detail import detailpagina, product_ld

# Opties die voor Titan en Citylight gelijk zijn (bron: beide productpagina's).
LEDKLEUR = ("LED-kleur", "2200K, 3000K of 4000K",
            "Standaard in drie kleurtemperaturen. Afwijkende kleuren op aanvraag.")
STURING = ("Sturing", "Aan/Uit, DALI, 1-10V of Dynadimmer",
           "DALI of DALI SR, 1-10V, of een Dynadimmer met het standaard 3A-dimregime of een klantspecifiek regime.")
GARANTIE = ("Garantie", "5 jaar, Made in Holland",
            "Ontworpen en geproduceerd in Nederland. Op onze armaturen geven we vijf jaar garantie.")

# ============================================================ Tunnelarmaturen
detailpagina({
    "bestand": "tunnelarmaturen.html",
    "namespace": "tunnelarmaturen",
    "titel": "Titan tunnelarmaturen op maat | De Licht Fabriek",
    "omschrijving": "Tunnelarmaturen in eigen beheer ontworpen en geproduceerd op klantspecificatie: RVS met poedercoat, polycarbonaat venster, IK10, antigraffiticoating, 2200K tot 4000K, dimbaar.",
    "service_type": "Tunnelarmaturen op klantspecificatie",
    "eyebrow": "Armatuur · Titan",
    "h1": "Tunnelarmaturen op maat",
    "hero_foto": "verledden-geartray",
    "volgorde": ["statement", "situaties", "aanpak", "specs", "voordelen", "galerij", "projecten", "faq", "slot"],
    "intro": '''          <p>Een tunnel of onderdoorgang is zelden standaard: andere maten, een ander plafond, een andere wand, en vaak een geschiedenis van vandalisme. Onze tunnelarmaturen ontwerpen en produceren we daarom in eigen beheer, op jouw specificatie. Tot op heden is geen uitdaging te groot gebleken.</p>
          <p>De Titan is de basis: een behuizing van roestvast staal met poedercoating, een venster van polycarbonaat en een LED-module in de uitvoering HE (high efficiency) of UHE (ultra high efficiency). Slagvast tot IK10, optioneel met een antigraffiticoating die je niet ziet maar wel merkt.</p>''',
    "situaties": {
        "kop": "Wanneer kies je voor een Titan?",
        "intro": "Drie situaties waarin een armatuur op klantspecificatie meer oplevert dan een catalogusproduct.",
        "items": [
            ("Nieuwe tunnel of onderdoorgang",
             "De maten en de montage liggen vast in het ontwerp van het kunstwerk. Het armatuur moet daarin passen, niet andersom. We maken de behuizing op de maat van de sparing of de wand."),
            ("Veel vandalisme en graffiti",
             "Een polycarbonaat venster in klasse IK10 houdt een klap. Met de antigraffiticoating op behuizing en venster is verf weer schoon te maken zonder dat de coating zichtbaar is."),
            ("Bestaande armaturen aan vervanging toe",
             "Vaak hoeft de behuizing niet weg. Met een LED-geartray en een nieuw venster gaat alleen de techniek eruit. Zie <a href=\"retrofit.html\">retrofit</a>."),
        ],
    },
    "aanpak": {
        "kop": "Van sparing tot brandend armatuur",
        "intro": "Omdat we ontwerpen, engineeren en produceren in eigen huis, zit er geen schakel tussen jouw vraag en het armatuur dat aan de wand hangt.",
        "label": "Jij levert",
        "stappen": [
            ("Maten en situatie", "Je stuurt de maten van de sparing of de wand, foto's van de situatie en de lichtwens: kleurtemperatuur, dimregime, sturing. Bestaande tekeningen zijn welkom.",
             "maten, foto's en de gewenste lichtkleur en sturing"),
            ("Ontwerp en engineering", "We werken de behuizing, het venster, de optiek en de driver uit en leggen het ontwerp aan je voor. De RAL-kleur van de poedercoating kies je uit de standaardreeks of naar wens.",
             "akkoord op tekening en kleur"),
            ("Productie in Wormerveer", "De behuizing in RVS wordt gemaakt en gepoedercoat, het venster in polycarbonaat gezet, de LED-module en de driver gemonteerd. Optioneel de antigraffiticoating.",
             ""),
            ("Levering en plaatsing", "We leveren de armaturen aan of plaatsen ze zelf, inclusief de inregeling van het dimregime.",
             "toegang tot de locatie en de voeding"),
        ],
    },
    "specs": {
        "kop": "Wat je kunt kiezen",
        "intro": "De vaste onderdelen van de Titan en de opties daarop. Niet genoemd? Vraag het; op klantspecificatie kan meer.",
        "items": [
            ("Behuizing", "RVS met poedercoating", "Roestvast staal, gepoedercoat in een standaard RAL-kleur of conform je wens."),
            ("Venster", "Polycarbonaat, drie uitvoeringen", "Transparant, met boomschorseffect of opaal. Opaal heeft een LTA van 82%: 82% van het licht gaat door het venster naar buiten."),
            ("Coating", "Antigraffiti, onzichtbaar", "Optioneel op behuizing en venster. Beide coatings zijn na het aanbrengen niet zichtbaar."),
            ("Slagvastheid", "IK10", "De hoogste slagvastheidsklasse voor armaturen in de openbare ruimte."),
            LEDKLEUR,
            STURING,
            ("Optiek", "60 graden", "De optiek bepaalt waar het licht komt; op de projecten hiernaast is dat een hoek van 60 graden."),
            ("Uitvoering", "HE of UHE", "High efficiency of ultra high efficiency: hoe meer licht per watt, hoe lager het verbruik bij hetzelfde lichtniveau."),
        ],
    },
    "voordelen": {
        "kop": "Wat een armatuur op maat oplevert",
        "items": [
            ("liniaal", "Het past in het ontwerp", "Geen aanpassingen aan de tunnel om het armatuur te laten passen: het armatuur volgt de maten van het kunstwerk."),
            ("schild", "Bestand tegen een klap en tegen verf", "IK10 en een antigraffiticoating, zodat onderhoud schoonmaken is en geen vervangen."),
            ("schuif", "Dimt zoals jij wilt", "Aan/Uit, DALI, 1-10V of een Dynadimmer met regime 3A: het armatuur past in je bestaande sturing."),
            ("certificaat", "Vijf jaar garantie", "Ontworpen en gemaakt in Nederland, met vijf jaar garantie op het armatuur."),
        ],
    },
    "galerij": {
        "kop": "Titan in de praktijk",
        "intro": "Verschillende uitvoeringen van hetzelfde armatuur, elk afgestemd op de tunnel waar het hangt.",
        "items": [
            ("2200K en 3000K naast elkaar", "Twee kleurtemperaturen in één tunnel",
             "Titan Tuscan Angle in polycarbonaat, IK10, met Dynadimmer 3A, in RVS. De warme en de neutrale lichtkleur zijn hier naast elkaar te zien.", "titan-tuscan-3000k"),
            ("Gebogen venster", "Afscherming die de wand volgt",
             "Een gebogen polycarbonaat afscherming in 2200K, dimbaar, langs een wand met mozaïek.", "tunnel-gebogen-a"),
            ("Antigraffiti", "Titan HE met 60°-optiek en coating",
             "In een onderdoorgang waar graffiti erbij hoort: IK10 en een antigraffiticoating op behuizing en venster.", "titan-antigraffiti"),
            ("Geartray", "Dimbare LED-geartray in 2200K",
             "Dezelfde LED-techniek als retrofit in een bestaand tunnelarmatuur, met Dynadimmer 3A.", "geartray-tunnel-2200k"),
        ],
    },
    "projecten": ["onderdoorgang-titan-2200k", "fietstunnel-titan-uhe-rvs", "tunnelverlichting-3000k-dimregime-3a"],
    "projecten_kop": "Tunnels met een Titan",
    "faq": [
        ("Wat betekent LTA bij het opalen venster?", [
            "LTA is de lichttransmissiewaarde: hoeveel van het licht door het venster heen naar buiten gaat. Bij ons opalen venster is dat 82%. Een opaal venster verdeelt het licht zachter en verbergt de LED-punten.",
        ]),
        ("Wat is het dimregime 3A van de Dynadimmer?", [
            "De Dynadimmer is een regelaar in het armatuur die het licht volgens een vast tijdschema terugregelt, zonder centrale sturing of bekabeling. 3A is het standaardregime dat in de Nederlandse openbare verlichting veel wordt gebruikt; een klantspecifiek regime kan ook.",
        ]),
        ("Kunnen jullie ook alleen de binnenkant vervangen?", [
            "Ja. Voor bestaande tunnelarmaturen maken we LED-geartrays: de behuizing blijft hangen, de techniek en eventueel het venster worden vernieuwd. Zie de pagina over retrofit.",
        ]),
    ],
    "contact_kop": "Een tunnel die om een eigen armatuur vraagt?",
    "ld": product_ld("Titan tunnelarmatuur",
                     "Tunnelarmatuur op klantspecificatie in RVS en polycarbonaat, IK10, 2200K tot 4000K, dimbaar via DALI, 1-10V of Dynadimmer.",
                     "verledden-geartray"),
})

# ============================================================= Paaltop
detailpagina({
    "bestand": "paaltop-armaturen.html",
    "namespace": "paaltop-armaturen",
    "titel": "Citylight paaltoparmatuur | De Licht Fabriek",
    "omschrijving": "Het Citylight paaltoparmatuur: slagvast polycarbonaat, efficiënte LED en aanpasbare optieken voor een gelijkmatige lichtspreiding op straat, plein en speelplaats. 2200K tot 4000K, dimbaar.",
    "service_type": "Paaltoparmaturen voor openbare verlichting",
    "eyebrow": "Armatuur · Citylight",
    "h1": "Citylight paaltop&shy;armatuur",
    "hero_foto": "citylight-2025",
    "volgorde": ["statement", "situaties", "specs", "aanpak", "voordelen", "galerij", "projecten", "faq", "slot"],
    "intro": '''          <p>De Citylight is een paaltoparmatuur voor straat, plein en speelplaats: een stille vorm die overdag niet opvalt en 's avonds gelijkmatig licht geeft op de plek waar mensen lopen.</p>
          <p>De behuizing is van duurzaam, slagvast polycarbonaat, de LED-module is efficiënt en de optiek kies je per situatie. Zo komt het licht op de weg of het plein terecht, en niet in de slaapkamer ernaast.</p>''',
    "situaties": {
        "kop": "Waar de Citylight op zijn plek is",
        "items": [
            ("Woonstraat en plein",
             "Een straat vraagt een langwerpige lichtverdeling, een plein een ronde. Met de optieken T2, T3 en T4 past de verdeling bij de plattegrond, zodat je minder masten nodig hebt voor hetzelfde lichtniveau."),
            ("Speelplaats en park",
             "Plekken waar kinderen spelen en waar een armatuur een bal of een stok te verduren krijgt. Polycarbonaat breekt niet zoals glas."),
            ("Nachtelijke rust",
             "Met een Dynadimmer of DALI dimt het armatuur 's nachts terug: minder verbruik en minder licht op de gevels als er toch niemand loopt."),
        ],
    },
    "specs": {
        "kop": "Wat je kunt kiezen",
        "items": [
            ("Behuizing", "Slagvast polycarbonaat", "Duurzaam en slagvast; het armatuur blijft heel waar glas breekt."),
            ("Optiek", "T2, T3 of T4", "Een reeks aanpasbare optieken voor een optimale, uniforme lichtspreiding op maat van de plek."),
            LEDKLEUR,
            STURING,
            ("Uitvoeringen", "Citylight en Citylight mini", "Hetzelfde armatuur in twee maten, voor een plein of een pad."),
            GARANTIE,
        ],
    },
    "aanpak": {
        "kop": "Van plattegrond tot mast",
        "intro": "De Citylight is een standaardarmatuur, maar de keuze van optiek, lichtkleur en sturing bepaalt of het licht komt waar het moet. Daar helpen we bij.",
        "label": "Jij levert",
        "stappen": [
            ("Plattegrond en wens", "Waar staan de masten, hoe hoog, en wat moet er verlicht worden? Met die gegevens kiezen we de optiek en het aantal armaturen.",
             "plattegrond of situatieschets, masthoogte"),
            ("Keuze van optiek, kleur en sturing", "T2, T3 of T4; 2200K, 3000K of 4000K; Aan/Uit, DALI, 1-10V of Dynadimmer. We leggen de keuze voor en lichten toe waarom.",
             "akkoord op de keuze"),
            ("Productie en levering", "De armaturen worden in Wormerveer gebouwd en ingeregeld op het gekozen dimregime.",
             ""),
        ],
    },
    "voordelen": {
        "kop": "Wat de Citylight oplevert",
        "items": [
            ("doel", "Licht waar het hoort", "De optiek legt het licht op straat of plein en houdt het van de gevels."),
            ("schild", "Breekt niet", "Slagvast polycarbonaat in plaats van glas: minder schade, minder vervangen."),
            ("maan", "Dimt in de nacht", "Dynadimmer of DALI regelt terug als er niemand loopt."),
            ("certificaat", "Vijf jaar garantie", "Ontworpen en gemaakt in Nederland, met vijf jaar garantie."),
        ],
    },
    "galerij": {
        "kop": "De Citylight van dichtbij",
        "items": [
            ("Werkplaats", "Citylight mini",
             "De kleine uitvoering, brandend in de werkplaats voordat hij de deur uitgaat.", "citylight-mini"),
            ("Ontwerp", "Citylight v2 in 3D",
             "Het armatuur wordt in 3D ontworpen en doorontwikkeld; dit is de tweede generatie.", "citylight-ontwerp"),
            ("Overdag", "Op een plein bij een school",
             "Een stille vorm die overdag niet om aandacht vraagt.", "citylight-plein"),
            ("Avond", "In de woonstraat",
             "Gelijkmatig licht op de rijbaan en het trottoir.", "citylight-straat"),
        ],
    },
    "projecten": ["citylight-beverwijk-wijkertoren", "citylight-speelplaats-en-straat"],
    "projecten_kop": "Waar de Citylight staat",
    "faq": [
        ("Welke optiek heb ik nodig?", [
            "Dat hangt af van de plattegrond en de masthoogte. Grofweg: T2 voor smalle paden, T3 voor straten, T4 voor bredere wegen en pleinen. Stuur een situatieschets, dan adviseren we.",
        ]),
        ("Kan de Citylight op bestaande masten?", [
            "De Citylight is een paaltoparmatuur en wordt op de mast geplaatst. Geef de mastdiameter door, dan kijken we of de bevestiging past of een adapter nodig is.",
        ]),
        ("Is het armatuur ook in een andere lichtkleur leverbaar?", [
            "Standaard zijn 2200K, 3000K en 4000K. Afwijkende kleuren leveren we op aanvraag.",
        ]),
    ],
    "contact_kop": "Een straat of plein dat beter licht verdient?",
    "ld": product_ld("Citylight paaltoparmatuur",
                     "Paaltoparmatuur in slagvast polycarbonaat met efficiënte LED en aanpasbare optieken (T2, T3, T4), 2200K tot 4000K, dimbaar.",
                     "citylight-2025"),
})

# ============================================================= Solarbolder
detailpagina({
    "bestand": "solarbolder.html",
    "namespace": "solarbolder",
    "titel": "Solarbolder: offgrid verlichting op zonne-energie | De Licht Fabriek",
    "omschrijving": "De Solarbolder is een offgrid staand armatuur dat 365 dagen per jaar licht geeft op alleen zon en daglicht. Ontwerp Atelier LEK, geproduceerd in Nederland in RVS en terrazzo.",
    "service_type": "Offgrid solar bolderverlichting",
    "eyebrow": "Armatuur · Offgrid",
    "h1": "Solarbolder",
    "hero_foto": "schielandhuis-entree-2",
    "volgorde": ["statement", "situaties", "voordelen", "specs", "aanpak", "galerij", "projecten", "faq", "slot"],
    "statement_knop": ("Vraag een prijsopgave", "contact.html"),
    "intro": '''          <p>De Solarbolder is een staand armatuur dat los van het elektriciteitsnet werkt. De enige voorziening die het nodig heeft is zon en daglicht; daarmee geeft het 365 dagen per jaar licht in de duisternis.</p>
          <p>Het ontwerp is van Iris Dijkstra van Atelier LEK. De Licht Fabriek heeft dat idee samen met Atelier LEK omgezet in een duurzaam gefabriceerde bolder: roestvast staal, terrazzo en duurzame elektronica, geproduceerd in Nederland.</p>''',
    "situaties": {
        "kop": "Waar een Solarbolder het verschil maakt",
        "items": [
            ("Geen kabel in de grond",
             "Een tuin, een parkpad, een plek bij een monument: overal waar graven duur, ongewenst of onmogelijk is. De bolder staat op zichzelf."),
            ("Een plek die om ontwerp vraagt",
             "RVS met poedercoat en een reflector van terrazzo of azobé. Een armatuur dat overdag een object is en 's avonds licht."),
            ("Licht met zo min mogelijk impact",
             "Geen netaansluiting, geen verbruik van het net. In amber, dat minder insecten aantrekt, voor het buitengebied."),
        ],
    },
    "voordelen": {
        "kop": "Wat de Solarbolder oplevert",
        "items": [
            ("zon", "Alleen zon en daglicht", "Het zonnepaneel in het bovenvlak laadt overdag; 's nachts brandt de bolder."),
            ("stekker", "Geen netaansluiting", "Geen graafwerk, geen kabels, geen aansluitkosten."),
            ("klok", "365 dagen per jaar", "Ontworpen om het hele jaar door licht te geven in de duisternis."),
            ("pin", "Made in Holland", "Geproduceerd in Nederland, in RVS, terrazzo en duurzame elektronica."),
        ],
    },
    "specs": {
        "kop": "Uitvoeringen",
        "intro": "De Solarbolder is in verschillende materialen en lichtkleuren gemaakt. Dit zijn de uitvoeringen uit onze projecten.",
        "items": [
            ("Energie", "Zon en daglicht", "Offgrid: het zonnepaneel zit in het bovenvlak van de bolder. Geen aansluiting op het net."),
            ("Behuizing", "RVS met poedercoat", "Roestvast staal, gepoedercoat in de gewenste kleur."),
            ("Reflector", "Terrazzo of azobé", "Wit carrara-terrazzo voor een lichte, stedelijke uitstraling of azobé-hardhout voor het buitengebied."),
            ("Lichtkleur", "3000K of amber", "Warmwit voor tuin en park; amber waar insecten en nachtdieren ontzien moeten worden."),
            ("Ontwerp", "Iris Dijkstra, Atelier LEK", "Bedacht en ontworpen door Atelier LEK, samen met De Licht Fabriek uitgewerkt tot een produceerbaar armatuur."),
            ("Productie", "Nederland", "Gemaakt in Nederland van hoogwaardige materialen en duurzame elektronica."),
        ],
    },
    "aanpak": {
        "kop": "Van plek tot brandende bolder",
        "intro": "Een Solarbolder vraagt geen installatie van kabels, wel een goede plek: genoeg daglicht op het paneel en een stevige ondergrond.",
        "label": "Jij levert",
        "stappen": [
            ("Plek en wens", "Waar komt de bolder, hoeveel daglicht valt er, en welke uitvoering past bij de plek: terrazzo of azobé, 3000K of amber.",
             "situatieschets of foto's van de plek"),
            ("Uitvoering vastleggen", "We stellen de uitvoering en het aantal voor en maken een prijsopgave.",
             "akkoord op uitvoering en aantal"),
            ("Productie en plaatsing", "De bolders worden in Nederland geproduceerd en op de plek gezet. Daarna doet de zon de rest.",
             "toegang tot de locatie"),
        ],
    },
    "galerij": {
        "kop": "De Solarbolder van dichtbij",
        "items": [
            ("Reflector", "Wit carrara-terrazzo",
             "De reflector verdeelt het licht naar beneden en is overdag het gezicht van de bolder.", "schielandhuis-reflector-detail"),
            ("Zonnepaneel", "In het bovenvlak",
             "Het paneel zit verzonken in de RVS-behuizing met poedercoat.", "solarbolder-zonnepaneel"),
            ("Amber", "Azobé en amber LED",
             "De uitvoering voor het buitengebied, hier in de avondschemer bij een weiland.", "solarbolder-amber"),
            ("Park", "Langs een parkpad",
             "Solarbolders tussen de bomen in Crooswijk, Rotterdam.", "solarbolder-crooswijk-2"),
        ],
    },
    "projecten": ["solarbolder-schielandhuis-rotterdam", "solarbolder-crooswijk-rotterdam", "solarbolder-amber-azobe"],
    "projecten_kop": "Waar de Solarbolder staat",
    "faq": [
        ("Brandt de Solarbolder ook in de winter?", [
            "De Solarbolder is ontworpen om 365 dagen per jaar licht te geven op zon en daglicht. Hoeveel daglicht er op de plek valt, bepaalt wel of een plek geschikt is; dat bekijken we vooraf.",
        ]),
        ("Is er een netaansluiting nodig?", [
            "Nee. Het zonnepaneel zit in het bovenvlak van de bolder en de elektronica zit erin. Er hoeft geen kabel in de grond.",
        ]),
        ("Wie heeft de Solarbolder ontworpen?", [
            "Iris Dijkstra van Atelier LEK. De Licht Fabriek heeft het ontwerp samen met Atelier LEK omgezet in een duurzaam gefabriceerde bolder die in Nederland wordt geproduceerd.",
        ]),
    ],
    "contact_kop": "Een plek zonder kabel die licht nodig heeft?",
    "ld": product_ld("Solarbolder",
                     "Offgrid staand armatuur op zon en daglicht, 365 dagen per jaar licht. Ontwerp Atelier LEK; RVS, terrazzo en duurzame elektronica, geproduceerd in Nederland.",
                     "schielandhuis-entree-2"),
})
