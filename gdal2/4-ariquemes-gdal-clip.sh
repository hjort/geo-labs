# https://gdal.org/programs/ogrinfo.html
# https://gdal.org/programs/gdalwarp.html

#ogrinfo -al -geom=SUMMARY ../../1-coleta/12-coleta-shape-municipio/RO_Ariquemes_2021/RO_Ariquemes_2021.shp
#gdalwarp -cutline ../../1-coleta/12-coleta-shape-municipio/RO_Ariquemes_2021/RO_Ariquemes_2021.shp -crop_to_cutline -dstnodata 0 saida/duas-cenas-landsat-srs4674-ts1327x772.tif saida/duas-cenas-landsat-srs4674-ts1327x772-ariquemes.tif
#gdalinfo saida/duas-cenas-landsat-srs4674-ts1327x772-ariquemes.tif

ogrinfo -al -geom=SUMMARY entrada/RO_Ariquemes_2021.shp

gdalwarp -cutline entrada/RO_Ariquemes_2021.shp -crop_to_cutline -dstnodata 0 saida/ariquemes-b4-4674-1330x772.tif saida/ariquemes-b4-4674-1330x772-clip.tif
gdalwarp -cutline entrada/RO_Ariquemes_2021.shp -crop_to_cutline -dstnodata 0 saida/ariquemes-b5-4674-1330x772.tif saida/ariquemes-b5-4674-1330x772-clip.tif

gdalinfo saida/ariquemes-b4-4674-1330x772-clip.tif
gdalinfo saida/ariquemes-b5-4674-1330x772-clip.tif

#ariquemes-ndvi-4674-1330x772-clip.tif
#("ariquemes-b5-4674-1330x772-clip@1" - "ariquemes-b4-4674-1330x772-clip@1") / ("ariquemes-b5-4674-1330x772-clip@1" + "ariquemes-b4-4674-1330x772-clip@1")
