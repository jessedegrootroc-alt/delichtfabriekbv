# -*- coding: utf-8 -*-
"""De inhoud van de drie dienstpagina's. Het skelet staat in bouw_detail.py.
   Feiten: delichtfabriekbv.nl (geartray-tunnelarmatuur, retrofit-menu,
   thermolight, paginatitel met 'Ontwerp, Engineering, Productie, installatie,
   retrofit oplossingen, Custom made oplossingen') en de projectfoto's."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bouw_detail import detailpagina

# ================================================================= Retrofit
detailpagina({
    "bestand": "retrofit.html",
    "namespace": "retrofit",
    "titel": "Retrofit en LED-geartrays | De Licht Fabriek",
    "omschrijving": "LED-geartrays voor bestaande armaturen: tunnelarmaturen, Schréder Valentino en Albany, TL en CDO naar LED. De behuizing blijft, de techniek wordt nieuw.",
    "service_type": "Retrofit van bestaande verlichting naar LED",
    "eyebrow": "Dienst · Retrofit",
    "h1": "Bestaande armaturen verledden",
    "hero_foto": "retrofit-module",
    "volgorde": ["statement", "situaties", "beeldtekst", "aanpak", "specs", "voordelen", "galerij", "projecten", "faq", "slot"],
    "statement_knop": ("Vraag een prijsopgave", "contact.html"),
    "intro": '''          <p>Een armatuur dat nog goed aan de wand of op de mast zit, hoeft niet weg omdat de lamp erin verouderd is. Met een LED-geartray vervangen we alleen de binnenkant: de LED-module, de driver en waar nodig de optiek en het venster. De behuizing blijft.</p>
          <p>Dat is de naadloze samensmelting van nieuwe, efficiënte hardware met slimme sturing: een module tot 200 lumen per watt en een driver die dimt zoals jij wilt, in een armatuur dat je al hebt.</p>''',
    "situaties": {
        "kop": "Wanneer retrofit de betere keuze is",
        "items": [
            ("TL in bestaande armaturen",
             "Tunnels, stations en gebouwen vol TL. De buizen gaan eruit, een LED-module komt erin, desgewenst met noodverlichting en DALI-dimming."),
            ("Gasontladingslampen op de mast",
             "Straatarmaturen met een CDO-lamp van 70W vervangen we door een LED-module van 22W met T3-optiek. Het armatuur blijft hangen."),
            ("Tunnelarmaturen met oude techniek",
             "Voor tunnelarmaturen en voor de Schréder Valentino en Albany maken we passende geartrays, met een nieuw venster als dat nodig is."),
        ],
    },
    "beeldtekst": {
        "ident": "verschil",
        "kop": "Oude TL eruit, LED-module erin",
        "tekst": '''            <p>Op de werkbank is het verschil klein: een buis naast een module. In het armatuur is het groot. De LED-module levert tot 200 lumen per watt, de driver regelt het licht terug op de uren dat er niemand is, en het venster laat weer door wat het moet doorlaten.</p>
            <p>We meten het bestaande armatuur in en engineeren de geartray daarop. Zo past hij zonder aanpassingen aan de behuizing.</p>''',
        "foto": "tl-vs-led",
        "knop": ("Bespreek je armaturen", "contact.html"),
    },
    "aanpak": {
        "kop": "Van bestaand armatuur tot nieuwe geartray",
        "intro": "Retrofit begint bij wat er hangt. Daarom willen we eerst het armatuur zien, of een exemplaar in handen hebben.",
        "label": "Jij levert",
        "stappen": [
            ("Inmeten van het armatuur", "Type, maten, bevestiging, voeding en de staat van het venster. Een exemplaar in onze werkplaats werkt het best; foto's en tekeningen kunnen ook.",
             "een armatuur of foto's en maten"),
            ("Geartray engineeren", "LED-module, optiek en driver worden op het armatuur en op de lichtwens afgestemd: lichtkleur, vermogen, dimregime, eventueel noodverlichting.",
             "lichtwens en sturing (DALI, 1-10V, Dynadimmer)"),
            ("Productie en proefmontage", "De geartrays worden in Wormerveer gemaakt en in een armatuur geprobeerd voordat de serie wordt gemaakt.",
             ""),
            ("Ombouw op locatie of in de werkplaats", "De oude techniek gaat eruit, de geartray erin, het venster wordt waar nodig vernieuwd.",
             "toegang tot de armaturen"),
        ],
    },
    "specs": {
        "kop": "Waarvoor we geartrays maken",
        "intro": "De uitvoeringen die er al zijn. Een ander armatuur? Stuur het type door.",
        "items": [
            ("Tunnel", "Geartray tunnelarmatuur", "Voor bestaande tunnelarmaturen, met nieuw polycarbonaat venster als het bestaande vervangen moet worden."),
            ("Schréder", "Geartray Valentino", "Passend in het Schréder Valentino-armatuur."),
            ("Schréder", "Geartray Albany", "Passend in het Schréder Albany-armatuur."),
            ("Straat", "CDO naar LED", "Van een CDO-lamp van 70W naar een LED-module van 22W met T3-optiek en Dynadimmer."),
            ("Binnen en tunnel", "TL naar LED", "LED-modules in plaats van TL, ook met noodverlichting en DALI-dimming."),
            ("Op maat", "Custom LED-module", "Een LED-module in een buis of op een eigen drager, 3000K, 180 lumen per watt."),
        ],
    },
    "voordelen": {
        "kop": "Wat verledden oplevert",
        "items": [
            ("recycle", "De behuizing blijft", "Geen nieuw armatuur, geen afval van het oude: alleen de techniek wordt vernieuwd. Circulair gedacht."),
            ("bliksem", "Tot 200 lumen per watt", "Minder vermogen voor hetzelfde licht; van 70W CDO naar 22W LED in de straat."),
            ("schuif", "Dimt in de nacht", "Dynadimmer met regime 3A of DALI: het licht gaat terug als er niemand is."),
            ("lagen", "Nieuw venster als dat nodig is", "Een vergeeld of beschadigd venster vervangen we in polycarbonaat, met antigraffiticoating."),
        ],
    },
    "galerij": {
        "kop": "Retrofit in beeld",
        "items": [
            ("Engineering", "Vervangende geartray in 3D",
             "Een geartray voor het DP Tuscan-armatuur: 4000 lumen bij 22W in 3000K.", "geartray-ontwerp"),
            ("Tunnel", "Dimbare geartray in 2200K",
             "LED-geartray met Dynadimmer 3A in een bestaand tunnelarmatuur.", "geartray-tunnel-2200k"),
            ("Tunnel", "Nieuwe geartray en venster in 3000K",
             "Een lange fietstunnel na het verledden, met nieuw polycarbonaat venster.", "verledden-geartray"),
            ("Onderdoorgang", "Upgrade naar 2200K",
             "Bestaande armaturen met een nieuwe geartray en een nieuw venster.", "tunnel-2e-keus"),
        ],
    },
    "projecten": ["retrofit-straatverlichting-2200k", "schreder-cdo-naar-led-2200k", "tl-naar-led-met-noodverlichting"],
    "projecten_kop": "Verled in de praktijk",
    "faq": [
        ("Past een geartray in elk armatuur?", [
            "In veel armaturen wel, maar niet in alle. Daarom meten we het bestaande armatuur eerst in. Voor tunnelarmaturen en de Schréder Valentino en Albany hebben we al passende geartrays.",
        ]),
        ("Kan het dimregime hetzelfde blijven als nu?", [
            "Ja. De geartray krijgt de driver die bij je sturing past: Aan/Uit, DALI of DALI SR, 1-10V, of een Dynadimmer met het standaard 3A-regime of een eigen regime.",
        ]),
        ("Wat als het venster vergeeld of beschadigd is?", [
            "Dan vervangen we het venster in polycarbonaat, desgewenst met antigraffiticoating. Dat gebeurt in dezelfde ombouw.",
        ]),
    ],
    "contact_kop": "Armaturen die aan nieuwe techniek toe zijn?",
})

# ================================================================= Maatwerk
detailpagina({
    "bestand": "maatwerk.html",
    "namespace": "maatwerk",
    "titel": "Maatwerk en engineering | De Licht Fabriek",
    "omschrijving": "Verlichting op maat voor bruggen, trappen, kunstwerken en bijzondere objecten: ontwerp, engineering, productie en installatie in eigen huis, ook op lage spanning.",
    "service_type": "Maatwerk verlichting: ontwerp, engineering, productie en installatie",
    "eyebrow": "Dienst · Maatwerk",
    "h1": "Maatwerk en engineering",
    "hero_foto": "cruijff",
    "hero_positie": "center 40%",
    "volgorde": ["statement", "situaties", "aanpak", "galerij", "voordelen", "projecten", "faq", "slot"],
    "intro": '''          <p>Een brugleuning, een trap in het groen, een standbeeld, een lichtbak voor een restauratieatelier: voor sommige plekken bestaat geen armatuur. Dan ontwerpen, engineeren en produceren we er een.</p>
          <p>Alles gebeurt in eigen huis in Wormerveer. De klantwens wordt vertaald naar een passende oplossing, en onze interne engineering en productie waarborgen de kwaliteit. Waar het moet werken we op extra lage spanning (48V of 54V DC), zodat de installatie veilig in de openbare ruimte kan staan.</p>''',
    "situaties": {
        "kop": "Wanneer maatwerk nodig is",
        "items": [
            ("Het object is het armatuur",
             "Verlichting in een brugleuning of een trapleuning, grondspots in een trap: het licht hoort bij het object en moet erin passen, niet erop."),
            ("Extra lage spanning gewenst",
             "Op plekken waar mensen het armatuur kunnen aanraken, werken we op 48V of 54V DC. Dat vraagt eigen engineering van voeding en module."),
            ("Een bijzondere functie",
             "Het aanlichten van een standbeeld, een UV-A lichtbak om vergeelde kunstwerken te herstellen, noodverlichting in een stationstunnel: licht als gereedschap."),
        ],
    },
    "aanpak": {
        "kop": "Ontwerp, engineering, productie, installatie",
        "intro": "Vier stappen, één adres. Omdat er geen schakel tussen zit, kan een ontwerp onderweg nog aangepast worden zonder dat de planning omvalt.",
        "label": "Jij levert",
        "stappen": [
            ("Ontwerp", "We vertalen de wens en de plek naar een lichtontwerp: waar komt het licht, hoeveel, in welke kleur, en hoe zit het in het object. Met een eigen lichtontwerper of architect werken we graag samen.",
             "de vraag, de plek en eventuele ontwerpuitgangspunten"),
            ("Engineering", "Module, optiek, driver, voeding en behuizing worden uitgewerkt in 3D en op tekening gezet, inclusief de spanning (netspanning of ELV) en de slagvastheid.",
             "akkoord op tekening"),
            ("Productie", "In onze werkplaats in Wormerveer: behuizing, montage van module en driver, proefopstelling.",
             ""),
            ("Installatie", "We plaatsen het armatuur en regelen het in. Ook herstel van bestaande bijzondere verlichting, zoals de trap- en brugverlichting bij het Muziekgebouw aan het IJ, hoort hierbij.",
             "toegang tot de locatie en de voeding"),
        ],
    },
    "galerij": {
        "kop": "Maatwerk in beeld",
        "items": [
            ("Trap", "Grondspots en leuningverlichting",
             "360°-grondspots in de treden en licht in de leuning, op 48V.", "trapopgang-grondspots"),
            ("Atelier", "UV-A lichtbak",
             "Op maat gebouwd om vergeling van kunstwerken te herstellen.", "uv-lichtbak"),
            ("Station", "LED met noodverlichting",
             "TL vervangen door dimbare LED met noodverlichting achter polycarbonaat.", "noodverlichting"),
            ("Ontwerp", "In 3D uitgewerkt",
             "Elk armatuur wordt in 3D ontworpen voordat er iets gemaakt wordt.", "citylight-ontwerp"),
        ],
    },
    "voordelen": {
        "kop": "Wat maatwerk in eigen huis oplevert",
        "items": [
            ("liniaal", "Past in het object", "Het armatuur volgt de leuning, de trede of de sparing; niet andersom."),
            ("slot", "Veilig op lage spanning", "48V of 54V DC waar mensen het armatuur kunnen aanraken."),
            ("hand", "Eén aanspreekpunt", "Ontwerp, engineering, productie en installatie bij dezelfde mensen."),
            ("certificaat", "Vijf jaar garantie", "Ook op maatwerk: ontworpen en gemaakt in Nederland."),
        ],
    },
    "projecten": ["brug-buikslotermeer-amsterdam", "brugverlichting-hoofddorp", "muziekgebouw-bimhuis-amsterdam"],
    "projecten_kop": "Maatwerk in de praktijk",
    "faq": [
        ("Werken jullie samen met onze lichtontwerper of architect?", [
            "Ja. De Solarbolder is zo ontstaan: een ontwerp van Atelier LEK dat wij produceerbaar hebben gemaakt. Een ontwerp van buiten werken we uit tot een armatuur dat te maken en te onderhouden is.",
        ]),
        ("Waarom extra lage spanning?", [
            "Op bruggen, trappen en leuningen kunnen mensen de verlichting aanraken. Met 48V of 54V gelijkspanning is de installatie veilig, ook als er iets beschadigd raakt.",
        ]),
        ("Herstellen jullie ook bestaande bijzondere verlichting?", [
            "Ja. Bij het Muziekgebouw aan het IJ en het BIMhuis in Amsterdam hebben we de trap- en brugverlichting hersteld in plaats van vervangen.",
        ]),
    ],
    "contact_kop": "Een plek waar geen standaardarmatuur past?",
})

# ================================================================ Thermolight
detailpagina({
    "bestand": "thermolight.html",
    "namespace": "thermolight",
    "titel": "Thermolight: thermografisch onderzoek | De Licht Fabriek",
    "omschrijving": "Thermografisch onderzoek maakt afwijkingen in elektrische installaties en warmteproblemen snel zichtbaar. Vraag informatie of een prijsopgave aan.",
    "service_type": "Thermografisch onderzoek",
    "eyebrow": "Dienst · Thermolight",
    "h1": "Thermo&shy;grafisch onderzoek",
    "hero_foto": "thermo-radiator",
    "volgorde": ["statement", "situaties", "aanpak", "voordelen", "galerij", "faq", "slot"],
    "statement_knop": ("Vraag een prijsopgave", "contact.html"),
    "intro": '''          <p>Met thermografisch onderzoek constateren we snel en vakkundig afwijkingen. Dat kan gaan om elektrische problemen, zoals een aansluiting die te warm wordt, en om warmtegerelateerde problemen, zoals een radiator of installatie die niet doet wat hij moet doen.</p>
          <p>Onder de naam Thermolight bieden we dat onderzoek aan: een warmtebeeldopname op locatie, een beoordeling van wat erop te zien is en de beelden erbij. Neem contact op voor aanvullende informatie of een prijsopgave.</p>''',
    "situaties": {
        "kop": "Waar een warmtebeeld iets laat zien",
        "items": [
            ("Elektrische installaties",
             "Een aansluiting of klem die te warm wordt, een zekering die meer te verduren krijgt dan de rest: op een warmtebeeld licht het op voordat het uitvalt."),
            ("Verwarming en warmteverlies",
             "Een radiator die maar half warm wordt, een leiding die warmte verliest waar dat niet hoort."),
            ("Machines en motoren",
             "Lagers, motoren en aandrijvingen die warmer lopen dan hun buren, als eerste teken van slijtage."),
        ],
    },
    "aanpak": {
        "kop": "Zo verloopt een onderzoek",
        "intro": "Een thermografisch onderzoek is contactloos: de installatie blijft in bedrijf terwijl we meten.",
        "label": "Jij levert",
        "stappen": [
            ("Vraag en afspraak", "Wat wil je weten en waarover: een verdeelkast, een verwarmingsinstallatie, een machine. Op basis daarvan maken we een prijsopgave en plannen we een moment waarop de installatie in bedrijf is.",
             "de vraag en toegang tot de installatie"),
            ("Opname op locatie", "We maken de warmtebeeldopnamen en, ter vergelijking, gewone foto's van dezelfde plekken.",
             ""),
            ("Beoordeling en beelden", "Je krijgt de beelden met onze beoordeling van de afwijkingen die erop te zien zijn.",
             ""),
        ],
    },
    "voordelen": {
        "kop": "Wat thermografie oplevert",
        "items": [
            ("oog", "Zichtbaar wat je niet voelt", "Een warm punt in een kast of een koud vlak op een radiator is op het beeld meteen te zien."),
            ("klok", "Snel", "Een opname kost weinig tijd en de installatie hoeft er niet voor uit."),
            ("thermometer", "Zonder aanraken", "Contactloos meten, ook aan onderdelen die onder spanning staan."),
            ("lijst", "Beelden erbij", "Je krijgt de warmtebeelden met de gewone foto's ernaast, zodat je weet waar je moet zijn."),
        ],
    },
    "galerij": {
        "kop": "Voorbeelden van opnamen",
        "intro": "Een paar warmtebeelden uit onze praktijk: wat je op het beeld ziet, en waar het op wijst.",
        "kolommen": 3,
        "items": [
            ("Elektrisch", "Opwarmende aansluiting",
             "Een klem die duidelijk warmer is dan de aders ernaast: een losse of overbelaste verbinding.", "thermo-connector"),
            ("Schakelkast", "Warmtebeeld naast foto",
             "Dezelfde kast op het warmtebeeld en op de gewone foto, zodat de afwijking te herleiden is.", "thermo-kast"),
            ("Machine", "Motor in bedrijf",
             "Een elektromotor tijdens het draaien; de warmste delen springen eruit.", "thermo-motor"),
        ],
    },
    "faq": [
        ("Moet de installatie uit tijdens het onderzoek?", [
            "Nee, juist niet. Thermografie laat zien wat er gebeurt als de installatie werkt. We meten contactloos, dus de installatie blijft in bedrijf.",
        ]),
        ("Wat krijg ik na afloop?", [
            "De warmtebeelden met onze beoordeling van de afwijkingen, met gewone foto's van dezelfde plekken ernaast.",
        ]),
        ("Wat kost een thermografisch onderzoek?", [
            "Dat hangt af van de omvang: één verdeelkast is iets anders dan een complete installatie. Neem contact op voor een prijsopgave.",
        ]),
    ],
    "contact_kop": "Weten waar het warm wordt?",
    "contact_tekst": "Vertel kort om welke installatie het gaat. We maken een prijsopgave voor het onderzoek.",
})
