# -*- coding: utf-8 -*-
"""Bouwt alle pagina's, de sitemap en robots.txt. Gebruik dit en niet de losse
   scripts: de armatuur- en dienstpagina's worden gedreven door inhoud_*.py."""
import runpy, sys, pathlib, datetime
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))

for naam in ["bouw_home", "inhoud_armaturen", "inhoud_diensten",
             "bouw_projecten", "bouw_overzichten", "bouw_contact"]:
    print(f"--- {naam}")
    runpy.run_path(str(HIER / f"{naam}.py"), run_name="__main__")

# ------------------------------------------------------------ sitemap + robots
from schil import BASIS, PROJECTEN, ARMATUREN, DIENSTEN, UIT

vandaag = datetime.date.today().isoformat()
paginas = (["", "armaturen.html"] + [b for b, *_ in ARMATUREN]
           + ["diensten.html"] + [b for b, *_ in DIENSTEN]
           + ["projecten.html"] + [f'project-{p["slug"]}.html' for p in PROJECTEN]
           + ["over-ons.html", "contact.html", "privacybeleid.html", "cookies.html"])
regels = "\n".join(
    f"  <url><loc>{BASIS}/{p}</loc><lastmod>{vandaag}</lastmod></url>" for p in paginas)
(UIT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"{regels}\n</urlset>\n", encoding="utf-8")
(UIT / "robots.txt").write_text(
    f"User-agent: *\nAllow: /\n\nSitemap: {BASIS}/sitemap.xml\n", encoding="utf-8")
print(f"sitemap.xml ({len(paginas)} adressen) en robots.txt geschreven")
