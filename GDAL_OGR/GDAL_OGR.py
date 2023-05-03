from osgeo import gdal
import sys

gdal.UseExceptions

try:
    ds = gdal.Open(r"A:\UW-Madison\GIS Spring 2022\G378\g378_rasterdata\raster\IndependenceSW.tiff")
except RuntimeError as e:
    print(e)
    print('File not found')
    sys.exit(1)

try:
    dsBand = ds.GetRasterBand(1)
except RuntimeError as e:
    print(f'band not found')
    sys.exit(1)

print('code excecuted')