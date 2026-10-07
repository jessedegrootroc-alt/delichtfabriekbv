# Herkomst van de herofilm

`hero-licht.mp4`: aangeleverd door Jesse op 7 oktober 2026 als
`Create_ONE_complete_professional_promotional_20261007191415.mp4` (1280×720,
24 fps, 10 s, met geluid, 4,2 MB). Het is gegenereerd promotiemateriaal met
sfeerbeelden van straatverlichting, een LED-module, een brug, een monteur en
een plein; het zijn geen opnamen van projecten van De Licht Fabriek en de
film wordt ook niet zo gepresenteerd.

Omgezet voor het web met ffmpeg: geluid eraf, H.264 crf 26, yuv420p,
faststart, 1280×720, 1,35 MB. Het eerste beeldje staat als foto
`hero-video-poster` in `assets/foto/` en is het stilstaande beeld onder de
film, zodat het begin niet verspringt.

Laadgedrag staat in `site.js` (herovideo): de bron wordt pas ingehangen als
`prefers-reduced-motion` uit staat, databesparing uit staat en de lijn geen 2G
is; zichtbaar vanaf `playing`.
