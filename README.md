# Lebenslauf - Daniel Glaser

[![Build PDF and Create Release](https://github.com/the78mole/cv/actions/workflows/build-and-release.yml/badge.svg?branch=master)](https://github.com/the78mole/cv/actions/workflows/build-and-release.yml)
[![Latest Release](https://img.shields.io/github/v/release/the78mole/cv)](https://github.com/the78mole/cv/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PDF Download](https://img.shields.io/badge/PDF-Download-blue)](https://github.com/the78mole/cv/releases/latest)
[![LaTeX](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![GitHub last commit](https://img.shields.io/github/last-commit/the78mole/cv)](https://github.com/the78mole/cv/commits/master)
[![GitHub repo size](https://img.shields.io/github/repo-size/the78mole/cv)](https://github.com/the78mole/cv)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

> **Automatisch generierter LaTeX-Lebenslauf mit CI/CD Pipeline**

Dieses Repository enthält meinen professionellen Lebenslauf als LaTeX-Dokument mit vollständiger Automatisierung:

## 🚀 Features

- **📄 LaTeX-basierter Lebenslauf** mit moderncv-Klasse
- **🔄 Automatische PDF-Generierung** bei jedem Commit
- **📦 Automatische Releases** mit semantischer Versionierung
- **🎯 Aktuelle Positionen-Extraktion** für Release Notes
- **✅ Pre-commit Hooks** für Code-Qualität
- **🐳 Docker-basierte LaTeX-Kompilierung**

## 📋 Workflow

1. **Push auf `master`** → Automatische PDF-Generierung
2. **Semantic Versioning** basierend auf Commit-Messages
3. **Release Creation** mit:
   - Versioniertem PDF
   - Aktuellen CV-Positionen
   - Changelog-Link
4. **Artifact Upload** für GitHub Actions

## 🛠 Technologie-Stack

- **LaTeX**: Dokumentenerstellung mit `moderncv`
- **Python**: CV-Extraktion mit `TexSoup` und `uv`
- **GitHub Actions**: CI/CD Pipeline
- **Docker**: Isolierte LaTeX-Umgebung (`xu-cheng/texlive-full`)
- **Pre-commit**: Code-Qualität mit Black, isort, flake8, latexindent

## 📥 Latest PDF

Der aktuelle Lebenslauf ist immer verfügbar:

[![Download Latest PDF](https://img.shields.io/badge/Download-Latest%20PDF-green?style=for-the-badge)](https://github.com/the78mole/cv/releases/latest)

## 🔧 Lokale Entwicklung

### Voraussetzungen

- LaTeX-Distribution (TeX Live empfohlen)
- Python 3.9+ mit `uv`
- `make` für Build-Automatisierung

### Setup

```bash
# Repository klonen
git clone https://github.com/the78mole/cv.git
cd cv

# Pre-commit hooks installieren
uv tool install pre-commit
uv tool install detect-secrets
pre-commit install

# Python-Tools installieren
cd scripts
uv sync
```

### Build-Befehle

```bash
# PDF generieren
make pdf

# Aufräumen
make clean

# Aktuelle Positionen extrahieren
cd scripts && uv run extract-current ../Lebenslauf.tex
```

## 📊 Project Structure

```text
cv/
├── .github/
│   └── workflows/
│       ├── build-and-release.yml  # Haupt-CI/CD Pipeline
│       └── pre-commit.yml         # Code-Qualität Checks
├── scripts/
│   └── src/cv_tools/
│       └── extract_current.py     # CV-Extraktion Tool
├── Lebenslauf.tex                 # LaTeX-Hauptdokument
├── Makefile                       # Build-Automatisierung
└── .pre-commit-config.yaml        # Code-Qualität Konfiguration
```

## 🤝 Contributions

Dieses Repository ist primär für meinen persönlichen Lebenslauf gedacht, aber Feedback und
Verbesserungsvorschläge für die Automatisierung sind willkommen!

## 📜 License

Dieses Projekt steht unter der [MIT License](LICENSE).

---

**🔄 Automatisch aktualisiert** | **✨ Made with LaTeX & GitHub Actions**
