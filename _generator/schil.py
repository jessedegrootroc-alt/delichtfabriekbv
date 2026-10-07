# -*- coding: utf-8 -*-
import pathlib, json
"""
Gedeelde paginaschil voor de site van De Licht Fabriek B.V.

Dit script schrijft platte HTML-bestanden weg. De site zelf heeft geen build-stap:
wat hier uitkomt is gewone HTML die je met een statische server serveert. Dit
bestand is gereedschap om alle pagina's identiek te houden terwijl ze gebouwd
worden.

Alle bedrijfsfeiten hieronder komen van https://www.delichtfabriekbv.nl/
(opgehaald 7 oktober 2026); zie work/migration-state.md voor de bron per feit.
"""

HIER = pathlib.Path(__file__).parent
UIT = HIER.parent

# Het domein van de bestaande site. Canonical, Open Graph, sitemap en robots
# verwijzen hierheen; staat de nieuwe site tijdelijk op een ander adres, zet
# dat dan hier en bouw opnieuw.
BASIS = "https://www.delichtfabriekbv.nl"

BEDRIJF = "De Licht Fabriek"
BEDRIJF_JURIDISCH = "De Licht Fabriek B.V."

# ------------------------------------------------------------ contactgegevens
TELEFOON_WEERGAVE = "06 28553641"
TELEFOON_LINK = "+31628553641"
EMAIL = "info@delichtfabriekbv.nl"
STRAAT = "Rosbayerweg 19"
POSTCODE = "1522 RW"
PLAATS = "Wormerveer"
ADRES = f"{STRAAT}, {POSTCODE} {PLAATS}"
KVK = "72963204"
BTW = "NL859301655B01"
GARANTIE = "5 jaar"

# ------------------------------------------------------------------ aanbod
# (bestand, titel, ondertitel, fotosleutel) -- gebruikt in het menu, de voet,
# de overzichten en de kaarten op de homepage.
ARMATUREN = [
    ("solarbolder.html", "Solarbolder", "Offgrid licht, 365 dagen per jaar", "schielandhuis-bolder"),
    ("tunnelarmaturen.html", "Tunnel&shy;armaturen", "Titan: op maat, in RVS en polycarbonaat", "tunnel-3000k"),
    ("paaltop-armaturen.html", "Paaltop-armaturen", "Citylight: slagvast en gelijkmatig licht", "citylight-straat"),
]
DIENSTEN = [
    ("retrofit.html", "Retrofit en LED-geartrays", "Bestaande armaturen verledden", "tl-vs-led"),
    ("maatwerk.html", "Maatwerk en engineering", "Van vraag tot armatuur, in eigen huis", "trapopgang-grondspots"),
    ("thermolight.html", "Thermografisch onderzoek", "Afwijkingen snel in beeld", "thermo-radiator"),
]

# Filters op het projectenoverzicht. Sleutel -> label.
TOEPASSINGEN = {
    "tunnel": "Tunnels en onderdoorgangen",
    "brug": "Bruggen en trappen",
    "straat": "Straat en plein",
    "solar": "Offgrid solar",
    "retrofit": "Retrofit",
    "bijzonder": "Bijzondere objecten",
}
PRODUCTEN = {
    "titan": ("Titan tunnelarmatuur", "tunnelarmaturen.html"),
    "citylight": ("Citylight paaltoparmatuur", "paaltop-armaturen.html"),
    "solarbolder": ("Solarbolder", "solarbolder.html"),
    "geartray": ("LED-geartray / retrofit", "retrofit.html"),
    "maatwerk": ("Maatwerk", "maatwerk.html"),
}

# ---------------------------------------------------------------- projecten
# Alles hieronder is afgeleid van de projectfoto's en hun bijschriften op de
# bronsite (portfolio en productpagina's). Waar een locatie of een getal niet
# op de bron staat, staat hij hier ook niet. Geen uitdagingen, resultaten of
# cijfers die niet uit de bron komen.
#
# Velden: slug, titel, plaats (of None), toepassing, product, beeld (hero),
# beelden (extra foto's over de volle breedte), kenmerken [(label, waarde,
# eenheid)], kort (kaarttekst), inleiding (alinea's), punten (wat is toegepast),
# verwant (slugs).
PROJECTEN = [
    {
        "slug": "onderdoorgang-titan-2200k",
        "titel": "Onderdoorgang met Titan HE in 2200K",
        "plaats": None,
        "toepassing": "tunnel", "product": "titan",
        "beeld": "hero-tunnel-titan", "beelden": ["titan-antigraffiti"],
        "kenmerken": [("Lichtkleur", "2200", "K"), ("Optiek", "60", "graden"), ("Slagvastheid", "IK10", ""), ("Uitvoering", "HE", "high efficiency")],
        "kort": "Titan-armaturen met 60°-optiek en antigraffiticoating in een onderdoorgang over het water, in warmwit 2200K.",
        "inleiding": [
            "Een onderdoorgang vol graffiti, met water eronder en een laag plafond. De Titan HE (high efficiency) is hier geplaatst in 2200K: warmwit licht dat de wanden en het wateroppervlak gelijkmatig oplicht zonder te verblinden.",
        ],
        "punten": [
            "Titan-tunnelarmaturen in de uitvoering HE, met een optiek van 60 graden.",
            "Lichtkleur 2200K.",
            "Slagvastheidsklasse IK10 en antigraffiticoating op behuizing en venster.",
        ],
        "verwant": ["fietstunnel-titan-uhe-rvs", "tunnelverlichting-3000k-dimregime-3a"],
    },
    {
        "slug": "fietstunnel-titan-uhe-rvs",
        "titel": "Fietstunnel met Titan UHE in roestvast staal",
        "plaats": None,
        "toepassing": "tunnel", "product": "titan",
        "beeld": "titan-uhe", "beelden": [],
        "kenmerken": [("Type", "DLF13-60-22", ""), ("Lichtkleur", "2200", "K"), ("Optiek", "60", "graden"), ("Slagvastheid", "IK10", "")],
        "kort": "Titan DLF13-60-22 in RVS, de UHE-uitvoering (ultra high efficiency), in een fietstunnel bij nacht.",
        "inleiding": [
            "Fietstunnel onder een drukke weg, bij nacht. De armaturen zijn Titan DLF13-60-22 in roestvast staal, de uitvoering UHE (ultra high efficiency), met een lichtkleur van 2200K en een optiek van 60 graden.",
        ],
        "punten": [
            "Titan-tunnelarmatuur type DLF13-60-22 in roestvast staal.",
            "Uitvoering UHE, lichtkleur 2200K, optiek 60 graden.",
            "Slagvastheidsklasse IK10.",
        ],
        "verwant": ["onderdoorgang-titan-2200k", "verledden-tunnel-geartray-22w"],
    },
    {
        "slug": "tunnelverlichting-3000k-dimregime-3a",
        "titel": "Tunnelverlichting in 3000K met dimregime 3A",
        "plaats": None,
        "toepassing": "tunnel", "product": "titan",
        "beeld": "tunnel-3000k", "beelden": [],
        "kenmerken": [("Lichtkleur", "3000", "K"), ("Dimregime", "3A", "Dynadimmer"), ("Venster", "PC", "polycarbonaat"), ("Slagvastheid", "IK10", "")],
        "kort": "Fietstunnel in de schemering met tunnelarmaturen in polycarbonaat, antigraffiticoating en een Dynadimmer met dimregime 3A.",
        "inleiding": [
            "Een fietstunnel onder de weg, gefotografeerd in de schemering als de verlichting net aan is. De armaturen hebben een polycarbonaat venster met antigraffiticoating en een Dynadimmer die 's nachts volgens dimregime 3A terugregelt.",
        ],
        "punten": [
            "Tunnelarmaturen met lichtkleur 3000K.",
            "Polycarbonaat venster en antigraffiticoating, slagvastheidsklasse IK10.",
            "Dynadimmer met het standaard dimregime 3A.",
        ],
        "verwant": ["onderdoorgang-titan-2200k", "gebogen-polycarbonaat-afscherming-2200k"],
    },
    {
        "slug": "verledden-tunnel-geartray-22w",
        "titel": "Tunnelarmaturen verled met een geartray van 22W",
        "plaats": None,
        "toepassing": "retrofit", "product": "geartray",
        "beeld": "verledden-tunnel", "beelden": ["verledden-geartray"],
        "kenmerken": [("Vermogen", "22", "W"), ("Lichtkleur", "3000", "K"), ("Dimregime", "3A", "Dynadimmer"), ("Venster", "PC", "nieuw polycarbonaat")],
        "kort": "Bestaande tunnelarmaturen omgebouwd naar LED met een high-efficiency geartray van 22W en een nieuw polycarbonaat venster.",
        "inleiding": [
            "De bestaande armaturen in deze tunnels zijn niet vervangen maar verled: de oude techniek is eruit, een LED-geartray van 22W met Dynadimmer is erin, en het venster is vernieuwd in polycarbonaat. De behuizing bleef hangen.",
        ],
        "punten": [
            "LED-geartray high efficiency, 22W, lichtkleur 3000K.",
            "Dynadimmer met dimregime 3A.",
            "Nieuw venster in polycarbonaat in het bestaande armatuur.",
        ],
        "verwant": ["tunnel-upgrade-2200k-nieuw-venster", "fietstunnel-titan-uhe-rvs"],
    },
    {
        "slug": "tunnel-upgrade-2200k-nieuw-venster",
        "titel": "Tunnel-upgrade naar LED in 2200K met nieuw venster",
        "plaats": None,
        "toepassing": "retrofit", "product": "geartray",
        "beeld": "tunnel-2e-keus", "beelden": ["geartray-tunnel-2200k"],
        "kenmerken": [("Lichtkleur", "2200", "K"), ("Dimregime", "3A", "Dynadimmer"), ("Venster", "nieuw", ""), ("Behuizing", "bestaand", "hergebruikt")],
        "kort": "Onderdoorgang met wandschilderingen: de verlichting is naar LED gebracht in 2200K, dimbaar, met een nieuw venster in de bestaande armaturen.",
        "inleiding": [
            "Een onderdoorgang met wandschilderingen waar de verlichting aan vervanging toe was. In plaats van nieuwe armaturen kregen de bestaande een LED-geartray in 2200K, een Dynadimmer en een nieuw venster.",
        ],
        "punten": [
            "LED-geartray in de bestaande tunnelarmaturen, lichtkleur 2200K.",
            "Dimbaar met Dynadimmer, dimregime 3A.",
            "Nieuw venster; de behuizing is hergebruikt.",
        ],
        "verwant": ["verledden-tunnel-geartray-22w", "gebogen-polycarbonaat-afscherming-2200k"],
    },
    {
        "slug": "gebogen-polycarbonaat-afscherming-2200k",
        "titel": "Tunnel met gebogen polycarbonaat afscherming",
        "plaats": None,
        "toepassing": "tunnel", "product": "titan",
        "beeld": "tunnel-gebogen-b", "beelden": ["tunnel-gebogen-a"],
        "kenmerken": [("Lichtkleur", "2200", "K"), ("Dimregime", "3A", "Dynadimmer"), ("Afscherming", "gebogen", "polycarbonaat"), ("Slagvastheid", "IK10", "")],
        "kort": "Tunnelarmaturen met een gebogen polycarbonaat afscherming, dimbaar, in 2200K, langs een wand met mozaïek.",
        "inleiding": [
            "Hier is gekozen voor een gebogen polycarbonaat afscherming die de wand volgt. De armaturen geven 2200K en dimmen 's nachts terug met een Dynadimmer op regime 3A.",
        ],
        "punten": [
            "Gebogen polycarbonaat afscherming, slagvastheidsklasse IK10.",
            "Lichtkleur 2200K, dimbaar met Dynadimmer (3A).",
        ],
        "verwant": ["tunnelverlichting-3000k-dimregime-3a", "onderdoorgang-titan-2200k"],
    },
    {
        "slug": "brug-buikslotermeer-amsterdam",
        "titel": "Brug met trapopgang in 48V, Buikslotermeer",
        "plaats": "Amsterdam",
        "toepassing": "brug", "product": "maatwerk",
        "beeld": "brug-buikslotermeer", "beelden": [],
        "kenmerken": [("Spanning", "48", "V ELV"), ("Plaats", "Amsterdam", "Buikslotermeer"), ("Toepassing", "brug", "met trapopgang")],
        "kort": "Leuningverlichting op een houten brug met trapopgang in Amsterdam-Noord, uitgevoerd op 48V extra lage spanning.",
        "inleiding": [
            "Een houten voetgangersbrug met trapopgang in Buikslotermeer, Amsterdam. De verlichting zit in de leuning en werkt op 48V extra lage spanning (ELV), zodat de installatie veilig in de openbare ruimte kan staan.",
        ],
        "punten": [
            "Leuningverlichting op maat voor brug en trapopgang.",
            "Extra lage spanning: 48V ELV.",
        ],
        "verwant": ["brugverlichting-hoofddorp", "trapopgang-grondspots-leuningverlichting"],
    },
    {
        "slug": "trapopgang-grondspots-leuningverlichting",
        "titel": "Trapopgang met 360°-grondspots en leuningverlichting",
        "plaats": None,
        "toepassing": "brug", "product": "maatwerk",
        "beeld": "trapopgang-grondspots", "beelden": [],
        "kenmerken": [("Spanning", "48", "V ELV"), ("Grondspots", "360", "graden"), ("Slagvastheid", "IK10", "")],
        "kort": "Trap in het groen met rondom stralende grondspots en verlichting in de leuning, op 48V.",
        "inleiding": [
            "Een trap tussen de struiken, bij nacht. Grondspots die rondom (360 graden) stralen markeren de treden; de leuning draagt de rest van het licht. De installatie werkt op 48V extra lage spanning.",
        ],
        "punten": [
            "LED-grondspots met 360°-uitstraling en leuningverlichting.",
            "48V ELV, slagvastheidsklasse IK10.",
        ],
        "verwant": ["brug-buikslotermeer-amsterdam", "muziekgebouw-bimhuis-amsterdam"],
    },
    {
        "slug": "brugverlichting-hoofddorp",
        "titel": "Brugverlichting in 54V DC, Hoofddorp",
        "plaats": "Hoofddorp",
        "toepassing": "brug", "product": "maatwerk",
        "beeld": "brug-hoofddorp", "beelden": [],
        "kenmerken": [("Spanning", "54", "V DC ELV"), ("Slagvastheid", "IK10", ""), ("Plaats", "Hoofddorp", "")],
        "kort": "Brugleuning met ingebouwde LED-verlichting in Hoofddorp, op 54V gelijkspanning en slagvast tot IK10.",
        "inleiding": [
            "Brugleuningverlichting in Hoofddorp: de armaturen zitten in de leuning en werken op 54V gelijkspanning (ELV). De behuizing is slagvast in klasse IK10.",
        ],
        "punten": [
            "Leuningverlichting op 54V DC, extra lage spanning.",
            "Slagvastheidsklasse IK10.",
        ],
        "verwant": ["brug-buikslotermeer-amsterdam", "trapopgang-grondspots-leuningverlichting"],
    },
    {
        "slug": "muziekgebouw-bimhuis-amsterdam",
        "titel": "Herstel trap- en brugverlichting, Muziekgebouw aan het IJ",
        "plaats": "Amsterdam",
        "toepassing": "brug", "product": "maatwerk",
        "beeld": "bimhuis", "beelden": [],
        "kenmerken": [("Plaats", "Amsterdam", "Muziekgebouw aan het IJ / BIMhuis"), ("Werk", "herstel", "bestaande verlichting")],
        "kort": "Herstel van de verlichting in de trapleuning en de brug bij het Muziekgebouw aan het IJ en het BIMhuis in Amsterdam.",
        "inleiding": [
            "Bij het Muziekgebouw aan het IJ en het BIMhuis in Amsterdam is de bestaande trap- en brugverlichting hersteld. Geen nieuw ontwerp, maar de bestaande leuningverlichting weer werkend en passend bij het gebouw.",
        ],
        "punten": [
            "Herstel van bestaande trap- en brugverlichting.",
        ],
        "verwant": ["brug-buikslotermeer-amsterdam", "aanlichting-standbeeld-johan-cruijff"],
    },
    {
        "slug": "citylight-beverwijk-wijkertoren",
        "titel": "Citylight bij de Wijkertoren, Beverwijk",
        "plaats": "Beverwijk",
        "toepassing": "straat", "product": "citylight",
        "beeld": "citylight-beverwijk", "beelden": ["citylight-kerk"],
        "kenmerken": [("Armatuur", "Citylight", "paaltop"), ("Plaats", "Beverwijk", "Wijkertoren")],
        "kort": "Citylight-paaltoparmaturen op het plein bij de Wijkertoren in Beverwijk, gefotografeerd in de schemering.",
        "inleiding": [
            "Op het plein rond de Wijkertoren in Beverwijk staan Citylight-paaltoparmaturen. De foto's zijn gemaakt in de schemering en bij nacht, met de aangelichte toren op de achtergrond.",
        ],
        "punten": [
            "Citylight paaltoparmaturen op masten rond het plein.",
        ],
        "verwant": ["citylight-speelplaats-en-straat", "retrofit-straatverlichting-2200k"],
    },
    {
        "slug": "citylight-speelplaats-en-straat",
        "titel": "Citylight op een speelplaats en in de woonstraat",
        "plaats": None,
        "toepassing": "straat", "product": "citylight",
        "beeld": "citylight-speelplaats", "beelden": ["citylight-straat"],
        "kenmerken": [("Armatuur", "Citylight", "paaltop"), ("Toepassing", "speelplaats", "en straat")],
        "kort": "Citylight-armaturen rond een speelplaats en in een woonstraat: gelijkmatig licht op de plek waar mensen lopen en spelen.",
        "inleiding": [
            "Twee toepassingen van hetzelfde armatuur: een speelplaats met bankjes en een woonstraat. De Citylight staat op de mast en verdeelt het licht met een optiek die bij de plek past.",
        ],
        "punten": [
            "Citylight paaltoparmaturen op een speelplaats en in een woonstraat.",
        ],
        "verwant": ["citylight-beverwijk-wijkertoren", "schreder-cdo-naar-led-2200k"],
    },
    {
        "slug": "solarbolder-schielandhuis-rotterdam",
        "titel": "Solarbolders in de tuin van het Schielandhuis",
        "plaats": "Rotterdam",
        "toepassing": "solar", "product": "solarbolder",
        "beeld": "schielandhuis-entree", "beelden": ["schielandhuis-bolder", "schielandhuis-reflector-detail", "schielandhuis-gebouw"],
        "kenmerken": [("Energie", "zon", "geen netaansluiting"), ("Reflector", "terrazzo", "wit carrara"), ("Afwerking", "RVS", "poedercoat"), ("Plaats", "Rotterdam", "Schielandhuis")],
        "kort": "Offgrid Solarbolders langs de paden in de tuin van het Schielandhuis in Rotterdam, met een witte terrazzo reflector.",
        "inleiding": [
            "In de tuin van het Schielandhuis in Rotterdam staan Solarbolders langs de paden en bij de entree. Ze werken zonder kabel: het zonnepaneel zit in het bovenvlak, de reflector is van wit carrara-terrazzo en de behuizing van gepoedercoat roestvast staal.",
            "Het ontwerp is van Iris Dijkstra (Atelier LEK); De Licht Fabriek heeft het samen met Atelier LEK uitgewerkt tot een in Nederland geproduceerd armatuur.",
        ],
        "punten": [
            "Solarbolders, offgrid: alleen zon en daglicht nodig.",
            "Reflector in wit carrara-terrazzo, behuizing in RVS met poedercoat.",
            "Zonnepaneel in het bovenvlak van de bolder.",
        ],
        "verwant": ["solarbolder-crooswijk-rotterdam", "solarbolder-amber-azobe"],
    },
    {
        "slug": "solarbolder-crooswijk-rotterdam",
        "titel": "Solarbolders langs het parkpad in Crooswijk",
        "plaats": "Rotterdam",
        "toepassing": "solar", "product": "solarbolder",
        "beeld": "solarbolder-crooswijk", "beelden": ["solarbolder-crooswijk-2"],
        "kenmerken": [("Lichtkleur", "3000", "K"), ("Reflector", "terrazzo", ""), ("Energie", "zon", "geen netaansluiting"), ("Plaats", "Rotterdam", "Crooswijk")],
        "kort": "Solarbolders in 3000K met terrazzo reflector langs een parkpad in Crooswijk, Rotterdam.",
        "inleiding": [
            "Langs een pad in een park in Crooswijk, Rotterdam, staan Solarbolders met een terrazzo reflector in 3000K. Geen graafwerk voor kabels: elke bolder laadt overdag en brandt 's nachts.",
        ],
        "punten": [
            "Solarbolders in lichtkleur 3000K met terrazzo reflector.",
            "Offgrid geplaatst langs een parkpad.",
        ],
        "verwant": ["solarbolder-schielandhuis-rotterdam", "solarbolder-amber-azobe"],
    },
    {
        "slug": "solarbolder-amber-azobe",
        "titel": "Solarbolder met amber LED en azobé reflector",
        "plaats": None,
        "toepassing": "solar", "product": "solarbolder",
        "beeld": "solarbolder-amber-2", "beelden": ["solarbolder-amber"],
        "kenmerken": [("Lichtkleur", "amber", ""), ("Reflector", "azobé", "hardhout"), ("Behuizing", "RVS", "poedercoat")],
        "kort": "Een Solarbolder in RVS met amberkleurige LED en een reflector van azobé, in het buitengebied.",
        "inleiding": [
            "Een uitvoering van de Solarbolder voor een plek buiten de stad: amberkleurig licht, dat minder insecten aantrekt dan wit licht, en een reflector van azobé-hardhout in een gepoedercoate RVS-behuizing.",
        ],
        "punten": [
            "Solarbolder in RVS met poedercoat.",
            "Amber LED en azobé reflector.",
        ],
        "verwant": ["solarbolder-schielandhuis-rotterdam", "solarbolder-crooswijk-rotterdam"],
    },
    {
        "slug": "retrofit-straatverlichting-2200k",
        "titel": "Retrofit straatverlichting in 2200K, 16W",
        "plaats": None,
        "toepassing": "retrofit", "product": "geartray",
        "beeld": "retrofit-straat", "beelden": [],
        "kenmerken": [("Lichtkleur", "2200", "K"), ("Vermogen", "16", "W"), ("Optiek", "T3", ""), ("Dimregime", "3A", "Dynadimmer")],
        "kort": "Bestaande straatarmaturen in een woonstraat omgebouwd naar LED: 2200K, 16W, T3-optiek en dimregime 3A.",
        "inleiding": [
            "Woonstraat met bestaande armaturen op de mast. De armaturen zijn omgebouwd naar LED met een module van 16W in 2200K en een T3-optiek voor de straat; een Dynadimmer regelt 's nachts terug volgens regime 3A.",
        ],
        "punten": [
            "LED-retrofit in bestaande straatarmaturen, 16W, lichtkleur 2200K.",
            "T3-optiek, Dynadimmer met dimregime 3A.",
        ],
        "verwant": ["schreder-cdo-naar-led-2200k", "tl-naar-led-met-noodverlichting"],
    },
    {
        "slug": "schreder-cdo-naar-led-2200k",
        "titel": "Schréder-armaturen van CDO 70W naar LED 22W",
        "plaats": None,
        "toepassing": "retrofit", "product": "geartray",
        "beeld": "schreder-cdo", "beelden": [],
        "kenmerken": [("Was", "CDO 70", "W"), ("Nu", "LED 22", "W"), ("Lichtkleur", "2200", "K"), ("Optiek", "T3", "Dynadim")],
        "kort": "Schréder-armaturen met een CDO-lamp van 70W, omgebouwd naar een LED-module van 22W in 2200K met T3-optiek.",
        "inleiding": [
            "Besneeuwde woonstraat bij nacht. De Schréder-armaturen hadden een CDO-lamp van 70W; die is vervangen door een LED-module van 22W in 2200K met T3-optiek en Dynadimmer. De armaturen zelf bleven hangen.",
        ],
        "punten": [
            "LED-module 22W, lichtkleur 2200K, T3-optiek, in bestaande Schréder-armaturen.",
            "Dynadimmer voor het dimregime.",
        ],
        "verwant": ["retrofit-straatverlichting-2200k", "verledden-tunnel-geartray-22w"],
    },
    {
        "slug": "tl-naar-led-met-noodverlichting",
        "titel": "Van TL naar LED met noodverlichting",
        "plaats": None,
        "toepassing": "retrofit", "product": "geartray",
        "beeld": "noodverlichting", "beelden": [],
        "kenmerken": [("Was", "TL", ""), ("Nu", "LED", "met noodverlichting"), ("Sturing", "DALI", "dimbaar"), ("Venster", "PC", "polycarbonaat")],
        "kort": "Voetgangerstunnel bij een station: TL-armaturen omgebouwd naar dimbare LED met noodverlichting, achter polycarbonaat.",
        "inleiding": [
            "Een voetgangerstunnel bij een station, waar de verlichting ook bij stroomuitval moet blijven branden. De TL-armaturen zijn omgebouwd naar LED met noodverlichting, dimbaar via DALI, achter een polycarbonaat afscherming.",
        ],
        "punten": [
            "TL vervangen door LED met geïntegreerde noodverlichting.",
            "DALI-dimbaar, polycarbonaat afscherming.",
        ],
        "verwant": ["retrofit-straatverlichting-2200k", "tunnel-upgrade-2200k-nieuw-venster"],
    },
    {
        "slug": "aanlichting-standbeeld-johan-cruijff",
        "titel": "Aanlichting standbeeld Johan Cruijff",
        "plaats": "Amsterdam",
        "toepassing": "bijzonder", "product": "maatwerk",
        "beeld": "cruijff", "beelden": [],
        "kenmerken": [("Plaats", "Amsterdam", "Johan Cruijff ArenA"), ("Werk", "aanlichting", "LED")],
        "kort": "LED-aanlichting van het bronzen standbeeld van Johan Cruijff bij de Johan Cruijff ArenA.",
        "inleiding": [
            "Het bronzen standbeeld van Johan Cruijff bij de ArenA in Amsterdam is met LED aangelicht, zodat het ook na zonsondergang zichtbaar blijft tegen de gevel.",
        ],
        "punten": [
            "LED-aanlichting van een standbeeld in de openbare ruimte.",
        ],
        "verwant": ["uv-lichtbak-herstel-kunstwerken", "muziekgebouw-bimhuis-amsterdam"],
    },
    {
        "slug": "uv-lichtbak-herstel-kunstwerken",
        "titel": "UV-A lichtbak voor het herstel van kunstwerken",
        "plaats": None,
        "toepassing": "bijzonder", "product": "maatwerk",
        "beeld": "uv-lichtbak", "beelden": [],
        "kenmerken": [("Licht", "UV-A", ""), ("Doel", "herstel", "vergeling"), ("Productie", "custom", "op maat")],
        "kort": "Een op maat gebouwde UV-A lichtbak waarmee vergeling van kunstwerken wordt hersteld.",
        "inleiding": [
            "Geen straatverlichting, maar wel licht als gereedschap: een UV-A lichtbak, op maat gebouwd voor een restauratieatelier, om vergelingsschade aan kunstwerken te herstellen.",
        ],
        "punten": [
            "UV-A armatuur op maat ontworpen en geproduceerd.",
        ],
        "verwant": ["aanlichting-standbeeld-johan-cruijff", "brug-buikslotermeer-amsterdam"],
    },
]


def project(slug):
    return next(p for p in PROJECTEN if p["slug"] == slug)


# ------------------------------------------------------------------- menu
NAV = [
    {"soort": "link", "href": "index.html", "label": "Home"},
    {
        "soort": "uitklap", "id": "armaturen", "label": "Armaturen",
        "links": [("armaturen.html", "Alle armaturen", "Welk armatuur past waar")]
                 + [(b, t, o) for b, t, o, _ in ARMATUREN],
        "kaart": {
            "kop": "Past geen standaardarmatuur?",
            "tekst": "Tunnelarmaturen maken we op klantspecificatie. Stuur je maten of tekening, dan denken we mee.",
            "knop": "Bespreek je project",
            "href": "contact.html",
            "foto": "citylight-lens",
        },
    },
    {
        "soort": "uitklap", "id": "diensten", "label": "Diensten",
        "links": [("diensten.html", "Alle diensten", "Retrofit, maatwerk en onderzoek")]
                 + [(b, t, o) for b, t, o, _ in DIENSTEN],
        "kaart": {
            "kop": "Bestaande armaturen behouden?",
            "tekst": "Met een LED-geartray blijft de behuizing hangen en gaat alleen de techniek eruit.",
            "knop": "Vraag een prijsopgave",
            "href": "contact.html",
            "foto": "ledmodule-buis",
        },
    },
    {"soort": "link", "href": "projecten.html", "label": "Projecten"},
    {"soort": "link", "href": "over-ons.html", "label": "Over ons"},
]


# ------------------------------------------------------------------- foto's
# De foto's komen van de bronsite; de pijplijn (scratch) heeft de ingebrande
# bijschriften eraf gesneden en WebP + AVIF gemaakt in een maatladder. De
# gegevens staan in fotos.json: per sleutel de breedtes, de grootste en kleinste
# maat en de alt-tekst. Zie assets/foto/HERKOMST.md.
_REG = json.loads((HIER / "fotos.json").read_text(encoding="utf-8"))

FOTOS = {}
MATEN = {}
BADGES = {}
for _k, _v in _REG.items():
    if _v.get("badge"):
        BADGES[_k] = _v
        continue
    (gb, gh), (kb, kh) = _v["groot"], _v["klein"]
    FOTOS[_k] = (_k, gb, gh, kb, kh, _v["alt"], "foto", None)
    MATEN[_k] = _v["breedtes"]


def foto(sleutel, klasse='', laden='lazy', maten='100vw', alt=None):
    """Eén beeld, in AVIF met WebP als terugval, in meerdere breedtes.

       <picture> met een AVIF-bron en een WebP-<img>. De browser kiest de
       breedte zelf, op grond van sizes en de pixeldichtheid. width en height
       zijn die van de grootste maat; ze leggen de verhouding vast, zodat er
       niets verspringt terwijl het beeld nog laadt.

       De alt-tekst beschrijft wat er te zien is; bij puur decoratief beeld geef
       je alt='' mee."""
    naam, gb, gh, kb, kh, standaard_alt, map_, mb = FOTOS[sleutel]
    tekst = standaard_alt if alt is None else alt
    prioriteit = ' fetchpriority="high" decoding="async"' if laden == 'eager' else ' decoding="async"'
    breedtes = sorted(MATEN.get(sleutel) or ({kb, gb} | ({mb} if mb else set())))
    bron = lambda ext: ', '.join(f'assets/{map_}/{naam}-{b}.{ext} {b}w' for b in breedtes)
    klasse_attr = f' class="{klasse}"' if klasse else ''

    # Vangnet: alleen een AVIF-bron als elk bestand in die srcset ook echt op
    # schijf staat (de browser valt bij een 404 niet terug op de WebP), en hard
    # stoppen als de WebP ontbreekt, want dan is de build fout.
    ontbreekt = [b for b in breedtes if not (UIT / f'assets/{map_}/{naam}-{b}.webp').exists()]
    if ontbreekt:
        raise FileNotFoundError(f'foto {sleutel!r}: WebP ontbreekt voor breedte(s) {ontbreekt}')
    avif_compleet = all((UIT / f'assets/{map_}/{naam}-{b}.avif').exists() for b in breedtes)
    avif_bron = f'<source type="image/avif" srcset="{bron("avif")}" sizes="{maten}">' if avif_compleet else ''

    return (f'<picture>{avif_bron}'
            f'<img src="assets/{map_}/{naam}-{gb}.webp" srcset="{bron("webp")}" sizes="{maten}" '
            f'width="{gb}" height="{gh}" alt="{tekst}" loading="{laden}"{prioriteit}{klasse_attr}>'
            f'</picture>')


# Hoe breed een kaart werkelijk is, voor het sizes-attribuut.
BEELD_MATEN_4 = "(max-width: 767px) 100vw, (max-width: 991px) 50vw, 25vw"
BEELD_MATEN_3 = "(max-width: 991px) 100vw, 33vw"


from iconen import icoon as _icoon

PIJL = _icoon("arrow-right", klasse="arrow--animation is-{n}", maat=16)

SPOOR = ('<span class="button__spoor" aria-hidden="true">'
         + PIJL.format(n=1).replace('width="16" height="16"', 'width="14" height="14"')
         + PIJL.format(n=2).replace('width="16" height="16"', 'width="14" height="14"')
         + '</span>')


def _inhoud(label):
    return f'<span class="button__inhoud">{label}{SPOOR}</span>'


def knop(label, href, soort='primary', extra=''):
    """De grote CTA-knop met dezelfde pijlwissel als de ronde icoonknop."""
    attr = f' {extra}' if extra else ''
    return f'<a href="{href}" class="button button--{soort}"{attr}>{_inhoud(label)}</a>'


def icoonknop(maat="", soort=""):
    """De ronde icoonknop. Decoratief: de hele kaart is de link.
       soort="button--secundair" geeft de donkere variant, voor projecten."""
    klasse = f"button--icon {maat} {soort}".strip()
    return (f'<span class="{klasse}" aria-hidden="true" inert>'
            f'<span class="button--circle"><span class="circle-container">'
            f'{PIJL.format(n=1)}{PIJL.format(n=2)}'
            f'</span></span></span>')


CHEVRON = _icoon("chevron-down", klasse="submenu--chevron", maat=12)

LOGO_DONKER = ('<img class="header--logo-kleur" src="assets/logo/logo-donker.png" '
               'srcset="assets/logo/logo-donker.png 1x, assets/logo/logo-donker@2x.png 2x" '
               f'alt="{BEDRIJF}" width="292" height="36">')
LOGO_WIT = ('<img class="header--logo-wit" src="assets/logo/logo-wit.png" '
            'srcset="assets/logo/logo-wit.png 1x, assets/logo/logo-wit@2x.png 2x" '
            'alt="" aria-hidden="true" width="292" height="36">')


def header(actief):
    """De balk met het logo, het hoofdmenu en de hamburger, plus de uitklappers
       en het mobiele paneel. Zie SECTIONS.md."""

    def is_actief(item):
        if item["soort"] == "link":
            return item["href"] == actief
        return any(b == actief for b, _, _ in item["links"])

    def bureau_item(item):
        aan = is_actief(item)
        klasse = "submenu--link is-actief" if aan else "submenu--link"
        if item["soort"] == "link":
            huidig = ' aria-current="page"' if aan else ""
            return f'      <a class="{klasse}" href="{item["href"]}"{huidig}>{item["label"]}</a>'
        return (f'      <button type="button" class="{klasse} submenu--trigger" '
                f'data-uitklap="{item["id"]}" aria-expanded="false" '
                f'aria-controls="uitklap-{item["id"]}">{item["label"]}{CHEVRON}</button>')

    def paneel(item):
        if item["soort"] != "uitklap":
            return ""
        k = item["kaart"]
        links = "\n".join(
            f'          <li><a class="uitklap__link" href="{b}">'
            f'<span class="uitklap__naam">{titel}</span>'
            f'<span class="uitklap__uitleg">{onder}</span></a></li>'
            for b, titel, onder in item["links"])
        return f'''  <div class="uitklap" id="uitklap-{item["id"]}" data-uitklap-paneel="{item["id"]}" inert>
    <div class="uitklap__inner">
      <div class="uitklap__kolom">
        <span class="subtitle">{item["label"]}</span>
        <ul class="uitklap__lijst" role="list">
{links}
        </ul>
      </div>
      <div class="uitklap__kaart">
        {foto(k["foto"], maten="(max-width: 1199px) 0px, 40vw", alt="")}
        <span class="uitklap__sluier" aria-hidden="true"></span>
        <div class="uitklap__kaart-tekst">
          <p class="uitklap__kaart-kop">{k["kop"]}</p>
          <p class="uitklap__kaart-body">{k["tekst"]}</p>
          {knop(k["knop"], k["href"])}
        </div>
      </div>
    </div>
  </div>'''

    def mobiel_item(item, i):
        vertraging = f'style="transition-delay:{i * 60}ms"'
        rol = (f'<span class="mobile-panel--text-slide"><span class="mobile-panel--text-slide-inner">'
               f'<span>{item["label"]}</span><span>{item["label"]}</span></span></span>')
        if item["soort"] == "link":
            return (f'      <li><a class="mobile-panel--nav-link" href="{item["href"]}" '
                    f'data-panel-sluit {vertraging}>{rol}</a></li>')
        sub = "\n".join(
            f'          <li><a class="mobile-panel--sublink" href="{b}" data-panel-sluit>{titel}</a></li>'
            for b, titel, _ in item["links"])
        return f'''      <li>
        <button type="button" class="mobile-panel--nav-link mobile-panel--nav-knop"
                data-mobiel-uitklap="{item["id"]}" aria-expanded="false"
                aria-controls="mobiel-{item["id"]}" {vertraging}>{rol}{CHEVRON}</button>
        <ul class="mobile-panel--sublijst" id="mobiel-{item["id"]}" role="list" hidden>
{sub}
        </ul>
      </li>'''

    links = "\n".join(bureau_item(n) for n in NAV)
    panelen = "\n".join(filter(None, (paneel(n) for n in NAV)))
    paneel_links = "\n".join(mobiel_item(n, i) for i, n in enumerate(NAV))

    return f'''<header class="header header--scrolled" id="siteHeader">
  <div class="header--container">
    <a href="index.html" class="header--logo" aria-label="{BEDRIJF}, naar de homepage">
      {LOGO_DONKER}
      {LOGO_WIT}
    </a>

    <nav class="submenu" aria-label="Hoofdmenu">
{links}
      <a class="submenu--link highlight" href="contact.html">Contact</a>
    </nav>

    <button type="button" id="hamburger" class="hamburger" aria-expanded="false" aria-controls="mobilePanel">
      Menu
      {_icoon("menu", maat=16)}
    </button>
  </div>

{panelen}
</header>

<div class="mobile-panel--overlay" id="panelOverlay" hidden></div>
<div class="mobile-panel" id="mobilePanel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-panel--topbar">
    <a class="mobile-panel--chip" href="tel:{TELEFOON_LINK}">Bel {TELEFOON_WEERGAVE}</a>
    <button type="button" class="mobile-panel--chip is-close" id="panelSluit">
      Sluiten
      {_icoon("xmark", maat=14)}
    </button>
  </div>
  <nav class="mobile-panel--nav" aria-label="Hoofdmenu">
    <span class="mobile-panel--label">Menu</span>
    <ul class="mobile-panel--list" role="list">
{paneel_links}
    </ul>
  </nav>
  <div class="mobile-panel--cta button__mobile-width">
    {knop("Bespreek je project", "contact.html")}
  </div>
</div>'''


def footer():
    armaturen = "\n".join(f'            <li><a href="{b}">{t}</a></li>' for b, t, _, _ in ARMATUREN)
    diensten = "\n".join(f'            <li><a href="{b}">{t}</a></li>' for b, t, _, _ in DIENSTEN)
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer--widgets">
      <div class="row footer--gap">
        <div class="col-lg-3 col-md-4 col-12 widget">
          <img src="assets/logo/logo-donker.png" srcset="assets/logo/logo-donker.png 1x, assets/logo/logo-donker@2x.png 2x" alt="{BEDRIJF}" width="292" height="36" style="margin-bottom:var(--space-500)">
          <p class="footer--intro">LED-verlichting voor openbare ruimte, outdoor en solar. Ontwerp, engineering en productie in Wormerveer, met {GARANTIE} garantie.</p>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h2 class="footer--kop">Armaturen</h2>
          <ul role="list">
            <li><a href="armaturen.html">Alle armaturen</a></li>
{armaturen}
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h2 class="footer--kop">Diensten</h2>
          <ul role="list">
            <li><a href="diensten.html">Alle diensten</a></li>
{diensten}
            <li><a href="projecten.html">Projecten</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h2 class="footer--kop">Contact</h2>
          <ul role="list">
            <li><a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <p class="footer--adres">{STRAAT}<br>{POSTCODE} {PLAATS}<br>KvK {KVK}</p>
        </div>
      </div>
    </div>
    <div class="footer--line"></div>
    <div class="footer--copyright">
      <span>&copy; 2026 {BEDRIJF_JURIDISCH}</span>
      <a href="privacybeleid.html">Privacybeleid</a>
      <a href="cookies.html">Cookies</a>
    </div>
  </div>
</footer>'''


COOKIEBALK = '''<!-- ================= COOKIEMELDING ================= -->
<aside id="cookiebalk" class="cookiebalk" hidden aria-label="Cookiemelding">
  <h2>Cookie-instellingen</h2>
  <p>Deze site plaatst alleen wat nodig is om hem te laten werken. Zet je analytische cookies aan, dan help je ons te zien wat werkt en wat niet. Lees het <a href="cookies.html">cookiebeleid</a>.</p>

  <div id="cookieKeuzes" class="cookie-keuzes" hidden>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" checked disabled aria-label="Functionele cookies, altijd aan">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Functioneel</span>
        <p>Nodig om de site te laten werken. Staat altijd aan.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieAnalytisch" aria-label="Analytische cookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Analytisch</span>
        <p>Laat ons zien welke pagina&rsquo;s bezocht worden, zodat we de site kunnen verbeteren.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieMarketing" aria-label="Marketingcookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Marketing</span>
        <p>Voor advertenties en het meten daarvan. Nu niet in gebruik.</p>
      </div>
    </div>
  </div>

  <div class="cookie-knoppen">
    <button type="button" class="cookie-knop" data-cookie="weigeren">Weigeren</button>
    <button type="button" class="cookie-knop" data-cookie="aanpassen">Aanpassen</button>
    <button type="button" class="cookie-knop cookie-knop--donker" data-cookie="toestaan">Toestaan</button>
  </div>
</aside>'''


ORGANISATIE_LD = f'''{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BEDRIJF_JURIDISCH}",
  "alternateName": "{BEDRIJF}",
  "url": "{BASIS}/",
  "logo": "{BASIS}/assets/logo/logo-donker@2x.png",
  "email": "{EMAIL}",
  "telephone": "{TELEFOON_LINK}",
  "vatID": "{BTW}",
  "identifier": {{ "@type": "PropertyValue", "name": "KvK", "value": "{KVK}" }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{STRAAT}",
    "postalCode": "{POSTCODE}",
    "addressLocality": "{PLAATS}",
    "addressCountry": "NL"
  }}
}}'''

OG_BEELD = "assets/social/lichtfabriek-deelafbeelding.png"
OG_ALT = "De Licht Fabriek: LED-verlichting voor openbare ruimte, tunnels en solar"


def pagina(bestand, titel, omschrijving, namespace, pagina_css, css_naam,
           inhoud, scripts=(), extra_ld=None, actief=None, body_klasse="", og_beeld=None, og_alt=None):
    """Zet één complete HTML-pagina in elkaar."""
    ld_blokken = f'<script type="application/ld+json">\n{ORGANISATIE_LD}\n</script>'
    if extra_ld:
        ld_blokken += f'\n<script type="application/ld+json">\n{extra_ld}\n</script>'

    script_regels = "\n".join(f'<script src="{s}"></script>' for s in scripts)
    body_attr = f' class="{body_klasse}"' if body_klasse else ""
    adres = f"{BASIS}/{'' if bestand == 'index.html' else bestand}"
    beeld = f"{BASIS}/{og_beeld or OG_BEELD}"

    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{titel}</title>
<meta name="description" content="{omschrijving}" />
<link rel="canonical" href="{adres}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="{BEDRIJF_JURIDISCH}" />
<meta name="theme-color" content="#111518" />
<meta name="color-scheme" content="light" />

<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />
<link rel="preload" href="assets/fonts/inter-tight-latin.woff2" as="font" type="font/woff2" crossorigin />

<link rel="stylesheet" href="styleguide.css" />
<link rel="stylesheet" href="transitions.css" />
<link rel="stylesheet" href="cookiebalk.css" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="cookiebalk.css" /></noscript>
<link rel="stylesheet" href="{pagina_css}" data-page-css="{css_naam}" />

<link rel="icon" href="assets/favicon/favicon.ico" sizes="16x16 32x32 48x48" />
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/favicon-32.png" />
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon/favicon-192.png" />
<link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png" />

<meta property="og:type" content="website" />
<meta property="og:site_name" content="{BEDRIJF}" />
<meta property="og:locale" content="nl_NL" />
<meta property="og:url" content="{adres}" />
<meta property="og:title" content="{titel}" />
<meta property="og:description" content="{omschrijving}" />
<meta property="og:image" content="{beeld}" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{og_alt or OG_ALT}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="{beeld}" />
<meta name="twitter:title" content="{titel}" />
<meta name="twitter:description" content="{omschrijving}" />

{ld_blokken}
</head>

<body{body_attr}>
<a class="skip-link" href="#main-content">Naar de inhoud</a>

<!-- De header en het mobiele paneel staan bewust BUITEN #smooth-wrapper.
     ScrollSmoother verschuift de inhoud met een transform, en onder een
     transform hangt position:fixed aan dat element in plaats van aan het
     scherm. -->
{header(actief or bestand)}

<div id="smooth-wrapper">
<div id="smooth-content">

<div data-barba="wrapper">
<div class="app__wrapper" data-barba="container" data-barba-namespace="{namespace}">
<div class="content__wrapper">

<main id="main-content">

{inhoud}

</main>

{footer()}

<script src="site.js"></script>
<script src="contactformulier.js"></script>
{script_regels}
</div><!-- /.content__wrapper -->
</div><!-- /[data-barba=container] -->
</div><!-- /[data-barba=wrapper] -->

</div><!-- /#smooth-content -->
</div><!-- /#smooth-wrapper -->

{COOKIEBALK}

<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollSmoother.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@barba/core@2.10.3/dist/barba.umd.js"></script>
<script defer src="cookiebalk.js"></script>
<script defer src="analytics.js"></script>
<script defer src="smooth-scroll.js"></script>
<script defer src="page-transitions.js"></script>

</body>
</html>
'''


# ------------------------------------------------------------ kenmerkenband
# De doorlopende band onderaan de pagina's. In de template stonden hier
# klantlogo's; van De Licht Fabriek zijn geen opdrachtgevers met naam bekend,
# dus staan hier de kenmerken uit het eigen materiaal: de drie badges van de
# bronsite en de feitelijke eigenschappen van het aanbod. Klantlogo's kunnen
# hier later bij, zie CONTENT-TODO.md.
KENMERKEN = [
    ("badge", "badge-made-in-holland", "Made in Holland", 120),
    ("tekst", "2200K · 3000K · 4000K", "", 0),
    ("badge", "badge-garantie", "Made in Holland, vijf jaar garantie", 183),
    ("tekst", "DALI / DALI SR · 1-10V", "", 0),
    ("badge", "badge-ik10", "IK10 rated", 80),
    ("tekst", "Dynadimmer, dimregime 3A", "", 0),
    ("tekst", "RVS en polycarbonaat", "", 0),
    ("tekst", "Antigraffiticoating", "", 0),
    ("tekst", "ELV 48V / 54V DC", "", 0),
    ("tekst", "Offgrid solar", "", 0),
    ("tekst", "Ontwerp en productie in Wormerveer", "", 0),
]


def _kenmerkset(verborgen=False, plat=False):
    extra = ' aria-hidden="true"' if verborgen else ''
    bron = 'src' if plat else 'data-src'
    regels = []
    for soort, waarde, alt, breedte in KENMERKEN:
        if soort == "badge":
            ext = "png" if waarde == "badge-garantie" else "webp"
            regels.append('          <li class="logo-slider__logo">'
                          f'<img {bron}="assets/foto/{waarde}.{ext}" alt="{alt}" '
                          f'width="{breedte}" height="80" decoding="async"></li>')
        else:
            regels.append(f'          <li class="logo-slider__logo logo-slider__tekst">{waarde}</li>')
    return f'        <ul class="logo-slider__set"{extra}>\n' + "\n".join(regels) + '\n        </ul>'


def kenmerkenband(nr):
    """De doorlopende band. De reeks staat er twee keer in: de animatie
       schuift precies de helft op. Het tweede exemplaar is aria-hidden."""
    return (f'  <section class="logo-slider" id="s{nr}-kenmerken" aria-label="Kenmerken van ons aanbod" data-logoband>\n'
            '    <div class="logo-slider__venster">\n'
            '      <div class="logo-slider__spoor">\n'
            f'{_kenmerkset()}\n{_kenmerkset(verborgen=True)}\n'
            '      </div>\n'
            '    </div>\n'
            '    <noscript>\n'
            '      <div class="logo-slider__venster">\n'
            '        <div class="logo-slider__spoor">\n'
            f'{_kenmerkset(plat=True)}\n{_kenmerkset(verborgen=True, plat=True)}\n'
            '        </div>\n'
            '      </div>\n'
            '    </noscript>\n'
            '  </section>')


def ctablok(nr, kop, tekst=None):
    """Eén donker vlak over de volle breedte met kop, tekst en de knop naar de
       contactpagina. Geen reactietijd: die staat niet op de bron."""
    regel = tekst or 'Stuur je maten, tekening of vraag. We denken mee over wat er past en maken een prijsopgave.'
    return (f'  <section class="cta-slot" id="s{nr}-contact">\n'
            '    <div class="container">\n'
            '      <div class="cta-slot__hoofd">\n'
            '        <span class="subtitle cta-slot__label">Contact</span>\n'
            f'        <h2 class="cta-slot__kop">{kop}</h2>\n'
            f'        <p class="cta-slot__tekst">{regel}</p>\n'
            '        <div class="cta-slot__actie">\n'
            f'          {knop("Bespreek je project", "contact.html")}\n'
            f'          <a class="cta-slot__bel" href="tel:{TELEFOON_LINK}">of bel {TELEFOON_WEERGAVE}</a>\n'
            '        </div>\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')


def slotblok(nr, kop, tekst=None):
    """De kenmerkenband met daaronder de CTA: twee secties, twee nummers."""
    return kenmerkenband(nr) + "\n\n" + ctablok(f"{int(nr) + 1:02d}", kop, tekst)


def paginahero(nr, ident, label, titel, beeld, alt=None, positie=None, hoog=False):
    """De hero met links de kop op grijs en rechts een foto."""
    stijl = f' style="object-position:{positie}"' if positie else ""
    beeldtag = foto(beeld, laden="eager", maten="(max-width: 767px) 100vw, 60vw", alt=alt)
    if stijl:
        beeldtag = beeldtag.replace("<img ", f"<img{stijl} ")
    klasse = " paginahero--hoog" if hoog else ""
    return (f'  <section class="paginahero{klasse}" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld">\n'
            f'      {beeldtag}\n'
            '    </div>\n'
            '  </section>')


def patroonhero(nr, ident, label, titel):
    """Dezelfde hero, met het merkpatroon (lichtkegels op donker) in plaats van
       een foto. Decoratief: alt="" en aria-hidden."""
    return (f'  <section class="paginahero paginahero--patroon" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld" aria-hidden="true">\n'
            '      <picture>\n'
            '        <source media="(max-width: 767px)" srcset="assets/patronen/hero-patroon-mobiel-720.webp 720w, assets/patronen/hero-patroon-mobiel-800.webp 800w, assets/patronen/hero-patroon-mobiel-1440.webp 1440w" sizes="100vw" width="1440" height="1440">\n'
            '        <img src="assets/patronen/hero-patroon-1440.webp" srcset="assets/patronen/hero-patroon-720.webp 720w, assets/patronen/hero-patroon-1000.webp 1000w, assets/patronen/hero-patroon-1440.webp 1440w" sizes="50vw" width="1440" height="940" alt="" loading="eager" fetchpriority="high" decoding="async">\n'
            '      </picture>\n'
            '    </div>\n'
            '  </section>')


KLEURENRIJ = ("oranje", "grijs", "wit", "donker")


def vlakkenrij(nr, ident, kop, vlakken, subtitel=None, intro=None):
    """Kop met daaronder vier gekleurde vlakken over de volle breedte."""
    label = f'        <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>\n' if subtitel else ""
    inleiding = f'        <p class="article-body vlakkenband__intro">{intro}</p>\n' if intro else ""
    items = "\n".join(
        f'      <li class="vlak vlak--{KLEURENRIJ[i % 4]}">\n'
        + (f'        <h3 class="vlak__kop">{titel}</h3>\n' if titel else '')
        + f'        <p class="vlak__tekst">{tekst}</p>\n'
        '      </li>'
        for i, (titel, tekst) in enumerate(vlakken)
    )
    return (f'  <section class="vlakkenband" id="s{nr}-{ident}">\n'
            '    <div class="container">\n'
            '      <div class="vlakkenband__kop">\n'
            f'{label}'
            f'        <h2 class="section-heading">{kop}</h2>\n'
            f'{inleiding}'
            '      </div>\n'
            '    </div>\n'
            '    <ul class="vlakkenrij">\n'
            f'{items}\n'
            '    </ul>\n'
            '  </section>')


def beeldkaart(kop, tekst, beeld, alt=None, kleur="grey", href=None, meta=None):
    """Een kaart met de foto erboven en de tekst eronder, twee per rij."""
    metaregel = f'        <span class="subtitle">{meta}</span>\n' if meta else ""
    binnen = (f'      <figure class="cta-blocks-advanced__banner">\n'
              f'        {foto(beeld, maten="(max-width: 991px) 100vw, 50vw", alt=alt)}\n'
              '        <span class="cta-blocks-advanced__backdrop" aria-hidden="true"></span>\n'
              '      </figure>\n'
              f'      <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{kleur}">\n'
              f'{metaregel}'
              f'        <h3 class="cta-blocks-advanced__title">{kop}</h3>\n'
              '        <div class="cta-blocks-advanced__wrapper">\n'
              f'          <div class="cta-blocks-advanced__content"><p>{tekst}</p></div>\n'
              '        </div>\n'
              '      </div>')
    if href:
        omhulsel = (f'    <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" '
                    f'href="{href}">\n{binnen}\n    </a>')
    else:
        omhulsel = f'    <div class="cta-blocks-advanced__card">\n{binnen}\n    </div>'
    return f'  <div class="col-lg-6 col-12 kolom--vullend">\n{omhulsel}\n  </div>'


def fotokaart(i, item, meta_label=None):
    """Eén onderdeel van het aanbod als paneel met de foto erboven (rij van
       drie of vier). item = (bestand, titel, ondertitel, beeld)."""
    bestand, titel, sub, beeld = item
    meta = meta_label or sub
    return f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{bestand}">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <span class="panel__meta">{meta}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{sub}</p>
            <span class="panel__actie">{icoonknop()}</span>
          </a>
        </div>'''


def aanbodkaart(i, item, intro, label):
    """Eén armatuur of dienst als grote kaart met de foto erboven, drie per rij."""
    bestand, titel, sub, beeld = item
    return f'''        <div class="col-lg-4 col-12 kolom--vullend">
          <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" href="{bestand}"
             aria-label="{titel}: {_plat(sub)}">
            <figure class="cta-blocks-advanced__banner cta-blocks-advanced__banner--verhouding">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{'grey' if i % 2 == 0 else 'white'}">
              <span class="subtitle">{label} 0{i + 1}</span>
              <div class="cta-blocks-advanced__wrapper">
                <div>
                  <h3 class="cta-blocks-advanced__title" style="margin-bottom:var(--space-500)">{titel}</h3>
                  <div class="cta-blocks-advanced__content"><p>{sub}</p><p>{intro}</p></div>
                </div>
                {icoonknop("button--icon--56")}
              </div>
            </div>
          </a>
        </div>'''


def projectrij(p, grijs):
    """Eén project als rij met tekst links en foto rechts."""
    product_naam = PRODUCTEN[p["product"]][0]
    meta2 = p["plaats"] or TOEPASSINGEN[p["toepassing"]]
    return f'''      <a class="cases-grid__row {'cases-grid__row--grey' if grijs else 'cases-grid__row--white'} hover--icon"
         href="project-{p["slug"]}.html" aria-label="Project: {_plat(p["titel"])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">{product_naam}</span>
            <span class="cases-grid__meta-item">{meta2}</span>
          </div>
          <h3 class="cases-grid__title">{p["titel"]}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{p["kort"]}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(p["beeld"], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>'''


def projectenblok(nr, slugs, kop="Uit de praktijk", ident="projecten"):
    rijen = "\n".join(projectrij(project(s), grijs=(i % 2 == 0)) for i, s in enumerate(slugs))
    return f'''  <section class="cases-grid" id="s{nr}-{ident}">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">{kop}</h2>
        {knop("Alle projecten", "projecten.html", "secundair")}
      </div>
      <div class="cases-grid__list">
{rijen}
      </div>
    </div>
  </section>'''


def quotelogo(slug):
    """Onder een citaat: het logo van de opdrachtgever. Zolang er geen echte
       reviews met toestemming zijn, staat hier een invulveld."""
    return ('<p class="quote__logo quote__logo--leeg">'
            '<span class="invulveld">Logo opdrachtgever</span></p>')


# TODO-CONTENT: placeholder-reviews. Op de bronsite staan geen reviews. Deze
# drie beschrijven de werkwijze (op maat, geartray past, offgrid), zonder
# resultaten, cijfers of garanties, en zonder namen van personen of bedrijven.
# Vervangen door echte reviews met naam en toestemming vóór livegang.
REVIEWS = [
    ("Het armatuur is precies gemaakt op de maten van onze onderdoorgang. Tekening, proefmontage en plaatsing liepen via één aanspreekpunt.",
     "Beheerder openbare verlichting", "gemeente", "tuin-schielandhuis-3", None),
    ("Voor het verledden van bestaande armaturen kregen we een geartray die zonder aanpassingen paste. Dat scheelde een complete vervanging.",
     "Projectleider", "installatiebedrijf", "titan-tuscan-3000k", None),
    ("De Solarbolder staat waar geen kabel ligt. Ontwerp en uitvoering sloten goed op elkaar aan.",
     "Lichtontwerper", "ontwerpbureau", "citylight-plein", None),
]


def quoteslider(nr, ident, subtitel, kop, items):
    """Een quote per keer, groot uitgelicht: beeld links, citaat rechts, pijlen
       en een timer eronder. items: (citaat, naam, functie, fotosleutel, logo).
       De foto is een project en geen portret."""
    dias = "\n".join(f'''        <figure class="quote" role="group" aria-roledescription="citaat"
               aria-label="Citaat {i + 1} van {len(items)}">
          <div class="quote__beeld">
            {foto(sleutel, maten="(max-width: 767px) 100vw, 40vw")}
          </div>
          <div class="quote__body">
            <blockquote class="quote__tekst"><p>{citaat}</p></blockquote>
            <hr class="quote__streep">
            <figcaption class="quote__naam">{naam}, {functie}</figcaption>
            {quotelogo(logo)}
          </div>
        </figure>''' for i, (citaat, naam, functie, sleutel, logo) in enumerate(items))

    return f'''  <section class="quotes" id="s{nr}-{ident}">
    <div class="container">
      <div class="quotes__kop">
        <span class="subtitle">{subtitel}</span>
        <h2 class="section-heading">{kop}</h2>
      </div>
      <!-- TODO-CONTENT: placeholder-reviews zonder naam; vervangen door echte reviews met toestemming -->
      <div class="quotes__venster" data-quoteslider aria-live="polite">
{dias}
      </div>
      <div class="quotes__nav" hidden>
        <button type="button" class="button--icon button--icon--56 button--grijs quotes__pijl" data-quote="vorige" aria-label="Vorige quote">
          <span class="button--circle"><span class="circle-container">{_pijl_paar("links")}</span></span>
        </button>
        <button type="button" class="button--icon button--icon--56 button--grijs quotes__pijl" data-quote="volgende" aria-label="Volgende quote">
          <span class="button--circle"><span class="circle-container">{_pijl_paar("rechts")}</span></span>
        </button>
        <p class="quotes__teller" data-quote-teller>1 / {len(items)}</p>
        <span class="quotes__timer" aria-hidden="true"><span class="quotes__timer-balk"></span></span>
      </div>
    </div>
  </section>'''


def _pijl_paar(richting):
    naam = "arrow-left" if richting == "links" else "arrow-right"
    return "".join(_icoon(naam, klasse=f"arrow--animation is-{n}", maat=16) for n in (1, 2))


def contactblok(nr, onderwerp, kop="Bespreek je project",
                intro="Stuur je maten, tekening of vraag. We nemen contact op om door te spreken wat er past."):
    """Het gedeelde formulier. De HTML wordt door contactformulier.js gerenderd;
       hier staat alleen de haak plus een terugval voor bezoekers zonder JS."""
    return f'''  <section class="band background--grey" id="s{nr}-contact">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Contact</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">{kop}</h2>
          <p class="article-body">{intro}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Liever bellen? <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a>
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <div data-contactformulier data-onderwerp="{onderwerp}"></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
              <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
          </noscript>
        </div>
      </div>
    </div>
  </section>'''


def faq_blok(nr, items, titel="Veelgestelde vragen"):
    """FAQ-items als accordeon plus de bijbehorende FAQPage-structuurdata."""
    regels = []
    for i, (vraag, antwoorden) in enumerate(items):
        alineas = "".join(f"<p>{a}</p>" for a in antwoorden)
        regels.append(f'''          <div class="accordion__item">
            <button type="button" class="accordion__header" aria-expanded="false" aria-controls="faq-{nr}-{i}">
              <span class="accordion__number">{i + 1:02d}</span>
              <span class="accordion__title">{vraag}</span>
              <span class="accordion__suffix" aria-hidden="true"><span class="accordion__icon"></span></span>
            </button>
            <div class="accordion__details" id="faq-{nr}-{i}">
              <div class="accordion__details-inner article-body">{alineas}</div>
            </div>
          </div>''')
    return f'''  <section class="band background--white" id="s{nr}-faq">
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-12">
          <span class="subtitle">FAQ</span>
          <h2 class="font-size--lg" style="margin-top:var(--space-500)">{titel}</h2>
        </div>
        <div class="col-md-8 col-12">
          <div class="accordion">
{chr(10).join(regels)}
          </div>
        </div>
      </div>
    </div>
  </section>'''


def faq_ld(items):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": _plat(v),
             "acceptedAnswer": {"@type": "Answer", "text": " ".join(_plat(a) for a in ant)}}
            for v, ant in items
        ],
    }, ensure_ascii=False, indent=2)


def _plat(tekst):
    import re, html
    return html.unescape(re.sub(r"<[^>]+>", "", tekst))


def sectiekop(subtitel, kop, intro=None, knop_html=None):
    """De kop boven een kaartenrij: subtitel, h2 en eventueel een intro, met
       rechts ruimte voor een knop."""
    intro_html = (f'            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{intro}</p>\n'
                  if intro else "")
    knop_kolom = (f'          <div class="col-md-4 col-12 text-md-end">\n            {knop_html}\n          </div>\n'
                  if knop_html else "")
    return f'''      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>
            <h2 class="section-heading">{kop}</h2>
{intro_html}          </div>
{knop_kolom}        </div>
      </div>'''
