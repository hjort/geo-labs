# https://gdal.org/programs/gdal_merge.html

gdal_merge.py -v -o saida/duas-cenas-landsat.tif -of GTiff -a_nodata 0 entrada/*

gdalinfo saida/duas-cenas-landsat.tif

