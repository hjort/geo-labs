gdal_merge.py -v -o BSB/DN_brasilia.tif -of GTiff -co COMPRESS=LZW -separate BSB/B?_brasilia.tif

gdalinfo BSB/DN_brasilia.tif

ls -lah BSB/DN_brasilia.tif
