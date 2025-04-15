# Visualizations for: "Evolution of default genetic control mechanisms"

This repository contains Python code for generating the figures published in:

> **William Bains, Enrico Borriello, and Dirk Schulze-Makuch** (2021). *Evolution of default genetic control mechanisms*. PLOS ONE 16(5): e0251568. https://doi.org/10.1371/journal.pone.0251568

## Repository Structure

```
├── generate_figures.py       # Main script to generate all figures
├── data/                     # Folder containing all CSV/TXT data files
│   ├── figure_1.csv
│   ├── figure_3A.txt
│   ├── figure_3B.txt
│   ├── figure_3C.csv
│   ├── figure_3D.csv
│   ├── figure_3E.txt
│   ├── figure_4.csv
│   ├── figure_5.csv
│   ├── figure_6.csv
│   ├── figure_7.csv
│   └── figure_8.csv
└── output/                   # (Optional) Folder where PDFs can be saved
    ├── figure_1.pdf
    ├── figure_3a.pdf
    ├── figure_3b.pdf
    ├── figure_3c.pdf
    ├── figure_3d.pdf
    ├── figure_3e.pdf
    ├── figure_4.pdf
    ├── figure_5.pdf
    ├── figure_6.pdf
    ├── figure_7.pdf
    └── figure_8.pdf
```

## Requirements

- Python >= 3.7
- NumPy
- pandas
- matplotlib
- SciPy

To install the required libraries:

```bash
pip install numpy pandas matplotlib scipy
```

## Usage

Each figure-generating function is modular and can be called independently. Run the script or import functions as needed.

```bash
python generate_figures.py
```

Alternatively, import the module in a Python or Jupyter environment:

```python
from generate_figures import (
    plot_figure_1, plot_figure_3a, plot_figure_3b, plot_figure_3c,
    plot_figure_3d, plot_figure_3e, plot_figure_4,
    plot_figure_5, plot_figure_6, plot_figure_7, plot_figure_8
)
plot_figure_5()
```

Each function accepts optional arguments:
- `csv_path` / `txt_path`: Path to input data file
- `save_path`: Path to save the figure as PDF
- `show_plot`: If `True`, display the plot in a window or notebook

## Figures

- Figure 1: Relative number of genomes by domain vs. genome size (log scale)
- Figure 3A: Fitness trajectory over time for a single genome in a static environment
- Figure 3B: Fitness trajectory under a fluctuating environment
- Figure 3C: Comparison of fitness trajectories across multiple simulation replicates
- Figure 3D: 3D visualization of fitness trajectories for multiple organisms
- Figure 3E: Fitness trajectory for a genome with regulatory control evolution enabled
- Figure 4: Scatter plot of genome size vs. environmental complexity, colored by a "perfection index"
- Figure 5: Frequency of regulatory gene acquisition events over evolutionary time across simulations
- Figure 6: Heatmap of gene expression patterns under different regulatory configurations
- Figure 7: Correlation between gene regulatory complexity and environmental variability
- Figure 8: Principal Component Analysis (PCA) of simulated genomes colored by evolutionary outcome

## Notes
- Ensure all data files are placed correctly under the `data/` folder.
- Output PDF files will be saved in the current working directory or in the path specified by `save_path`.

## License
This code is shared for academic and non-commercial use. Please cite the original publication when using these materials.

---

**Author:** Enrico Borriello

For questions, please refer to the contact information in the original publication.

