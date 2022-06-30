# Cartogrammer

Turn shapefiles into grids of evenly spaced squares for use in grid cartograms.

See an example useage [here](https://nbviewer.org/github/dexmcmillan/cbc-data/blob/main/notebooks-other/20220630-CARTOGRAMMEREXAMPLE/20220630-CARTOGRAMMEREXAMPLE.ipynb).

### Useage

Cartogrammer exposes one class, Cartogram. Implement like so:

```python:
import cartogrammer

cartogram = cartogrammer.Cartogram(shapefile_path, export)

print(cartogram.data)

```

### Arguments

**file (str)**: The filepath to the shapefile (in .zip format) that you'd like to convert.

**export (str)**: The filepath and name of the exported file.
