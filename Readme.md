# Daniels Lebenslauf

## Debian prerequisites

    sudo apt-get install texlive texworks cm-super texlive-fonts-extra texlive-latex-extra texlive-lang-german

## Allgemein

Zur einfacheren Benutzung ist ein Makefile beigefügt. Folgende Targets sind verfügbar:

- `make pdf` : Erstellt das PDF aus der TeX-Datei.
- `make publish` : Kopiert das erstellte PDF in das GDrive-Verzeichnis
- `make clean` : Löscht Hilfsdateien, die bei der PDF-Erstellung entstehen.

## PDF erstellen

    pdflatex Lebenslauf.tex

oder

    make pdf

## PDF publizieren

Um den Lebenslauf in GDrive hochzuladen:

    make publish
