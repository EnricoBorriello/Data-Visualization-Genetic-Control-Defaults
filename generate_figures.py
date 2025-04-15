#Visualizations for
#William Bains, Enrico Borriello, and Dirk Schulze-Makuch,
#'Evolution of default genetic control mechanisms,'
#PloS one 16.5 (2021): e0251568. https://doi.org/10.1371/journal.pone.0251568

#Author: Enrico Borriello

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from mpl_toolkits.mplot3d import Axes3D

# Global settings
plt.rcParams.update({
    'axes.linewidth': 1.5,
    'font.size': 14
})

#------------------------------------

# FIGURE 1

def plot_figure_1(csv_path='data/figure_1.csv', save_path='figure_1.pdf', show_plot=True):
    """
    Plot Figure 1 from a CSV file and optionally save it.
    
    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot (for Jupyter Notebook). If False, only saves.
    """
    
    # Load Data
    data = pd.read_csv(
        csv_path,
        names=['size', 'bacteria', 'archaea', 'eukarya', 'virus']
    ).iloc[1:].astype(float)

    size_log = np.log10(data['size'].values)
    bac_num = data['bacteria'].values
    arc_num = data['archaea'].values
    euk_num = data['eukarya'].values
    vir_num = data['virus'].values

    # Interpolators
    interpolators = {
        'Bacteria': interp1d(size_log, bac_num, kind='cubic'),
        'Archaea': interp1d(size_log, arc_num, kind='cubic'),
        'Eukarya': interp1d(size_log, euk_num, kind='cubic'),
        'Virus': interp1d(size_log, vir_num, kind='cubic')
    }

    colors = {
        'Virus': 'tab:green',
        'Archaea': 'darkgray',
        'Bacteria': 'orange',
        'Eukarya': 'tab:blue'
    }

    # Create Plot
    fig, ax = plt.subplots()
    ax.set_xscale('log')

    x = 10 ** np.arange(-3, 5, 0.01)

    for label, interpolator in interpolators.items():
        y = interpolator(np.log10(x))
        # Decorative thick white line underneath
        ax.plot(x, y, linewidth=6, color='white', zorder=1)
        ax.plot(x, y, label=label, linewidth=2, color=colors[label], zorder=2)

    # White horizontal line at y=0
    ax.plot([10**-3, 10**4], [0, 0], color='white', linewidth=7.6, zorder=0)

    # Labels and limits
    ax.set_xlim(10**-3, 10**4)
    ax.set_ylim(0.00, 0.5)
    ax.set_xlabel('Genome size (megabases)')
    ax.set_ylabel('Relative number of genomes')

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Legend
    ax.legend(
        prop={'size': 11},
        fancybox=True,
        framealpha=1,
        shadow=True,
        borderpad=0.5
    )

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 3A

def plot_figure_3a(csv_path='data/figure_3A.txt', save_path='figure_3a.pdf', show_plot=True):
    """
    Plot Figure 3A: Average fitness over time.
    
    Parameters
    ----------
    csv_path : str
        Path to the TXT file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot (for Jupyter Notebook). If False, only saves.
    """

    # Load Data
    data = pd.read_csv(csv_path).iloc[1:].astype(float)
    av_fit_en_1 = data.values.flatten()

    # Prepare X axis (time in millions of generations)
    x = 100. * np.arange(len(av_fit_en_1)) / 1e6

    # Create Plot
    fig, ax = plt.subplots()

    ax.plot(x, av_fit_en_1, linewidth=2, color='tab:blue')

    # Set limits
    ax.set_xlim(0, 2.5)
    ax.set_ylim(0, 30)

    # Labels
    ax.set_xlabel('Time (millions of generations)')
    ax.set_ylabel('Average fitness')

    # Ticks
    ax.tick_params(axis='both', labelsize=14)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 3B

def plot_figure_3b(csv_path='data/figure_3B.txt', save_path='figure_3b.pdf', show_plot=True):
    """
    Plot Figure 3B: Average fitness over time (short timescale).

    Parameters
    ----------
    csv_path : str
        Path to the TXT file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path).iloc[1:].astype(float)
    av_fit = data.values.flatten()

    # Prepare x-axis (time in millions of generations)
    x = 100. * np.arange(len(av_fit)) / 1e6

    # Create plot
    fig, ax = plt.subplots()

    ax.plot(x, av_fit, linewidth=2, color='tab:blue')

    #pl.tight_layout(pad=.10, w_pad=10, h_pad=10)
    plt.subplots_adjust(left=4, bottom=4, right=5.5, top=5.5)

    # Set limits
    ax.set_xlim(0, 0.7)
    ax.set_ylim(0, 30)

    # Labels
    text_size = 14
    ax.set_xlabel('Time (millions of generations)', fontsize=text_size)
    ax.set_ylabel('Average fitness', fontsize=text_size)

    # Ticks
    ax.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------


def plot_figure_3c(csv_path='data/figure_3C.csv', save_path='figure_3c.pdf', show_plot=True):
    """
    Plot Figure 3C: Average fitness over time in three environments.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path, names=['fit1', 'fit2', 'fit3', 'average']).iloc[1:].astype(float)

    fit1 = data['fit1'].values
    fit2 = data['fit2'].values
    fit3 = data['fit3'].values
    avg = data['average'].values

    # Prepare x-axis (time in millions of generations)
    x = 100. * np.arange(len(avg)) / 1e6

    # Create plot
    fig, ax = plt.subplots()

    # Plot each line with decorative white background first
    for y_values, color, label in [
        (fit1, 'tab:blue', 'Environment 1'),
        (fit2, 'orange', 'Environment 2'),
        (fit3, 'tab:green', 'Environment 3'),
        (avg, 'black', 'Average')
    ]:
        ax.plot(x, y_values, linewidth=4, color='white')  # Decorative white line
        ax.plot(x, y_values, linewidth=2, color=color, label=label)

    #pl.tight_layout(pad=.10, w_pad=10, h_pad=10)
    plt.subplots_adjust(left=4, bottom=4, right=5.5, top=5.5)

    # Set limits
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 30)

    # Labels
    text_size = 14
    ax.set_xlabel('Time (millions of generations)', fontsize=text_size)
    ax.set_ylabel('Average fitness', fontsize=text_size)

    # Ticks
    ax.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Legend
    ax.legend(
        prop={'size': 0.8 * text_size},
        fancybox=True,
        framealpha=1,
        shadow=True,
        borderpad=0.5
    )

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 3D

def plot_figure_3d(csv_path='data/figure_3D.csv', save_path='figure_3d.pdf', show_plot=True):
    """
    Plot Figure 3D: 3D plot of individual fitness over time for five organisms.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path)

    fit1 = data['Organism_1'].values
    fit2 = data['Organism_2'].values
    fit3 = data['Organism_3'].values
    fit4 = data['Organism_4'].values
    fit5 = data['Organism_5'].values

    # Prepare x-axis (time in millions of generations)
    x = 100. * np.arange(len(fit1)) / 1e6

    # Prepare y-axis (organism labels)
    y = {
        1: np.ones_like(x),
        2: np.ones_like(x) * 2,
        3: np.ones_like(x) * 3,
        4: np.ones_like(x) * 4,
        5: np.ones_like(x) * 5,
    }

    # Prepare z-axis (fitness values)
    z = {
        1: fit1,
        2: fit2,
        3: fit3,
        4: fit4,
        5: fit5,
    }

    # Create 3D plot
    plt.figure()
    ax = plt.subplot(projection='3d')

    # Define colors
    colors = {
        1: 'tab:blue',
        2: 'orange',
        3: 'tab:green',
        4: 'darkgray',
        5: 'black',
    }

    # Plot each organism's fitness curve with white decorative background
    for i in range(5, 0, -1):
        ax.plot(x, y[i], z[i], color='white', linewidth=4)  # Decorative white line
        ax.plot(x, y[i], z[i], color=colors[i], linewidth=2)

    # View angle
    ax.view_init(elev=30, azim=-75)

    # Labels
    text_size = 18
    ax.set_xlabel('Time (millions of generations)', size=text_size, labelpad=16)
    ax.set_ylabel('Organism', size=text_size, labelpad=16)
    ax.set_zlabel('Individual fitness', size=text_size, labelpad=16)

    # Remove colored panes
    for pane in [ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane]:
        pane.fill = False
        pane.set_edgecolor('white')

    # Ticks
    ax.set_yticks(range(1, 6, 1))
    ax.tick_params(axis='x', labelsize=text_size)
    ax.tick_params(axis='y', labelsize=text_size)
    ax.tick_params(axis='z', labelsize=text_size)

    # Tight layout adjustments
    plt.tight_layout()

    # Set limits
    ax.set_zlim(0, 30)
    ax.set_xlim(0, 0.85)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 3E

def plot_figure_3e(txt_path='data/figure_3E.txt', save_path='figure_3e.pdf', show_plot=True):
    """
    Plot Figure 3E: Average fitness over time.

    Parameters
    ----------
    txt_path : str
        Path to the TXT file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(txt_path)[1:].astype(float)
    fit = np.array(data)

    # Prepare x-axis (time in millions of generations)
    x = 100. * np.arange(len(fit)) / 1e6

    # Create figure
    fig, ax = plt.subplots()

    # Plot
    plt.plot(x, fit, linewidth=2, color='tab:blue')

    # Set limits
    plt.ylim(0, 30)
    plt.xlim(0, 1.2)

    # Labels
    text_size = 14
    plt.xlabel('Time (millions of generations)', size=1.0 * text_size)
    plt.ylabel('Average fitness', size=1.0 * text_size)

    # Tick parameters
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 4


def plot_figure_4(csv_path='data/figure_4.csv', save_path='figure_4.pdf', show_plot=True):
    """
    Plot Figure 4: Scatter plot of genome vs. environmental complexity colored by perfection index.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path).astype(float)

    # Extract columns
    x = data['g_comp']
    y = data['e_comp']
    colors = data['perf']
    sizes = 400 * colors

    # Create figure
    fig, ax = plt.subplots()

    # Scatter plot
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.75, cmap='Spectral')

    # Colorbar
    cbar = plt.colorbar(scatter, ticks=np.arange(0, 1, 0.1))
    cbar.set_label('Perfection Index', size=12)

    # Log scales
    plt.xscale('log')
    plt.yscale('log')

    # Limits
    plt.xlim(10**2, 10**4)
    plt.ylim(10**1, 10**5)

    # Labels and title
    text_size = 14
    plt.xlabel('Genome complexity', size=1.0 * text_size)
    plt.ylabel('Environmental complexity', size=1.0 * text_size)
    plt.title('Perfection Index\n', size=text_size)

    # Ticks
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()


#------------------------------------

# FIGURE 5

def plot_figure_5(save_path='figure_5.pdf', show_plot=True):
    """
    Plot Figure 5: Fitness trajectories with error bars for two model sets.

    Parameters
    ----------
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Data
    x1 = np.arange(0, 1.1, 0.25)
    y1 = [0, 0.752, 0.875, 0.962, 1]
    yerr1 = [0, 0.405, 0.443, 0.438, 0]

    x2 = x1
    y2 = [0, 0.644, 0.792, 0.924, 1]
    yerr2 = [0, 0.213, 0.220, 0.187, 0]

    # Create figure
    fig, ax = plt.subplots()

    # Plot lines
    plt.plot(x1, y1, '-o', linewidth=2, color='tab:blue', label='All 118 models', markersize=10)
    plt.plot(x2, y2, '-s', linewidth=2, color='orange', label='101 models with positive curve parameter', markersize=10)

    # Add error bars
    ax.errorbar(x1, y1, yerr=yerr1, fmt='-o', color='tab:blue', capsize=5, capthick=2, linewidth=2, markersize=10)
    ax.errorbar(x2, y2, yerr=yerr2, fmt='-s', color='orange', capsize=5, capthick=2, linewidth=2, markersize=10)

    # Labels and ticks
    text_size = 14
    plt.xlabel('Fraction of time before fitness plateau', size=text_size)
    plt.ylabel('Average fitness ± 1 STD', size=text_size)
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

    # Legend
    plt.legend(prop={"size": 0.8 * text_size}, fancybox=True, framealpha=1, shadow=True, borderpad=0.5)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 6

def plot_figure_6(csv_path='data/figure_6.csv', save_path='figure_6.pdf', show_plot=True):
    """
    Plot Figure 6: Relationship between starting gene length and average coding sequence length.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path).astype(float)

    x = data['len1']
    y = data['len2']
    colors = data['num']
    sizes = 1 * colors

    # Create plot
    fig, ax = plt.subplots()

    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.75, cmap='Spectral')
    plt.colorbar(scatter, ticks=np.arange(25, 101, 25))

    # Axes limits
    plt.xlim(1, 6)
    plt.ylim(0, 12)

    # Labels
    text_size = 14
    plt.xlabel('Starting gene length', size=text_size)
    plt.ylabel('Average coding sequence length\nat fitness plateau', size=text_size)
    plt.title('Gene number\n', size=text_size)

    # Ticks
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)
    ax.set_axisbelow(True)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 7

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_figure_7(csv_path='data/figure_7.csv', save_path='figure_7.pdf', show_plot=True):
    """
    Plot Figure 7: Relationship between regulatory ratio and gene expression.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path).astype(float)

    x = data['min']
    y = data['frac']
    colors = data['size']
    sizes = 2 * colors

    # Create plot
    fig, ax = plt.subplots()

    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.75, cmap='Spectral')
    plt.colorbar(scatter, ticks=np.arange(25, 101, 25))

    # Axes limits
    plt.xlim(0.5, 2.5)
    plt.ylim(0, 1)

    # Labels
    text_size = 14
    plt.xlabel('min -ve / min +ve', size=text_size)
    plt.ylabel('Fraction of genes expressed', size=text_size)
    plt.title('Genome size\n', size=text_size)

    # Ticks
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)
    ax.set_axisbelow(True)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()

#------------------------------------

# FIGURE 8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_figure_8(csv_path='data/figure_8_all.csv', save_path='figure_8_all.pdf', show_plot=True):
    """
    Plot Figure 8: Perfection index vs. element length ratio, colored by time to plateau.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path).astype(float)

    x = data['frac']
    y = data['avg']
    colors = data['time']
    sizes = 0.05 * colors

    # Create plot
    fig, ax = plt.subplots()

    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.75, cmap='Spectral')
    plt.colorbar(scatter, ticks=np.arange(0, 20000, 2500))

    # Axes limits
    plt.xlim(-0.1, 1.1)
    plt.ylim(0.5, 2.5)

    # Labels
    text_size = 14
    plt.xlabel('Perfection index', size=text_size)
    plt.ylabel('Average -ve el. len. / avg. +ve el. len.', size=text_size)
    plt.title('Time to plateau\n(all data)\n', size=text_size)

    # Ticks
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)
    ax.set_axisbelow(True)

    # Save
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Optionally show
    if show_plot:
        plt.show()
    else:
        plt.close()


#------------------------------------

# FIGURE 8 replicates

def plot_figure_8_replicates(csv_path='data/figure_8_rep.csv',
                              save_path='figure_8_rep.pdf',
                              show_plot=True):
    """
    Plot Figure 8 (replicates): Perfection index vs. element length ratio,
    colored by time to plateau, with annotated regions for replicate sets.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the replicate data.
    save_path : str
        Path where the figure will be saved as PDF.
    show_plot : bool
        If True, displays the plot. If False, only saves.
    """

    # Load data
    data = pd.read_csv(csv_path).astype(float)

    x = data['frac']
    y = data['avg']
    colors = data['time']
    sizes = 0.05 * colors

    # Create plot
    fig, ax = plt.subplots()

    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.75, cmap='Spectral')
    plt.colorbar(scatter)

    # Axes limits
    plt.xlim(0, 1)
    plt.ylim(0.6, 1.8)

    # Labels and title
    text_size = 14
    plt.xlabel('Perfection index', size=text_size)
    plt.ylabel('Average -ve el. len. / avg. +ve el. len.', size=text_size)
    plt.title('Time to plateau\n(replicate sets)\n', size=text_size)

    # Tick styling
    plt.tick_params(axis='both', labelsize=text_size)

    # Gridlines
    ax.yaxis.grid(True, linestyle='-', color='whitesmoke')
    ax.xaxis.grid(True, linestyle='-', color='whitesmoke')
    plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)
    ax.set_axisbelow(True)

    # Annotations and dividers
    plt.plot([0.625, 0.625], [0.6, 1.8], '--', color='darkgray')
    plt.plot([0, 0.625], [1.1, 1.1], '--', color='darkgray')
    plt.text(0.05, 1.65, "set 3", va='bottom', size=12)
    plt.text(0.05, 0.95, "set 2", va='bottom', size=12)
    plt.text(0.68, 1.65, "set 1", va='bottom', size=12)

    # Save plot
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=100)

    # Show or close
    if show_plot:
        plt.show()
    else:
        plt.close()
