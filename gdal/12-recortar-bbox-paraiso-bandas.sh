ogrinfo -al -geom=SUMMARY gleba_paraiso_bbox/SELECT.shp

for i in {02..07}
do
  echo "[B${i}]"

  gdalwarp \
    -cutline gleba_paraiso_bbox/SELECT.shp \
    -crop_to_cutline -dstnodata 0 \
    B${i}.tif B${i}_paraiso.tif

  gdalinfo B${i}_paraiso.tif
done

