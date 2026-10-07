# Merkpatroon

Twee verloopbeelden van rood naar oranje, aangeleverd door Jesse op 7 oktober
2026 (`bron/verloop-breed.webp` 2000×528 en `bron/verloop.webp` 1439×940).
Op verzoek verticaal gespiegeld (oranje boven, rood onder). Daaruit zijn met
Pillow (cover-uitsnede, WebP kwaliteit 82) deze bestanden gemaakt:

| bestand | maat | bron | waar |
|---|---|---|---|
| `hero-patroon-{720,1000,1440}.webp` | 1,53:1 | verloop | `.paginahero--patroon` vanaf 768px (armaturen, diensten, projecten, contact) |
| `hero-patroon-mobiel-{720,800,1440}.webp` | 1:1 | verloop, middenuitsnede | dezelfde hero onder 768px, als band boven de titel |
| `cta-patroon-{1440,2880}.webp` | 3,8:1 | verloop-breed | achtergrond van het slotblok (`.cta-slot__hoofd`) |

Er ligt geen waas over de verlopen. In het slotblok staan label, kop en tekst
daarom in de donkere tekstkleur (het oranje bovenin is te licht voor wit); alleen
de belregel onderin, op het rood, is wit. De hero's dragen geen tekst op het beeld.

Decoratief: in de HTML met `alt=""` en `aria-hidden`, in het slotblok als
achtergrond. Vervangen kan door de bestanden te overschrijven in dezelfde maten.
