# https://gdal.org/programs/ogrinfo.html
# https://gdal.org/programs/gdalwarp.html

ogrinfo -al -geom=SUMMARY ../../1-coleta/12-coleta-shape-municipio/RO_Ariquemes_2021/RO_Ariquemes_2021.shp

gdalwarp -cutline ../../1-coleta/12-coleta-shape-municipio/RO_Ariquemes_2021/RO_Ariquemes_2021.shp -crop_to_cutline -dstnodata 0 saida/duas-cenas-landsat-srs4674-ts1327x772.tif saida/duas-cenas-landsat-srs4674-ts1327x772-ariquemes.tif

gdalinfo saida/duas-cenas-landsat-srs4674-ts1327x772-ariquemes.tif

