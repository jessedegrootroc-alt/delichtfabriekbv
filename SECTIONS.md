# SECTIONS.md: het sectieskelet

De site heeft geen build-stap, dus er zijn geen includes of partials. Pagina's van
hetzelfde type delen hun structuur doordat de generator (`_generator/`) ze uit
dezelfde functies opbouwt. Dit bestand beschrijft dat skelet één keer; de HTML in
de hoofdmap is het resultaat en wordt niet met de hand bewerkt.

---

## Wat elke pagina heeft

```html
<body>
  <a class="skip-link" href="#main-content">Naar de inhoud</a>

  <!-- alles met position:fixed staat BUITEN #smooth-wrapper -->
  <header class="header" id="siteHeader">…</header>
  <div class="mobile-panel--overlay" id="panelOverlay" hidden></div>
  <div class="mobile-panel" id="mobilePanel">…</div>

  <div id="smooth-wrapper">
    <div id="smooth-content">
      <div data-barba="wrapper">
        <div class="app__wrapper" data-barba="container" data-barba-namespace="…">
          <div class="content__wrapper">
            <main id="main-content">…secties…</main>
            <footer class="footer">…</footer>
            <script src="site.js"></script>
            <script src="contactformulier.js"></script>
          </div>
        </div>
      </div>
    </div>
  </div>

  <aside id="cookiebalk">…</aside>
  <!-- gsap, ScrollTrigger, ScrollSmoother, barba, cookiebalk.js,
       analytics.js, smooth-scroll.js, page-transitions.js -->
</body>
```

Regels die daarbij horen:

- **Het hoofdmenu heeft twee uitklappers: Armaturen en Diensten.** Een item in
  `NAV` (schil.py) is óf een gewone link óf een uitklapper met sublinks en een
  kaart. De sublinks komen uit `ARMATUREN` en `DIENSTEN`, zodat een wijziging
  daar meteen in het menu, de voet en de overzichten landt. De kaart in de
  uitklapper draagt een foto (`citylight-lens`, `ledmodule-buis`) die nergens
  anders staat, want de uitklapper staat op elke pagina.
- **Alles wat `position: fixed` is hoort buiten `#smooth-wrapper`.** ScrollSmoother
  verschuift `#smooth-content` met een transform, en onder een transform hangt
  `fixed` aan dat element in plaats van aan het scherm.
- **De header en het paneel staan buiten de barba-container** en blijven staan bij
  een pagina-overgang. Welke menulink actief is wordt in `page-transitions.js`
  overgezet; `site.js` haalt zijn oude listeners eraf via `window.__dlfVast`.
- **De scripts in de container** worden bij een pagina-overgang opnieuw uitgevoerd
  en zoeken hun elementen binnen `document.currentScript.closest('[data-barba="container"]')`.
- **Het contactformulier** staat één keer in `contactformulier.js` en rendert in
  elke `<div data-contactformulier data-onderwerp="…">`. De onderwerpen zijn de
  drie armaturen, de drie diensten en "Overig".
- **Sectie-ids zijn genummerd** (`s01-introductie`, `s02-…`) in de volgorde op de
  pagina.

---

## Rangorde in de knoppen

| Niveau | Kleur | Waarvoor |
|---|---|---|
| primair | oranje (`button--primary`) | alles wat naar contact leidt, armaturen en diensten |
| secundair | leisteen (`button--secundair`) | alles wat naar een project leidt |
| tertiair | wit met rand (`button--secondary`) | de tweede knop in een hero |

Armaturen en diensten zijn waar iemand voor komt; de projecten zijn de
onderbouwing daarbij. Het contactblok onder aan een projectpagina blijft oranje:
dat is de conversie.

## Homepage (`index.html`)

| id | component | rol in de flow |
|---|---|---|
| `s01-introductie` | `.hero` met eigen foto en sluier, witte tekst linksonder | wie, voor wie, belofte, twee knoppen |
| `s02-wat-we-doen` | `.content-text-side-cta` op grijs | herkenning van de situaties waarvoor DLF maakt |
| `s03-eigen-huis` | `.cta-blocks-advanced__card--horizontal`: tekst links, beeld rechts, elk de helft; onder 992px gestapeld | één partij van vraag tot armatuur |
| `s04-armaturen` | drie `.cta-blocks-advanced__card` met foto (16:10) | de drie armaturen |
| `s05-projecten` | drie `.cases-grid__row` | bewijs |
| `s06-cijfers` | `.panel-row--3` met `.usp__getal` (tellers) | drie cijfers met bron (5 jaar, 200 lm/W, 365 dagen) |
| `s07-diensten` | `.panel-row--3` met `.panel--beeld` | de drie diensten |
| `s08-reviews` | `.quotes` (quoteslider, wisselt elke 6 s) | placeholder-reviews |
| `s09-faq` | `.accordion`, drie items, met `FAQPage` | bezwaren |
| `s10-over` | `.streamer--employee` op leisteen, foto links | het bedrijf in Wormerveer |
| `s11-kenmerken` + `s12-contact` | het slotblok | kenmerkenband + CTA |

## Detailpagina's (`bouw_detail.py`)

Armaturen (`solarbolder`, `tunnelarmaturen`, `paaltop-armaturen`) en diensten
(`retrofit`, `maatwerk`, `thermolight`) delen de kop en de staart en kiezen zelf de
blokken ertussen (`cfg["volgorde"]`). Gedeelde opmaak in `service.css`.

| blok | component | waar |
|---|---|---|
| kop | `.paginahero.paginahero--hoog`: kop op grijs links (40%), foto rechts (60%) | alle zes |
| `statement` | `.content-text-side-cta` met knop ernaast | alle zes |
| `situaties` | `.panel-row--3`, "Situatie 01…03" | alle zes |
| `aanpak` | `.band.background--grey` + `<ol class="trap">`, met "Jij levert" per trede | alle zes |
| `specs` | `.panel-row--4` of `--3` met `.spec` (meta, waarde, uitleg) | armaturen, retrofit |
| `voordelen` | `.panel-row--4` met icoon uit de iconenset | alle zes |
| `beeldtekst` | `.content-text-side-visual` | retrofit (TL naast LED) |
| `galerij` | `beeldkaart()` twee per rij, of `kolommen: 3` als drie panelen | alle zes |
| `projecten` | `projectenblok()`: drie rijen | alle behalve thermolight |
| `faq` | het gedeelde FAQ-blok | alle zes |
| `slot` | kenmerkenband + CTA | alle zes |

De volgorde verschilt per pagina (bijvoorbeeld specs vóór of ná de aanpak), zodat
twee blokken van dezelfde vorm niet op elke pagina op dezelfde plek staan.

## Overzichten (`bouw_overzichten.py`)

`armaturen.html` en `diensten.html`: `.paginahero--patroon`, intro-band,
`.panel-row--3` met `.panel--beeld` ("kies op situatie"), daarna een `vlakkenrij`
(armaturen: wat alle armaturen delen) of een `trap` (diensten: de vier stappen),
FAQ en slotblok.

## Projecten (`bouw_projecten.py`)

**`projecten.html`**: `.paginahero--patroon`, intro, twee filtergroepen
(toepassing en product, `projecten.js`), telling in `aria-live`, kaartraster
(`.case-kaart`, 16:10-beeld), lege-staat, FAQ, slotblok. De kaarten staan in de
HTML en worden alleen verborgen.

**`project-<slug>.html`**: één template, statisch gebouwd uit `PROJECTEN`.

| id | component |
|---|---|
| `s01-introductie` | `.service-hero` met foto, sluier en twee knoppen (naar het product, naar contact) |
| `s02-kenmerken` | `.kerncijfers`: tot vier feiten; een woord als waarde krijgt `.kerncijfer__getal--tekst` |
| `s03-project` | `.case-lead`: wat het is, in leadformaat |
| `s04-toegepast` | `.case-blok` met `.case-lijst`: wat er is toegepast |
| geen | `.case-bleed`: beeld over de volle breedte (0 tot 3 keer) |
| `s05-product` | `.case-blok`: het toegepaste product met knop |
| `s06-verwant` | twee andere projecten als `.cases-grid__row` |
| `s07-contact` | het gedeelde contactblok, onderwerp voorgeselecteerd op het product |

Geen citaat, geen "uitdaging" en geen "resultaat": die staan niet op de bron.

## Over ons en contact

| pagina | secties |
|---|---|
| `over-ons.html` | `.paginahero` met foto · statement (de zin van de bronsite) · `vlakkenrij` met vier uitgangspunten · werkwijze als vier `beeldkaart()` · `.streamer--employee` · samenwerking (`panel-row--3`, Atelier LEK) · FAQ · slotblok |
| `contact.html` | `.paginahero--patroon` · formulier met aanloop links · **reviews direct onder het formulier** (quoteslider) · `vlakkenrij` met telefoon, e-mail, bezoekadres, bedrijfsgegevens |
| `privacybeleid.html`, `cookies.html` | `.tekstband` met één leeskolom |

## Het slotblok: kenmerkenband en CTA

| component | wat |
|---|---|
| `.logo-slider` | doorlopende band met de drie badges van de bronsite (Made in Holland, 5 jaar garantie, IK10) afgewisseld met tekstkenmerken (`.logo-slider__tekst`). De reeks staat er twee keer in; pauzeert bij hover en focus, staat stil bij `prefers-reduced-motion`. Klantlogo's kunnen in `KENMERKEN` worden toegevoegd. |
| `.cta-slot` | één vlak over de volle breedte met het merkpatroon, kop, tekst, de knop en een belregel (`.cta-slot__bel`) |

`slotblok("11")` levert `s11-kenmerken` en `s12-contact`.

## Beeld

- Elke foto is een `<picture>` met AVIF en WebP in een maatladder (`foto()` in
  `schil.py`, gegevens in `fotos.json`). `width`/`height` staan erbij tegen
  verspringen.
- Vaste beeldvakken (kaarten 16:10, hero's, quotes) gebruiken `object-fit: cover`;
  vrijstaand beeld houdt zijn verhouding.
- **Dezelfde foto staat nooit twee keer op één pagina.** De sleutels per pagina
  zijn daarop gekozen; de twee foto's in de uitklapper van het menu worden
  daarom nergens anders gebruikt. Een statische controle hierop staat in het
  QA-log van `work/migration-state.md`.
