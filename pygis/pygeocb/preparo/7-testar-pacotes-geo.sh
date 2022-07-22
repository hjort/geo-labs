#/bin/bash -x

echo "
import numpy
import pyproj
" | python

echo "
import shapely
import matplotlib
import descartes
" | python

echo "
import shapefile
import geojson
import pandas
" | python

echo "
import scipy
import pysal
" | python

echo "
from osgeo import gdal
from osgeo import ogr
from osgeo import osr
from osgeo import gdal_array
from osgeo import gdalconst
" | python

python -c 'from osgeo import gdal; print(gdal.__version__)'
