#!/usr/bin/python3

from osgeo import gdal

srcFile = gdal.Open("Example.tif")
band = srcFile.GetRasterBand(1)

# using the built-in struct module
import struct
fmt = "<" + ("h" * band.XSize)
for row in range(band.YSize):
	scanline = band.ReadRaster(0, row, band.XSize, 1, band.XSize, 1, band.DataType)
	row_data = struct.unpack(fmt, scanline)
	print(row_data)

# do the same thing again, this time using NumPy
'''
values = band.ReadAsArray()
for row in range(band.XSize):
	print(values[row])
'''

