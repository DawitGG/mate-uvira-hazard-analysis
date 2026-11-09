"""Helpers for locating and reading raster (GeoTIFF) files."""

from pathlib import Path

import numpy as np
import rasterio


def find_tif(folder, keyword=None):
    """Return the path of the single .tif file in `folder`.

    If `keyword` is given, only file names containing it
    (case-insensitive) are considered.
    """
    folder = Path(folder)
    if not folder.is_dir():
        raise FileNotFoundError(f"Folder not found: {folder}")

    candidates = sorted(folder.glob("*.tif"))
    if keyword:
        candidates = [p for p in candidates if keyword.lower() in p.name.lower()]

    if not candidates:
        raise FileNotFoundError(f"No matching .tif file in {folder}")
    if len(candidates) > 1:
        raise ValueError(f"Several files match: {[p.name for p in candidates]}")
    return candidates[0]


def load_raster(path, nodata_to_nan=False):
    """Read band 1 of a raster. Returns (array, profile).

    If nodata_to_nan is True, nodata pixels become NaN (array turns float32).
    """
    with rasterio.open(path) as src:
        array = src.read(1)
        profile = src.profile

    nodata = profile.get("nodata")
    if nodata_to_nan and nodata is not None:
        array = array.astype("float32")
        array[array == nodata] = np.nan

    return array, profile
