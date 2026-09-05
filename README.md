# cantera_thermodynamic

> A collection of open‑source combustion & thermodynamic simulation cases built with **Cantera**.
> Trunk‑Based‑Development workflow, simulation scripts, academic plotting and post‑processing tools for combustion‑thermodynamic research.

[![GitHub Repo stars](https://img.shields.io/github/stars/Skixkk/cantera_thermodynamic)](https://github.com/Skixkk/cantera_thermodynamic)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

## 📚 Overview

This repository stores reusable simulation projects based on the Cantera chemical kinetics library.
Focus on methane‑air combustion, adiabatic‑flame‑temperature equilibrium calculation, multi‑mechanism comparison, academic‑grade visualization and thermodynamic post‑processing.

All cases follow clean engineering specifications:

- Isolated sub‑folders for each simulation case
- Auto‑generated `dist/` output directory for exported figures
- High‑resolution vector graphics export: PDF / SVG / PNG, ready‑to‑use for papers & theses
- Both English‑version and Chinese‑version plotting scripts are provided

## 🧪 Included Simulation Cases

### 1. `constant_p_adi_flame_T`

Constant‑pressure adiabatic‑flame‑temperature solver

- Methane‑air mixture
- HP‑equilibrium calculation (`equilibrate('HP')`)
- Equivalence‑ratio sweep: 0.6 ~ 1.4
- Academic curve plotting
- Auto‑export results to `./dist`

### 2. `GRI30_GRI30_ion`

Combustion‑mechanism comparison

- Baseline mechanism: **GRI‑3.0**
- Ion‑containing mechanism: **GRI‑30‑ion**
- Compare adiabatic flame‑temperature curves, analyse the effect of ion‑reactions
- Dual‑language plotting: English chart & Chinese‑label chart for domestic thesis

### 3. `test`

Environment verification scripts, quick tests for Cantera installation & quantity units.

## 🚀 Quick Start

### 1. Clone repository

```Bash
git clone git@github.com:Skixkk/cantera_thermodynamic.git
cd cantera_thermodynamic
```

### 2. Create virtual environment & install dependencies

```Bash
# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Run one simulation case

```Bash
cd constant_p_adi_flame_T
python Constant_P_adiabatic_flame_T.py
```

Generated figures will be saved into `./dist` folder automatically.

## 📁 Project Structure

```Bash
cantera_thermodynamic/
├── constant_p_adi_flame_T/      # Constant‑pressure adiabatic flame temperature
│   ├── dist/                     # Output figures (PDF,SVG,PNG)
│   └── *.py
├── GRI30_GRI30_ion/              # GRI‑3.0 vs GRI‑30‑ion comparison
│   ├── dist/
│   └── *.py
├── test/                          # Environment & unit test scripts
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🔧 Development Workflow

This repo follows **Trunk‑Based‑Development**:

- Long‑lived trunk branch: `main`
- **Direct push to `main` is forbidden**. All changes must go through Pull‑Request review
- Short‑lived feature branches created from latest `main`
- Branch naming rule: `type/issueId‑short‑kebab‑case‑description`
- Feature branch will be deleted after merged into `main`

Commit message follows **Angular Commit Convention**:

```Text
type(<scope>): <emoji> <subject>

<body>

<footer>
```

## 📌 Future Plan

- Add constant‑volume adiabatic flame temperature solver
- Laminar flame‑speed simulation
- More combustion‑mechanism comparison cases
- Parameter sweep & batch post‑processing scripts
- Additional thermodynamic property calculation modules

## 📄 License

This project is released under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

## 🤝 Contributions

Issues, suggestions and pull‑requests are welcome.
Before submitting PR, please pull the latest `main` branch and create a short‑lived feature branch.
