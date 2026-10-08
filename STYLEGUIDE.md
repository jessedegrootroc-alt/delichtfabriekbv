# STYLEGUIDE.md: De Licht Fabriek

Het ontwerpsysteem van deze site is overgenomen uit een template; de volledige
specificatie daarvan staat in `STYLEGUIDE-SPECIFICATIE.md` (de paragraafnummers
in de commentaren van `styleguide.css` verwijzen daarnaar). Dit bestand beschrijft
wat je moet weten om hier te werken, en waar De Licht Fabriek afwijkt.

## Het systeem in het kort

- **Palet: de kleuren van De Licht Fabriek.** Oranje en de donkere tonen komen uit
  het thema van de bronsite (`#ff6310`, `#111518`), het logo is zwart lijnwerk.

  | Token | Waarde | Waarvoor |
  |---|---|---|
  | `--color-oranje` | `#FF6310` | de CTA-kleur: knoppen, accenten, het eerste vlak in een vlakkenrij, invulvelden |
  | `--color-oranje-hover` | `#E85300` | hover op een oranje knop |
  | `--color-leisteen` | `#2A3340` | merkvlakken (de band op de homepage, het vierde vlak), grote koppen, de secundaire knop, de rand van een trede |
  | `--color-leisteen-diep` | `#1C232D` | haarlijnen, kleine labels, hover op een leisteen vlak |
  | `--color-nacht` | `#111518` | **alle lopende tekst en kleine koppen**, de sluier over foto's, het slotblok |
  | `--color-background` | `#FFFFFF` | het paginavlak |
  | `--color-grey` | `#F1F1F1` | de tweede achtergrond, voor afwisselende banden en panelen |

  Verzin geen nieuwe kleuren; gebruik deze tokens. De oude namen uit de template
  (`groen`, `geel`) komen niet meer voor.

- **Contrast.** Nacht op wit haalt 17,9:1, op grijs 15,9:1. Wit op leisteen
  11,6:1. Zwarte tekst op oranje 7,0:1 (knoppen, het oranje vlak). Oranje als
  tekstkleur op wit haalt maar 3,0:1 en wordt daarom nergens voor tekst gebruikt;
  grote koppen staan in leisteen, niet in oranje. Wit op oranje (1,9:1) mag nooit.
- **Vierkante hoeken.** `border-radius: 0` op alles, behalve ronde icoonknoppen
  (`100px`) en de markeer-chip in een kop (`12px`).
- **Geen schaduwen op layout.** Hoogteverschil maak je met een andere
  achtergrondkleur. Alleen zwevende lagen (de cookiemelding) hebben er een.
- **Koppen zijn licht (300), labels zijn medium (500).** Hoe kleiner de tekst, hoe
  zwaarder. Uppercase labels krijgen `letter-spacing: 2.2px`; lopende tekst is
  nooit uppercase.
- **Secties zijn volle kleurbanden**, geen zwevende kaarten. Het ritme komt uit de
  padding van de band: 96px verticaal en 48px horizontaal op desktop, 32/16px op
  mobiel. Twee banden op elkaar halveren hun padding (`:has(+ section)`), zodat
  elke overgang dezelfde lucht heeft.
- **Eén zijinzet voor de hele pagina: `--inset-x`.** 48px, 16px onder 992px.
  Alles wat de linkerrand raakt gebruikt die ene variabele.
- **De container heeft geen maximumbreedte** (`--container-max: none`; de
  template hield 1800px aan). Elke kleurband loopt dus op elk scherm tot de
  rand; er staat nooit een witte strook naast een grijs, donker of oranje vlak.
  De leesbreedte komt uit `--content-max-*` en uit maxima op de statementtekst,
  de kaarttekst en de citaten.
- **Links uitlijnen.** Gecentreerde tekst alleen in het slotblok.
- **Beweging is beperkt** tot hover, menu's, de doorlopende kenmerkenband, de
  quoteslider (6 s per citaat, timerbalk, pauze bij focus) en de tellers op de
  homepage. Alles respecteert `prefers-reduced-motion`; ScrollSmoother staat dan
  uit.
- **Lettertype:** Inter Tight, lokaal in `assets/fonts/`, `font-display: swap`.
  De bronsite gebruikt een themastandaard (Nunito Sans) zonder huisstijlkeuze;
  de template-typografie is aangehouden.

## Waar De Licht Fabriek afwijkt van de template

| Onderwerp | Template | Hier | Waarom |
|---|---|---|---|
| Kleuren | groen en geel | oranje, nacht, leisteen | het palet van de bron en het zwarte logo |
| Logo | svg-woordmerk | `logo-donker.png` / `logo-wit.png` (1x en 2x), 8,1:1 | de bron levert alleen een png met een kader; het kader is eraf, het lijnwerk is vrijgemaakt. Op een donkere hero wisselt de header naar de witte variant |
| Merkpatroon | gele stralen | lichtkegels op donker (`assets/patronen/`) | getekend voor dit merk: licht in de duisternis |
| Logoband | klantlogo's | badges en tekstkenmerken (`.logo-slider__tekst`) | er zijn geen opdrachtgevers met naam; kenmerken zijn wel feiten |
| Homepagehero | foto met film erover | foto (eerste beeldje) met de aangeleverde film erover | `assets/video/hero-licht.mp4`, zie `assets/video/HERKOMST.md` |
| Dienstpagina | één vast skelet | kop en staart vast, blokken per pagina gekozen (`cfg["volgorde"]`) | producten vragen specificaties, diensten een beeldverhaal; zonder nieuwe componenten |
| Cases | database (Supabase) met beheer | statische projectpagina's uit `PROJECTEN` | geen beheeromgeving nodig; alles komt uit de bron |
| Kerncijfers | getallen | getallen én woorden (`.kerncijfer__getal--tekst`) | "terrazzo" of "Rotterdam" past niet in de cijferstijl |
| Slotblok | kop, tekst, knop | plus een belregel (`.cta-slot__bel`) | bellen is op de bronsite de eerste contactroute |
| Paginakop | vaste regelbreedte | `hyphens: auto` op `.paginahero__titel` | "Tunnelarmaturen" en "Thermografisch" lopen anders over het beeld |
| Container | maximaal 1800px | geen maximum | geen witte stroken naast de kleurbanden op brede schermen, op verzoek |
| Cursussen, CMS, admin | aanwezig | verwijderd | niet van toepassing |

Nieuwe afwijkingen markeer je in de CSS met een comment dat begint met
`INFERRED:` en de reden erbij.

## Praktisch

- Tokens en componenten: `styleguide.css`. Paginaspecifieke opmaak: `index.css`,
  `service.css`, `projecten.css`, `contact.css`, `over-ons.css`, `tekstpagina.css`.
- Elke paginastijl is in de `<head>` gemarkeerd met `data-page-css="naam"`; het
  overgangsscript wisselt die mee.
- De sectiestructuur staat in `SECTIONS.md`.
- **Kleuren staan als token, niet als rgba.** De sluiers over foto's gebruiken de
  rgba-waarde van nacht (`17, 21, 24`) en leisteen (`42, 51, 64`); staat er een
  rgba, zet er dan bij welk token het is.
- **Foto met witte tekst erover: altijd twee lagen** (leisteen 20% naar 80%, zwart
  50% naar 75%). Zo staan de hero's van de projectpagina's; de homepagehero heeft
  zwart 30% naar 70% omdat de tekst daar onderin staat.
- **Het slotblok wijkt bewust af van de contrasteis**: witte tekst op het rood-oranje verloop zonder waas, op verzoek. Zie het commentaar bij `.cta-slot__hoofd`.
- **Dark mode** is er niet (`color-scheme: light`); de template had hem ook niet.
