# Resume - Daniel Glaser

[🇩🇪 Deutsch](README.md) | 🇺🇸 **English**

[![Build PDF and Create Release](https://github.com/the78mole/cv/actions/workflows/build-and-release.yml/badge.svg?branch=master)](https://github.com/the78mole/cv/actions/workflows/build-and-release.yml)
[![Latest Release](https://img.shields.io/github/v/release/the78mole/cv)](https://github.com/the78mole/cv/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PDF Download](https://img.shields.io/badge/PDF-Download-blue)](https://github.com/the78mole/cv/releases/latest)
[![LaTeX](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

> **Automatically generated LaTeX resume with CI/CD pipeline**

This repository contains my professional resume as a LaTeX document with complete automation:

## 🚀 Features

- **📄 LaTeX-based resume** using the moderncv class
- **🔄 Automatic PDF generation** on every commit
- **📦 Automated releases** with semantic versioning
- **🎯 Current positions extraction** for release notes
- **✅ Pre-commit hooks** for code quality
- **🐳 Docker-based LaTeX compilation**

## 📋 Workflow

1. **Push to `master`** → Automatic PDF generation
2. **Semantic versioning** based on commit messages
3. **Release creation** with:
   - Versioned PDF
   - Current CV positions
   - Changelog link
4. **Artifact upload** for GitHub Actions

## 🛠 Technology Stack

- **LaTeX**: Document creation with `moderncv`
- **Python**: CV extraction with `TexSoup` and `uv`
- **GitHub Actions**: CI/CD pipeline
- **Docker**: Isolated LaTeX environment (`xu-cheng/texlive-full`)
- **Pre-commit**: Code quality with Black, isort, flake8, latexindent

## 📥 Latest PDF

The current resume is always available:

[![Download Latest PDF](https://img.shields.io/badge/Download-Latest%20PDF-green?style=for-the-badge)](https://github.com/the78mole/cv/releases/latest)

## 🔧 Local Development

### Prerequisites

- LaTeX distribution (TeX Live recommended)
- Python 3.9+ with `uv`
- `make` for build automation

### Setup

```bash
# Clone repository
git clone https://github.com/the78mole/cv.git
cd cv

# Install pre-commit hooks
uv tool install pre-commit
uv tool install detect-secrets
pre-commit install

# Install Python tools
cd scripts
uv sync
```

### Build Commands

```bash
# Generate PDF
make pdf

# Clean up
make clean

# Extract current positions
cd scripts && uv run extract-current ../Lebenslauf.tex
```

## 📊 Project Structure

```text
cv/
├── .github/
│   └── workflows/
│       └── build-and-release.yml  # Main CI/CD pipeline
├── scripts/
│   └── src/cv_tools/
│       └── extract_current.py     # CV extraction tool
├── Lebenslauf.tex                 # LaTeX main document
├── Makefile                       # Build automation
└── .pre-commit-config.yaml        # Code quality configuration
```

## 🤝 Contributions

This repository is primarily for my personal resume, but feedback and suggestions for
automation improvements are welcome!

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

**🔄 Automatically updated** | **✨ Made with LaTeX & GitHub Actions**
