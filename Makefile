# Makefile für LaTeX-Dokument

# Variablen
TEXFILE = Lebenslauf
PDFLATEX = pdflatex
PUBDIR = /home/daniel/GDrive/Dokumente/Daniel/Beruf/Lebenslauf/
PUBNAME = Lebenslauf Daniel Glaser

# Standard-Target
.PHONY: pdf clean all

# PDF erstellen
pdf:
	$(PDFLATEX) $(TEXFILE).tex
	$(PDFLATEX) $(TEXFILE).tex

publish: pdf
	DATE=$$(date +%Y-%m-%d); cp $(TEXFILE).pdf "$(PUBDIR)/$${DATE} - $(PUBNAME).pdf"

pub: publish

# Hilfsdateien löschen
clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.fls *.fdb_latexmk *.synctex.gz

# Alles löschen (inklusive PDF)
distclean: clean
	rm -f $(TEXFILE).pdf

# Alles neu erstellen
all: clean pdf
