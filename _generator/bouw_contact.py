# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *

# ============================================================ contact.html
# Flow: intro en geruststelling -> gegevens -> formulier -> reviews direct
# onder het formulier -> gegevensvlakken. Geen reactietijd: die staat niet op
# de bron en wordt niet verzonnen.
inhoud = f'''{patroonhero("01", "contact", "Contact", "Contact")}

  <section class="band background--white" id="s02-formulier">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <div class="article-body">
            <p>Vertel kort om welke plek het gaat en wat er nu hangt of staat. Een foto, een tekening of de maten van een sparing helpen ons om meteen gericht mee te denken.</p>
            <p>Na je bericht nemen we contact op om de vraag door te spreken. Daarna volgt een voorstel of een prijsopgave.</p>
          </div>
          <p class="contact-direct">Liever meteen iemand spreken? Bel
            <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a> of mail naar
            <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>

        <div class="col-lg-8 col-12">
          <div class="contact-formulier-wikkel">
            <div data-contactformulier data-onderwerp="overig"></div>
            <noscript>
              <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
                <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
            </noscript>
          </div>
        </div>
      </div>
    </div>
  </section>

{quoteslider("03", "reviews", "Wat opdrachtgevers zeggen", "Uit de samenwerking", [
    ("Het armatuur is precies gemaakt op de maten van onze onderdoorgang. Tekening, proefmontage en plaatsing liepen via één aanspreekpunt.",
     "Beheerder openbare verlichting", "gemeente", "citylight-kerk", None),
    ("Voor het verledden van bestaande armaturen kregen we een geartray die zonder aanpassingen paste. Dat scheelde een complete vervanging.",
     "Projectleider", "installatiebedrijf", "tunnel-gebogen-b", None),
    ("De Solarbolder staat waar geen kabel ligt. Ontwerp en uitvoering sloten goed op elkaar aan.",
     "Lichtontwerper", "ontwerpbureau", "tuin-schielandhuis-2", None),
])}

{vlakkenrij("04", "gegevens", "Onze gegevens", [
    ("Telefoon",
     f'<a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a><br>Op werkdagen bereikbaar'),
    ("E-mail",
     f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
    ("Bezoekadres",
     f"{BEDRIJF_JURIDISCH}<br>{STRAAT}<br>{POSTCODE} {PLAATS}"),
    ("Bedrijfsgegevens",
     f"KvK {KVK}<br>BTW {BTW}"),
])}
'''

(UIT / "contact.html").write_text(pagina(
    bestand="contact.html",
    titel="Contact | De Licht Fabriek",
    omschrijving=f"Neem contact op met De Licht Fabriek in Wormerveer over armaturen, retrofit of maatwerk. Bel {TELEFOON_WEERGAVE} of mail {EMAIL}.",
    namespace="contact",
    pagina_css="contact.css",
    css_naam="contact",
    inhoud=inhoud,
), encoding="utf-8")

# ======================================================= tekstpagina's
PRIVACY = f'''  <section class="tekstband" id="s01-privacybeleid">
    <div class="container">
      <div class="tekst">
        <p class="meta">Juridisch</p>
        <h1>Privacybeleid</h1>
        <p class="meta">Laatst bijgewerkt: <span class="invulveld">nog invullen</span></p>

        <h2>Wie verwerkt je gegevens</h2>
        <p>{BEDRIJF_JURIDISCH}, {STRAAT}, {POSTCODE} {PLAATS}, KvK {KVK}. Voor vragen over dit beleid kun je terecht bij <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2>Welke gegevens en waarom</h2>
        <h3>Contactformulier</h3>
        <p>Vul je het formulier in, dan verwerken we je naam, bedrijfsnaam, e-mailadres, telefoonnummer, het gekozen onderwerp en je bericht. Die gegevens gebruiken we alleen om je vraag te beantwoorden en, als dat tot een opdracht leidt, om die uit te voeren.</p>
        <p>Grondslag: je toestemming, en bij een lopende opdracht de uitvoering van de overeenkomst.</p>

        <h3>Bezoekgegevens</h3>
        <p>De site plaatst geen analytische of marketingcookies zolang je daar geen toestemming voor geeft. Je keuze zelf bewaren we in de lokale opslag van je browser onder de naam <span class="invulveld">dlf-cookies-v1</span>. Dat is geen cookie: het gaat niet mee naar de server.</p>

        <h2>Hoe lang we het bewaren</h2>
        <p>Berichten via het formulier bewaren we tot twee jaar na het laatste contact. Gegevens die bij een opdracht horen bewaren we zolang de wet dat vraagt, voor de administratie zeven jaar.</p>

        <h2>Met wie we het delen</h2>
        <p>We verkopen geen gegevens. We delen ze alleen met partijen die nodig zijn om te leveren, zoals de partij die deze site host.</p>
        <div class="invulblok">
          <p>De hostingpartij moet hier met naam genoemd worden, met de vermelding of er een verwerkersovereenkomst ligt.</p>
        </div>

        <h2>Je rechten</h2>
        <p>Je mag je gegevens inzien, corrigeren of laten verwijderen, en je mag bezwaar maken tegen de verwerking. Stuur een mail naar <a href="mailto:{EMAIL}">{EMAIL}</a>; we reageren binnen een maand. Ben je het niet eens met hoe we ermee omgaan, dan kun je klagen bij de Autoriteit Persoonsgegevens.</p>

        <h2>Beveiliging</h2>
        <p>De site gaat over https en de gegevens uit het formulier komen alleen terecht bij wie ze nodig heeft.</p>
        <div class="invulblok">
          <p>Beschrijf hier alleen de maatregelen die daadwerkelijk zijn ingericht. Wat er nog niet is, hoort er niet in te staan.</p>
        </div>
      </div>
    </div>
  </section>'''

(UIT / "privacybeleid.html").write_text(pagina(
    bestand="privacybeleid.html",
    titel="Privacybeleid | De Licht Fabriek",
    omschrijving="Hoe De Licht Fabriek omgaat met de gegevens uit het contactformulier en e-mail: waarvoor we ze gebruiken, hoe lang we ze bewaren en welke rechten je hebt.",
    namespace="privacybeleid",
    pagina_css="tekstpagina.css",
    css_naam="tekst",
    inhoud=PRIVACY,
    body_klasse="tekstpagina",
), encoding="utf-8")

COOKIES = f'''  <section class="tekstband" id="s01-cookies">
    <div class="container">
      <div class="tekst">
        <p class="meta">Juridisch</p>
        <h1>Cookies</h1>
        <p class="meta">Laatst bijgewerkt: <span class="invulveld">nog invullen</span></p>

        <h2>Wat deze site plaatst</h2>
        <p>Op dit moment plaatst deze website geen analytische of marketingcookies. Er draait geen statistiekentool en er staat geen advertentiepixel op de pagina.</p>
        <p>Het enige dat wordt opgeslagen is je eigen keuze in de cookiemelding. Die bewaren we in de lokale opslag van je browser onder de naam <span class="invulveld">dlf-cookies-v1</span>, zodat je de vraag niet bij elk bezoek opnieuw krijgt.</p>

        <h2>De drie categorie&euml;n</h2>
        <h3>Functioneel</h3>
        <p>Nodig om de site te laten werken, waaronder het onthouden van je keuze. Hiervoor is geen toestemming vereist.</p>
        <h3>Analytisch</h3>
        <p>Bedoeld om te zien welke pagina&rsquo;s bezocht worden, zodat de site verbeterd kan worden. Er staat een statistiekentool klaar die pas laadt nadat je analytische cookies hebt aangezet.</p>
        <div class="invulblok">
          <p>Welke statistiekentool er gebruikt gaat worden en welk meet-ID daarbij hoort, moet hier nog ingevuld worden. Zolang dat veld leeg is, laadt er niets.</p>
        </div>
        <h3>Marketing</h3>
        <p>Voor advertenties en het meten van het effect daarvan. Op dit moment niet in gebruik.</p>

        <h2>Je keuze wijzigen</h2>
        <p>Je kunt je keuze op elk moment aanpassen of intrekken.</p>
        <p><button type="button" class="cookie-knop cookie-knop--donker" data-cookie-instellingen>Cookie-instellingen openen</button></p>

        <h2>Wat er verder gebeurt</h2>
        <p>De pagina laadt de scripts voor de pagina-overgangen van een extern adres. Dat zet geen cookies, maar ontvangt wel het IP-adres van je bezoeker:</p>
        <ul>
          <li>cdn.jsdelivr.net</li>
        </ul>
        <p>De lettertypen staan op onze eigen server; daar gaat dus niets naartoe. Meer over gegevens staat in het <a href="privacybeleid.html">privacybeleid</a>.</p>
      </div>
    </div>
  </section>'''

(UIT / "cookies.html").write_text(pagina(
    bestand="cookies.html",
    titel="Cookies | De Licht Fabriek",
    omschrijving="Welke cookies de site van De Licht Fabriek plaatst, waarvoor ze dienen en hoe je je keuze voor statistieken op elk moment aanpast of intrekt.",
    namespace="cookies",
    pagina_css="tekstpagina.css",
    css_naam="tekst",
    inhoud=COOKIES,
    body_klasse="tekstpagina",
), encoding="utf-8")

print("contact.html, privacybeleid.html en cookies.html geschreven")
