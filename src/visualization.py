"""Functions for plotting raster maps and exporting them as images."""

from pathlib import Path

import matplotlib.pyplot as plt


def save_map(array, title, output_path, cmap="viridis", cbar_label="",
             vmin=None, vmax=None, dpi=600):
    """Plot a 2D array with a colorbar and save it as an image (600 dpi default)."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(array, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_title(title)
    ax.set_xlabel("Column (pixel)")
    ax.set_ylabel("Row (pixel)")
    fig.colorbar(im, ax=ax, label=cbar_label)

    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.show()
    plt.close(fig)
