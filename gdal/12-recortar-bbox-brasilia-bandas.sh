ogrinfo -al -geom=SUMMARY area_brasilia.shp

for i in {1..7}
do
  echo "[B${i}]"

  gdalwarp \
    -cutline area_brasilia.shp \
    -crop_to_cutline -dstnodata 0 \
    BSB/LC09_L2SP_221071_20220714_20220718_02_T1_SR_B${i}.TIF \
    BSB/B${i}_brasilia.tif

  gdalinfo BSB/B${i}_brasilia.tif
done

