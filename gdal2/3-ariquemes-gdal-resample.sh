# https://gdal.org/programs/gdalwarp.html

#gdalwarp -ts 1327 772 saida/duas-cenas-landsat-srs4674.tif saida/duas-cenas-landsat-srs4674-ts1327x772.tif
#gdalinfo saida/duas-cenas-landsat-srs4674-ts1327x772.tif

gdalwarp -ts 1330 772 saida/ariquemes-b4-4674.tif saida/ariquemes-b4-4674-1330x772.tif
gdalwarp -ts 1330 772 saida/ariquemes-b5-4674.tif saida/ariquemes-b5-4674-1330x772.tif

gdalinfo saida/ariquemes-b4-4674-1330x772.tif
gdalinfo saida/ariquemes-b5-4674-1330x772.tif

