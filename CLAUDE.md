# Vorschau-Repo (Max Rathsack, Webseiten-Entwürfe)

Pflicht für JEDE Entwurf-Seite (Websiten/<Firma>/<Firma>-Entwurf-StilX.html):
- Direkt nach `<head>` einfügen: `<script src="../../assets/geraet.js"></script>`
  → am Computer erscheint der Entwurf automatisch in der Handy-Ansicht, auf dem Handy normal.
- Pro Firma eine Übersichtsseite `Websiten/<Firma>/index.html` mit allen 3 Entwürfen (nur dieser eine Link geht an Kunden).
- In der Kunden-Mail beim Link erwähnen: «Die Entwürfe funktionieren auf dem Handy und am Computer – am Computer sehen Sie sie in einer Handy-Ansicht, so wie Ihre Kunden die Seite sehen.»

Sicherheitsnetz: Die GitHub Action `.github/workflows/handyansicht.yml` ergänzt das Script nach jedem Push automatisch, falls es fehlt.
