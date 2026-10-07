/* ============================================================================
   projecten.js: de filters op het projectenoverzicht
   ----------------------------------------------------------------------------
   Twee groepen filterpillen: toepassing en product. Binnen een groep geldt er
   één tegelijk, en de eerste pil ('alle') zet de groep weer open. De kaarten
   staan gewoon in de HTML en worden alleen verborgen, dus zonder JavaScript
   zie je alle projecten.

   Alles in één functie, zodat het bestand opnieuw uitgevoerd kan worden na een
   pagina-overgang.
   ========================================================================== */

(() => {
  /* Tijdens een overgang staan twee pagina's in de DOM; zoek binnen de eigen. */
  const container = document.currentScript?.closest('[data-barba="container"]') || document;

  const raster = container.querySelector('#projectRaster');
  if (!raster) return;

  const telling = container.querySelector('.cases-overzicht__telling');
  const leeg = container.querySelector('.cases-overzicht__leeg');
  const keuze = { toepassing: 'alles', product: 'alles' };

  const werkBij = () => {
    const kaarten = [...raster.querySelectorAll('.case-kaart')];
    let zichtbaar = 0;
    kaarten.forEach((k) => {
      const past = (keuze.toepassing === 'alles' || k.dataset.toepassing === keuze.toepassing)
                && (keuze.product === 'alles' || k.dataset.product === keuze.product);
      k.hidden = !past;
      if (past) zichtbaar++;
    });

    /* De achtergrond van een kaart wisselt om en om; omdat er kaarten
       wegvallen, wordt die wisseling opnieuw geteld over wat er overblijft. */
    let n = 0;
    kaarten.forEach((k) => {
      if (k.hidden) return;
      k.classList.toggle('is-even', n % 2 === 1);
      n++;
    });

    if (telling) {
      telling.textContent = zichtbaar === kaarten.length
        ? `${kaarten.length} projecten`
        : `${zichtbaar} van ${kaarten.length} projecten`;
    }
    if (leeg) leeg.hidden = zichtbaar > 0;
    window.ScrollTrigger?.refresh();
  };

  container.querySelectorAll('.filter-pil').forEach((p) => {
    p.addEventListener('click', () => {
      const groep = p.dataset.filter;
      keuze[groep] = p.dataset.waarde;
      container.querySelectorAll(`.filter-pil[data-filter="${groep}"]`).forEach((q) => {
        const aan = q === p;
        q.classList.toggle('is-actief', aan);
        q.setAttribute('aria-pressed', String(aan));
      });
      werkBij();
    });
  });

  werkBij();
})();
