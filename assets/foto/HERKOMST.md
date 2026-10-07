# Herkomst van de foto's

Alle foto's in deze map zijn van De Licht Fabriek zelf en komen van
https://www.delichtfabriekbv.nl/ (wp-content/uploads, opgehaald 7 oktober 2026).
Het zijn eigen project- en productfoto's; er staat geen stockfotografie tussen.

## Bewerking

De originelen dragen ingebrande bijschriften bovenaan ("Titan HE in 2200K ...") en
een watermerk "De Licht Fabriek" rechtsonder. Die zijn eraf gesneden: bij de
meeste liggende foto's 8% van boven en 10% van onder; bij enkele beelden met een
groter bijschrift of een ingezette foto (Citylight 2025) meer. De maten per
sleutel staan in `_generator/fotos.json`.

Daarna zijn ze verkleind naar een maatladder en weggeschreven als WebP (kwaliteit
80) en AVIF (kwaliteit 58):

| ladder | breedtes | waarvoor |
|---|---|---|
| band | 480, 800, 1200, 1800, 2400 | hero's en beeld over de volle breedte |
| kaart | 480, 800, 1200 | kaarten, galerij, citaten |
| klein | tot de bronbreedte | bronnen kleiner dan 1200px |

De pijplijn (`beeld.py`, scratch) leest de originelen, snijdt, schaalt en schrijft
`fotos.json`. Een foto vervangen: zelfde sleutel, zelfde breedtes, en de regel in
`fotos.json` bijwerken als de verhouding verandert.

## Sleutels en bronbestanden

Zie `_generator/fotos.json`: per sleutel staat het bronbestand (`bron`), de
breedtes, de maat van de grootste en kleinste variant en de alt-tekst.

Badges (`badge-made-in-holland`, `badge-garantie`, `badge-ik10`) zijn de drie
beeldmerken van de bronsite, ongewijzigd behalve het formaat.

## Licentie

Eigen materiaal van De Licht Fabriek B.V. De thermografiebeelden
(`thermo-*`) staan op de bronsite maar zijn klein (500 tot 1232px); zie
`image-replacements.json` voor de vervanging.
