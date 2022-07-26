gdal_merge.py -o AMAZONIA_1_WFI_20210918_035_017_L4_RGB.tif -separate \
  AMAZONIA_1_WFI_20210918_035_017_L4_BAND3.tif \
  AMAZONIA_1_WFI_20210918_035_017_L4_BAND2.tif \
  AMAZONIA_1_WFI_20210918_035_017_L4_BAND1.tif \
  -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE

gdal_merge.py -o AMAZONIA_1_WFI_20210923_035_017_L4_RGB.tif -separate \
  AMAZONIA_1_WFI_20210923_035_017_L4_BAND3.tif \
  AMAZONIA_1_WFI_20210923_035_017_L4_BAND2.tif \
  AMAZONIA_1_WFI_20210923_035_017_L4_BAND1.tif \
  -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE

gdal_merge.py -o AMAZONIA_1_WFI_20210928_035_017_L4_RGB.tif -separate \
  AMAZONIA_1_WFI_20210928_035_017_L4_BAND3.tif \
  AMAZONIA_1_WFI_20210928_035_017_L4_BAND2.tif \
  AMAZONIA_1_WFI_20210928_035_017_L4_BAND1.tif \
  -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE
