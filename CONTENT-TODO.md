# CONTENT-TODO: wat er nog van De Licht Fabriek moet komen

Alles op de site komt van https://www.delichtfabriekbv.nl/ (7 oktober 2026) of is
daar rechtstreeks uit afgeleid. Wat de bron niet geeft, is niet verzonnen; op die
plekken staat een placeholder die hieronder genoemd wordt. Een geel invulveld in
de pagina (`.invulveld`) markeert een gat dat niet per ongeluk live mag.

## Vóór livegang

| Wat | Waar | Nu |
|---|---|---|
| **Reviews** met naam, functie, bedrijf en toestemming | homepage `s08-reviews`, contact `s03-reviews` (`REVIEWS` in `schil.py` en `bouw_contact.py`) | drie placeholder-citaten over de werkwijze, alleen met een rol ("Beheerder openbare verlichting, gemeente"), zonder resultaten of cijfers, met een geel invulveld voor het logo |
| **Klantlogo's** met toestemming | kenmerkenband onderaan de pagina's (`KENMERKEN` in `schil.py`) | de drie badges van de bronsite plus feitelijke kenmerken als tekst |
| **Endpoint contactformulier** | `contactformulier.js`, `ENDPOINT` | leeg: het formulier toont een bevestiging maar verstuurt niets |
| **Datum privacy- en cookiebeleid**, hostingpartij, verwerkersovereenkomst | `privacybeleid.html`, `cookies.html` | gele invulvelden |
| **Thermolight-beeld** | hero en galerij op `thermolight.html` | de kleine warmtebeelden van de bronsite; zie `image-replacements.json` |
| **Reactietijd** op een bericht | contact, slotblok | bewust niet genoemd; staat niet op de bron |

## Te bevestigen door De Licht Fabriek

- De **productnaam Titan** (met HE/UHE en type DLF13-60-22) komt uit de
  fotobijschriften, niet uit lopende tekst. Klopt de naam en de schrijfwijze?
- **Vijf jaar garantie** en **Made in Holland** komen van de badge op de bronsite.
  Geldt de garantie voor alle armaturen, ook maatwerk en geartrays? Zo niet, dan
  moet dat op `maatwerk.html` en `retrofit.html` worden aangepast.
- **200 lumen per watt** (geartray) en **180 lumen per watt** (custom LED-module in
  buis) komen uit fotobijschriften. Op de homepage staat 200 als cijfer.
- **IK10** staat als badge en in bijschriften bij tunnel- en brugverlichting. Op
  `paaltop-armaturen.html` wordt het niet geclaimd, omdat de bron dat daar niet doet.
- **Locaties en toeschrijving van de projecten** komen uit bestandsnamen van de
  foto's: Buikslotermeer Amsterdam, Hoofddorp, Beverwijk (Wijkertoren), Crooswijk en
  Schielandhuis Rotterdam, Muziekgebouw aan het IJ / BIMhuis, Johan Cruijff ArenA.
  Wie de opdrachtgever was staat nergens en wordt dus niet genoemd.
- Bij een aantal projecten zijn **twee foto's samengenomen** op grond van gelijke
  bijschriften (bijvoorbeeld "Verledden tunnel" en "Verledden geartray"). Horen ze
  bij hetzelfde project?
- **Thermolight**: de pagina beschrijft het onderzoek in algemene termen (contactloos,
  installatie blijft in bedrijf, beelden met beoordeling). Welke rapportage levert
  De Licht Fabriek precies?
- **Oprichtingsjaar, team, certificeringen, levertijden, prijzen**: staan niet op de
  bron en niet op de site. Aanleveren als ze genoemd moeten worden.

## Herofilm

De film onder de homepagehero (`assets/video/hero-licht.mp4`) is gegenereerd
promotiemateriaal, aangeleverd door Jesse: sfeerbeeld, geen opnamen van eigen
projecten. Eigen filmbeeld van een project of de werkplaats kan hem één op één
vervangen (zelfde bestandsnaam, 16:9); het eerste beeldje dan ook opnieuw als
`hero-video-poster` in de beeldpijplijn.

## Wat de site bewust niet doet

- Geen cijfers over besparing, levensduur in uren of aantal geplaatste armaturen.
- Geen klantnamen bij projecten.
- Geen stockfoto's: alle beeld is van De Licht Fabriek zelf, met de ingebrande
  bijschriften eraf gesneden (zie `assets/foto/HERKOMST.md`). De enige uitzondering
  zijn de kleine thermografiebeelden, die op de bronsite staan maar te klein zijn.
