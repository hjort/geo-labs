#!/usr/bin/python3

# gdal_merge.py -v -o saida/duas-cenas-landsat.tif -of GTiff -a_nodata 0 entrada/*

import math
import os.path
import sys
import time

from osgeo import gdal

sys.path.append('/usr/bin')
import gdal_merge

def gerar_mosaico(saida='out.tif', cena1=None, cena2=None):

    verbose = 0
    quiet = 0
    #names = []
    #frmt = None
    #out_file = saida

    ulx = None
    psize_x = None
    separate = 0
    copy_pct = 0
    nodata = None
    a_nodata = None
    create_options = []
    pre_init = []
    band_type = None
    createonly = 0
    bTargetAlignedPixels = False
    start_time = time.time()

    gdal.AllRegister()

    frmt = "GTiff" # GeoTiff
    a_nodata = 0   # nodata = 0

    out_file = saida
    names = []
    names.append(cena1)
    names.append(cena2)

    Driver = gdal.GetDriverByName(frmt)
    DriverMD = Driver.GetMetadata()

    from gdal_merge import names_to_fileinfos
    file_infos = names_to_fileinfos(names)

    if ulx is None:
        ulx = file_infos[0].ulx
        uly = file_infos[0].uly
        lrx = file_infos[0].lrx
        lry = file_infos[0].lry

        for fi in file_infos:
            ulx = min(ulx, fi.ulx)
            uly = max(uly, fi.uly)
            lrx = max(lrx, fi.lrx)
            lry = min(lry, fi.lry)

    if psize_x is None:
        psize_x = file_infos[0].geotransform[1]
        psize_y = file_infos[0].geotransform[5]

    if band_type is None:
        band_type = file_infos[0].band_type

    gdal.PushErrorHandler('CPLQuietErrorHandler')
    t_fh = gdal.Open(out_file, gdal.GA_Update)
    gdal.PopErrorHandler()

    if t_fh is None:
        if bTargetAlignedPixels:
            ulx = math.floor(ulx / psize_x) * psize_x
            lrx = math.ceil(lrx / psize_x) * psize_x
            lry = math.floor(lry / -psize_y) * -psize_y
            uly = math.ceil(uly / -psize_y) * -psize_y
        geotransform = [ulx, psize_x, 0, uly, 0, psize_y]
        xsize = int((lrx - ulx) / geotransform[1] + 0.5)
        ysize = int((lry - uly) / geotransform[5] + 0.5)
        if separate != 0:
            bands = 0
            for fi in file_infos:
                bands = bands + fi.bands
        else:
            bands = file_infos[0].bands
        t_fh = Driver.Create(out_file, xsize, ysize, bands,
                             band_type, create_options)
        t_fh.SetGeoTransform(geotransform)
        t_fh.SetProjection(file_infos[0].projection)
        if copy_pct:
            t_fh.GetRasterBand(1).SetRasterColorTable(file_infos[0].ct)
    else:
        if separate != 0:
            bands = 0
            for fi in file_infos:
                bands = bands + fi.bands
        else:
            bands = min(file_infos[0].bands, t_fh.RasterCount)

    # Do we need to set nodata value ?
    if a_nodata is not None:
        for i in range(t_fh.RasterCount):
            t_fh.GetRasterBand(i + 1).SetNoDataValue(a_nodata)

    # Do we need to pre-initialize the whole mosaic file to some value?
    if pre_init is not None:
        if t_fh.RasterCount <= len(pre_init):
            for i in range(t_fh.RasterCount):
                t_fh.GetRasterBand(i + 1).Fill(pre_init[i])
        elif len(pre_init) == 1:
            for i in range(t_fh.RasterCount):
                t_fh.GetRasterBand(i + 1).Fill(pre_init[0])

    # Copy data from source files into output file.
    t_band = 1
    fi_processed = 0
    for fi in file_infos:
        if createonly != 0:
            continue
        if separate == 0:
            for band in range(1, bands + 1):
                fi.copy_into(t_fh, band, band, nodata)
        else:
            for band in range(1, fi.bands + 1):
                fi.copy_into(t_fh, band, t_band, nodata)
                t_band = t_band + 1
        fi_processed = fi_processed + 1
    # Force file to be closed.
    t_fh = None

# Banda 4
gerar_mosaico(saida="saida/ariquemes-b4.tif",
  cena1="/data/Landsat8-Data/LC09_L1TP_231067_20220704_20220704_02_T1/LC09_L1TP_231067_20220704_20220704_02_T1_B4.TIF",
  cena2="/data/Landsat8-Data/LC09_L1TP_232067_20220727_20220727_02_T1/LC09_L1TP_232067_20220727_20220727_02_T1_B4.TIF"
)

# Banda 5
gerar_mosaico(saida="saida/ariquemes-b5.tif",
  cena1="/data/Landsat8-Data/LC09_L1TP_231067_20220704_20220704_02_T1/LC09_L1TP_231067_20220704_20220704_02_T1_B5.TIF",
  cena2="/data/Landsat8-Data/LC09_L1TP_232067_20220727_20220727_02_T1/LC09_L1TP_232067_20220727_20220727_02_T1_B5.TIF"
)

