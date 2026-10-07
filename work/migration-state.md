# Migratie template → De Licht Fabriek B.V.

Werkdocument. Kort, feitelijk, bijgewerkt per fase. Bron: https://www.delichtfabriekbv.nl/ (WordPress/Blocksy, opgehaald 7 oktober 2026).

## Besluit over de plek

De template is de MADEGRO-site (`../madegro`, live voor een andere klant). Die blijft ongemoeid. De ombouw staat in deze map `lichtfabriek/`, als kopie van de template met eigen git-historie. Zelfde stack: statische HTML uit `_generator/*.py`, geen build, GSAP/Barba van jsDelivr.

## Fase 1: bronfeiten per URL

| URL | Feiten |
|---|---|
| `/` | Titel: "LEDverlichting in de gebieden: Openbare Verlichting, Outdoor en Solar – LEDverlichting, Ontwerp, Engineering, Productie, installatie, retrofit oplossingen, Custom made oplossingen." Kop: "Innovatieve LED-oplossingen waar design en functionaliteit naadloos samenkomen". Drie USP's: Maatwerk (op maat, afgestemd op project, wensen, technische eisen), Duurzaam gedacht (energiezuinig, lange levensduur, minimale impact, circulair ontwerp), Slim licht (past zich automatisch aan, bespaart energie, comfort en efficiëntie). Galerij met projectfoto's. Tel. +31 6 28553641. |
| `/solarbolder/` | Offgrid staand armatuur, geeft 365 dagen per jaar licht; werkt los van het elektriciteitsnet, alleen zon en daglicht nodig. Bedacht en ontworpen door Iris Dijkstra van Atelier LEK (atelierlek.nl); samen met Atelier LEK omgezet in een duurzaam gefabriceerde Solarbolder. Geproduceerd in Nederland; RVS, terrazzo, duurzame elektronica. Foto's: Crooswijk Rotterdam (3000K, terrazzo reflector), Schielandhuis Rotterdam (tuin, reflector terrazzo wit carrara, zonnepaneel in RVS met poedercoat), amber LED met azobé reflector. |
| `/tunnelarmaturen/` | In eigen beheer ontworpen en geproduceerd op klantspecificatie; "tot op heden geen uitdaging te groot". Vaak RVS-behuizing + polycarbonaat venster. Poedercoating in standaard RAL of klantwens. Venster: transparant, boomschorseffect of opaal (LTA 82%; LTA = lichttransmissiewaarde). Optioneel antigraffiticoating op behuizing en venster, onzichtbaar na aanbrengen. LED-kleuren standaard 2200K/3000K/4000K, afwijkend op aanvraag. Drivers: Aan/Uit, DALI/DALI SR, 1-10V, Dynadimmer (standaard 3A-dimregime of klantspecifiek). Productnaam uit foto's: Titan (HE = High Efficiency, UHE = Ultra High Efficiency, 60°-optiek, IK10). |
| `/paaltop-armaturen/` | Citylight: stijlvol, modern paaltoparmatuur; duurzaam slagvast polycarbonaat; efficiënte LED; reeks aanpasbare optieken (T2/T3/T4 op foto) voor optimale, uniforme lichtspreiding. Zelfde LED-kleuren en driveropties als tunnelarmaturen. Foto's: Beverwijk Wijkertoren, speelplaats, straat, Citylight mini, Fusion360-ontwerp. |
| `/retrofit/`, `/armaturen/` | Alleen een kop, geen tekst. |
| `/geartray-tunnelarmatuur/` | Kop: "Innovatieve LED-geartrays, de naadloze samensmelting van nieuwe (lees efficiënte) en slimme hardware en functionaliteit". Foto's: custom LED-module 3000K 180 lm/W in buis; vervangende geartray "zeer efficiënt 200 lm/W" (DP Tuscan, 4000 lumen @ 22W, 3000K); verschil oude TL vs LED-module; retrofitmodule met slimme driver (Dynadimmer 3A). |
| `/geartray-schreder-valentino/`, `/geartray-schreder-albany/` | Alleen de kop (under construction). Bestaan als productvarianten; geen specificaties. Foto elders: "Schréder CDO 70W naar 2200K LED-module T3-optiek Dynadim 22W". |
| `/portfolio/` | "Hierbij afbeeldingen van gerealiseerde projecten." Alleen foto's; feiten uit bijschriften: Brug Buikslotermeer Amsterdam (trapopgang, 48V ELV); Brugverlichting Hoofddorp (ELV 54V DC, IK10); Citylight Beverwijk Wijkertoren; Citylight speelplaats/straat; Herstel trap-/brugverlichting Muziekgebouw aan het IJ / BIMhuis Amsterdam; aanlichting standbeeld Johan Cruijff (ArenA); UV-A lichtbak voor herstel kunstwerken (vergeling); TL naar LED met noodverlichting (DALI dimbaar, polycarbonaat); tunnels: Titan 2200K/3000K, dimregime 3A, antigraffiti, gebogen polycarbonaat afscherming, 2e-keus upgrade naar LED 2200K met nieuw venster, 22W geartray; Solarbolder Crooswijk en Schielandhuis; retrofit straatverlichting 2200K T3 16W; trapopgang met 360° grondspots en leuningverlichting (ELV 48V, IK10). |
| `/thermolight/` | "Met thermografisch onderzoek constateren wij snel en vakkundig afwijkingen. Dit kan zowel betrekking hebben op elektrische als warmtegerelateerde problemen." Voorbeelden getoond; contact voor informatie of prijsopgave. |
| `/contact/` | "De Licht Fabriek: waar de klantwens wordt vertaald naar een passende oplossing. Onze interne engineering en productie waarborgen de gewenste kwaliteit." Telefoon 06-28553641; bezoekadres Rosbayerweg 19, 1522 RW Wormerveer; info@delichtfabriekbv.nl; KvK 72963204; BTW NL859301655B01; bank NL44 INGB 0008 9398 15. |
| Badges (beeld) | "Made in Holland", "Made in Holland · 5 jaar garantie" (eigen badge), "IK10 rated". |

Niet op de bron: oprichtingsjaar, teamgrootte, namen van medewerkers, klantnamen/opdrachtgevers, reviews, certificeringen (anders dan IK10-claim), prijzen, levertijden. Die worden niet verzonnen.

Merk: logo zwart lijnwerk (lamp met fabriekssilhouet) + serif-woordmerk; themapalet oranje `#ff6310`/`#fd7c47`, grijs `#687279`, donker `#111518`, lichtgrijs `#E9EBEC`/`#F4F5F6`. Lettertype op de bron is themastandaard (Nunito Sans), geen huisstijlkeuze; de template houdt Inter Tight.

## Fase 2: doelgroep en conversie

- **Primair (B2B):** gemeenten en provincies (beheerders openbare verlichting, projectleiders civiele kunstwerken), aannemers/installateurs OVL, lichtontwerpers en architecten, beheerders van gebouwen en terreinen. Beslisser: beheerder/projectleider; beïnvloeder: ontwerper, installateur.
- **Koopfase:** oriënterend ("kan dit op maat?", "past dit in ons bestaande armatuur?") tot concreet (aanbesteding, vervanging TL/CDO, nieuwe tunnel/brug). Voorkennis technisch gemiddeld tot hoog: men kent K-waarden, DALI, dimregimes, IK-klassen.
- **Job to be done:** verlichting die op maat past bij object en ontwerp, energiezuinig en dimbaar, bestand tegen vandalisme (IK10, antigraffiti), zonder netaansluiting waar geen kabel ligt (Solarbolder), met zekerheid over kwaliteit en garantie (Made in Holland, 5 jaar), en één partij voor ontwerp, engineering, productie en installatie.
- **Twijfels/bezwaren → bewijs:** "kan het op maat?" → tunnelarmaturen op klantspecificatie, Solarbolder met Atelier LEK, maatwerk-projecten (brug, trap, UV-lichtbak); "past het in ons bestaande armatuur?" → geartrays voor tunnelarmaturen en Schréder Valentino/Albany, CDO→LED; "hoe zit het met dimmen/sturing?" → Aan/Uit, DALI/DALI SR, 1-10V, Dynadimmer 3A; "vandalisme?" → IK10, polycarbonaat, antigraffiticoating; "garantie/kwaliteit?" → interne engineering en productie, Made in Holland, 5 jaar garantie; "wat is de volgende stap?" → situatie bespreken, prijsopgave aanvragen.
- **CTA's:** primair "Vraag een offerte aan" / "Bespreek je project" (contact); laagdrempelig "Bekijk de projecten", "Bel 06 28553641".

## Fase 3: template-inventaris (wat waarvoor dient)

| Template-onderdeel | Inzet voor DLF |
|---|---|
| `pagina()` schil, header met twee uitklappers, mobiel paneel, voet | Armaturen ▾ en Diensten ▾ in plaats van Diensten/Cursussen |
| Homepage (hero met foto/video, statement, tekst+uitlopend beeld, dienstkaarten, projectrijen, USP-tellers, kaarten van vier, quoteslider, FAQ, medewerkersband, logoband, CTA) | hero met eigen foto (geen film beschikbaar), 3 armatuurkaarten, 3 dienstkaarten (rij van vier → drie diensten + maatwerkkaart), projectrijen, cijfers met bron, placeholder-reviews, FAQ, bedrijfsband, kenmerkenband, CTA |
| Servicepagina (paginahero--hoog, statement, herkenningskaarten, trap, voordelen met iconen, partners, projecten, FAQ, slot) | productdetail (Solarbolder, Tunnelarmaturen, Paaltop) met specificatieblok; dienstdetail (Retrofit, Maatwerk, Thermolight) met wisselende secties |
| Cursusaanbod (patroonhero, intro, kaartraster, FAQ) | overzichten `armaturen.html` en `diensten.html` |
| Cases-overzicht met filters + casepagina | `projecten.html` met filters op toepassing en plaats; statische `project-*.html` zonder database |
| Over ons (paginahero, statement, vlakkenrij, beeldkaarten, band, samenwerking, FAQ) | over-ons met feiten van de bron; samenwerking = Atelier LEK |
| Contact (patroonhero, formulier, vlakkenrij) | + reviews direct onder het formulier (eis fase 13) |
| Logoband | kenmerkenband (badges en tekstmerken met feiten); klantlogo's zijn er niet |
| Dark mode, navigatiegradient | niet aanwezig in deze template (color-scheme light; balk wordt grijs bij scrollen) |

## Fase 4: sitemap

```
index.html
armaturen.html            overzicht
  solarbolder.html        Solarbolder (offgrid)
  tunnelarmaturen.html    Titan tunnelarmaturen
  paaltop-armaturen.html  Citylight paaltoparmatuur
diensten.html             overzicht
  retrofit.html           LED-geartrays en retrofit
  maatwerk.html           ontwerp, engineering, productie, installatie
  thermolight.html        thermografisch onderzoek
projecten.html            overzicht met filters
  project-<slug>.html     12 projecten uit het portfolio
over-ons.html
contact.html
privacybeleid.html  cookies.html
```

Vervalt uit de template: cursussen (4 + overzicht), cases uit Supabase, admin.html, case.js/cases.js, bibliotheek.json, vercel-redirects, MADEGRO-logo's en -partners.

## Fase 5/6: contentmapping en flow (kort)

| Pagina | Doel → flow |
|---|---|
| Home | herkenning (wie, voor wie) → wat we maken (3 armaturen) → wat we doen (diensten) → bewijs (projecten) → cijfers met bron → reviews (placeholder) → FAQ → over het bedrijf → kenmerken → CTA |
| Armaturen | welke past wanneer (3 kaarten met situaties) → wat alle armaturen delen (LED-kleur, sturing, materiaal, garantie) → FAQ → CTA |
| Productdetail | hero → statement → situaties (wanneer dit) → aanpak (van vraag tot plaatsing) → voordelen → opties/specificaties → projecten met dit product → FAQ → CTA |
| Diensten | retrofit of nieuw, maatwerk, thermografie: wat kies je wanneer |
| Dienstdetail | hero → statement → situaties → aanpak → wat het oplevert → voorbeeld (beeld) → projecten → FAQ → CTA |
| Projecten | filters → kaarten → FAQ → CTA |
| Project | hero → kenmerken (feiten) → wat er stond/wat gevraagd was (alleen waar bekend) → toegepast product → beelden → verwante projecten → contact |
| Over ons | hero → statement (bron) → waarden (uit USP's) → werkwijze (ontwerp, engineering, productie, installatie) → band → samenwerking Atelier LEK → FAQ → CTA |
| Contact | intro → formulier → reviews → gegevens |

## Status

- [x] Fase 1–6 vastgelegd
- [x] Fase 7–13 gebouwd: 34 pagina's (home, 2 overzichten, 3 armaturen, 3 diensten, projectenoverzicht, 20 projecten, over ons, contact, privacy, cookies)
- [x] Fase 14 `image-replacements.json` (Thermolight-hero en -galerij, klantlogo's optioneel)
- [x] Fase 15–21 QA, zie log

## QA-log (7 oktober 2026)

| Controle | Hoe | Resultaat |
|---|---|---|
| Links, assets, srcsets | statisch script over alle 34 html-bestanden | 0 ontbrekende bestanden, 0 dode interne links |
| Eén h1 per pagina, unieke title en description | idem | ok; descriptions ≤ 160 tekens, titles van enkele projecten 70–88 tekens (Google kapt af, geen fout) |
| Dubbele foto op één pagina | idem (sleutel per `<img>`) | 0 |
| Template-restanten in html/css/js | grep op MADEGRO, Martin, cursus, Supabase, lorem | 0 in html/js; css-commentaren opgeschoond |
| JavaScript-syntax | `node -e new Function(...)` over alle scripts | ok (na herstel van `window.DLF`) |
| Horizontale scroll | iframe-scan van 18 pagina's op 320, 375 en 768 px | nergens `scrollWidth > viewport`; alleen het mobiele paneel staat bewust buiten beeld |
| Desktop 1280 | screenshots per sectie: home (12 secties), tunnelarmaturen, project Schielandhuis, projecten, over ons, contact, retrofit | ok; h1 "Tunnelarmaturen" liep over het beeld → `hyphens: auto` + `&shy;`; kenmerken met een woord als waarde → `.kerncijfer__getal--tekst` |
| Desktop 1440 | tunnelarmaturen-hero | ok |
| Tablet 768 | home: kaarten, projectrijen, diensten | ok, kolommen stapelen zoals bedoeld |
| Mobiel 375 | home (hero, armaturen, projecten, band, kenmerken, CTA, voet), tunnelarmaturen (hero, trap, specs), project Buikslotermeer (hero, kenmerken), projecten (filters) | ok; Citylight-mini droeg nog een watermerk → strakker gesneden |
| Toegankelijkheid (home) | JS: alt op elk beeld, naam op elke knop/link, label bij elk veld, kopvolgorde, `lang`, skip-link | 0 beelden zonder alt, 0 naamloze knoppen, 0 velden zonder label; sprong h2→h4 in de voet → voetkoppen zijn h2 |
| Contrast | berekend op de tokens | nacht op wit 17,9:1; wit op leisteen 11,6:1; zwart op oranje 7,0:1; oranje wordt niet als tekstkleur gebruikt |
| Beeldgewicht | bestandsgroottes + netwerklog | hero 1800px AVIF ≈ 120 kB, 2400px ≈ 184 kB; de browser kiest AVIF; alle foto's lazy behalve de hero (`fetchpriority="high"`) |
| Formulier | contactpagina | zeven onderwerpen, labels, verplichte velden, akkoordvinkje; endpoint nog leeg (CONTENT-TODO) |
| Reduced motion | code | smoother uit, band stil, timer verborgen, tellers over (template) |
| Dark mode / navigatiegradient | n.v.t. | de template heeft geen dark mode en geen gradient in de balk; niet toegevoegd |

Niet uitvoerbaar: Lighthouse/LCP-meting in een echte browser (pane zonder meetgereedschap); echte browsers buiten Chromium.
