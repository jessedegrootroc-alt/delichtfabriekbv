# De Licht Fabriek: website

Statische site voor De Licht Fabriek B.V. (Wormerveer): HTML, CSS en vanilla
JavaScript, geen build-stap en geen npm-afhankelijkheden. Van een CDN komen alleen
GSAP (met ScrollTrigger en ScrollSmoother) en Barba.js: samen doen die de
pagina-overgangen en het vloeiende scrollen.

De site is een ombouw van een bestaande template (het ontwerpsysteem in
`STYLEGUIDE.md` en `SECTIONS.md`) naar de inhoud van https://www.delichtfabriekbv.nl/.
Het werkdocument van die ombouw, met de bronfeiten per URL, staat in
`work/migration-state.md`.

## Lokaal draaien

Open `index.html` in de browser, of draai een server vanuit deze map:

    npx serve -l 5500 .

Alle links zijn relatief, dus de map kan zonder aanpassing als eigen site
gepubliceerd worden.

## Publiceren

Statisch, werkt zonder configuratie op GitHub Pages, Netlify, Vercel of Cloudflare
Pages: wijs de host naar deze map. Het domein staat in `_generator/schil.py`
(`BASIS`); canonical, Open Graph, `sitemap.xml` en `robots.txt` volgen daaruit bij
het bouwen. `.vercelignore` houdt de iconenset (3185 svg's, alleen nodig bij het
bouwen) buiten de upload.

## Structuur

```
index.html                Home
armaturen.html            overzicht
  solarbolder.html        ┐
  tunnelarmaturen.html    ├ drie armatuurpagina's, één sectieskelet (bouw_detail.py)
  paaltop-armaturen.html  ┘
diensten.html             overzicht
  retrofit.html           ┐
  maatwerk.html           ├ drie dienstpagina's, hetzelfde skelet met andere blokken
  thermolight.html        ┘
projecten.html            overzicht met filters op toepassing en product
project-<slug>.html       twintig projectpagina's, één sectieskelet
over-ons.html  contact.html  privacybeleid.html  cookies.html

STYLEGUIDE.md             het ontwerpsysteem en de kleuren van De Licht Fabriek
SECTIONS.md               het sectieskelet dat de pagina's delen
CONTENT-TODO.md           wat er nog van de opdrachtgever moet komen
image-replacements.json   beeldposities met een tijdelijk of te klein beeld
work/migration-state.md   bronfeiten, sitemap, contentmapping, QA-log

styleguide.css            tokens en componenten, geldt overal
index.css  service.css  projecten.css  contact.css  over-ons.css  tekstpagina.css
cookiebalk.css  transitions.css

site.js                   header, mobiel paneel, accordeons, quoteslider, op elke pagina
contactformulier.js       het contactformulier, één keer
index.js                  alleen de tellers op de homepage
projecten.js              de filters op het projectenoverzicht
smooth-scroll.js          vloeiend scrollen met GSAP ScrollSmoother
page-transitions.js       Barba.js + GSAP
cookiebalk.js  analytics.js

assets/foto               eigen foto's van De Licht Fabriek, WebP + AVIF in maatladders
assets/logo  favicon  patronen  social  fonts  iconen
sitemap.xml  robots.txt   gegenereerd
```

## Werken aan deze site

- **De HTML is gegenereerd.** Alle pagina's komen uit `_generator/`; pas je een
  pagina met de hand aan, dan is dat weg bij de volgende bouw. Bouwen:

      cd _generator && python3 bouw_alles.py

  Inhoud staat in `schil.py` (bedrijfsgegevens, aanbod, projecten, menu),
  `inhoud_armaturen.py`, `inhoud_diensten.py`, `bouw_home.py`,
  `bouw_overzichten.py`, `bouw_projecten.py` en `bouw_contact.py`.
- **Foto's** staan geregistreerd in `_generator/fotos.json` (maten en alt-teksten)
  en komen uit `assets/foto/`. Hoe ze gemaakt zijn staat in `assets/foto/HERKOMST.md`.
  Een nieuwe foto: zelfde bestandsnaamschema (`<sleutel>-<breedte>.webp` en `.avif`)
  en een regel in `fotos.json`.
- Lees `SECTIONS.md` voordat je een sectie aanpast; pagina's van hetzelfde type
  delen hun structuur.
- Nieuwe kleuren, maten of afstanden komen uit de tokens in `styleguide.css`.
- Het contactformulier verstuurt nog niets: zet het endpoint in `contactformulier.js`.
- Statistieken laden pas na toestemming en alleen als er een meet-ID staat in
  `analytics.js`. Dat veld is nu bewust leeg.
