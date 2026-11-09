# mate-uvira-hazard-analysis
Team Mate: Environmental Programming, Assignment 6, Vrije Universiteit Brussel (2026-2027)
Team Mate: Dawit, Andre, Lander, Brian

## 1. Project overview
This software analyses the landslide and flash flood event that hit Uvira
(DR Congo) on 17-04-2020, using remote sensing data. It:
- loads a natural hazard (NH) likelihood map, a slope map and a stream network map,
- visualizes and exports the slope and stream network maps at 600 dpi,
- builds a binary affected/non-affected map with a user-chosen threshold,
- separates landslide from flash flood areas using slope and stream thresholds, then exports a 600 dpi map for each area,
- plots spatially averaged daily rainfall as a time series,
- computes X-day rainfall statistics (average, median, max, sum) before or after a chosen date, including the required 1-, 2- and 3-day periods around 17-04-2020,
- exports the rainfall statistics to a CSV.

## 2. Repository structure
```
├── DATA/                  # input data (not included / see section 4)
├── src/                   # Python modules (io, hazard, rainfall, plotting, gui)
|   └── io.py              # io
|   └── hazard.py          # hazard
|   └── rainfall.py        # rainfall
|   └── plotting.py        # plotting
|   └── gui.py             # gui
├── notebooks/
│   └── user_manual.ipynb  # tutorial, AI-use log, contributions, flow chart
├── outputs/               # generated maps and CSV
├── environment.yml        # conda environment
└── README.md
```
## 3. Installation
```bash
git clone https://github.com/DawitGG/mate-uvira-hazard-analysis.git
cd mate-uvira-hazard-analysis
conda env create -f environment.yml
conda activate <environment-name>
```

## 4. Data
Place the data in a `DATA/` folder with this layout:
- `Natural_hazard_image/`: NH likelihood map (0-1, 30 m)
- `Rainfall_images/`: daily rainfall .tif files
- `Land_surface_data/`: slope and stream network maps (30 m)