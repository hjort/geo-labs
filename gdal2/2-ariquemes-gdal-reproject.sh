# https://gdal.org/programs/gdalwarp.html

gdalwarp -t_srs EPSG:4674 saida/duas-cenas-landsat.tif saida/duas-cenas-landsat-srs4674.tif

gdalinfo saida/duas-cenas-landsat-srs4674.tif

