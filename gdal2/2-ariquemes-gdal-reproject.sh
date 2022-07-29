# https://gdal.org/programs/gdalwarp.html

#gdalwarp -t_srs EPSG:4674 saida/duas-cenas-landsat.tif saida/duas-cenas-landsat-srs4674.tif
#gdalinfo saida/duas-cenas-landsat-srs4674.tif

gdalwarp -t_srs EPSG:4674 saida/ariquemes-b4.tif saida/ariquemes-b4-4674.tif
gdalwarp -t_srs EPSG:4674 saida/ariquemes-b5.tif saida/ariquemes-b5-4674.tif

gdalinfo saida/ariquemes-b4-4674.tif
gdalinfo saida/ariquemes-b5-4674.tif

