# Merkpatroon

Twee verloopbeelden van rood naar oranje, aangeleverd door Jesse op 7 oktober
2026 (`bron/verloop-breed.webp` 2000×528 en `bron/verloop.webp` 1439×940).
Daaruit zijn met Pillow (cover-uitsnede, WebP kwaliteit 82) deze bestanden
gemaakt:

| bestand | maat | bron | waar |
|---|---|---|---|
| `hero-patroon-{720,1000,1440}.webp` | 1,53:1 | verloop | `.paginahero--patroon` vanaf 768px (armaturen, diensten, projecten, contact) |
| `hero-patroon-mobiel-{720,800,1440}.webp` | 1:1 | verloop, middenuitsnede | dezelfde hero onder 768px, als band boven de titel |
| `cta-patroon-{1440,2880}.webp` | 3,8:1 | verloop-breed | achtergrond van het slotblok (`.cta-slot__hoofd`) |

In het slotblok ligt er een donkere aanloop over (0% boven, 45% onder), omdat
wit op het lichte oranje onderin anders onder de contrasteis zakt. De hero's
dragen geen tekst op het beeld.

Decoratief: in de HTML met `alt=""` en `aria-hidden`, in het slotblok als
achtergrond. Vervangen kan door de bestanden te overschrijven in dezelfde maten.
