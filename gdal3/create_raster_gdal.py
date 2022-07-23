#!/usr/bin/python3

from osgeo import gdal

driver = gdal.GetDriverByName("GTIFF")
dstFile = driver.Create("Example.tif", 360, 180, 1, gdal.GDT_Int16)

'''
The name of the raster file.
The desired number of cells across.
The desired number of cells down.
The desired number of bands in the file.
A constant defining the type of information to store in each cell. In our case,
each cell will hold a 16-bit integer value.
'''

from gdal import osr

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS("WGS84")
dstFile.SetProjection(spatialReference.ExportToWkt())

# we will use WGS84, allowing us to refer to each cell's
# position using latitude and longitude values

originX = -180
originY = 90
cellWidth = 1.0
cellHeight = 1.0
dstFile.SetGeoTransform([originX, cellWidth, 0, originY, 0, -cellHeight])

'''
The X and Y position of the top-left corner of the top-left cell
The width of each cell, measured in degrees of longitude
The height of each cell, measured in degrees of latitude
'''

band = dstFile.GetRasterBand(1)

import random

values = []
for row in range(180):
	row_data = []
	for col in range(360):
		row_data.append(random.randint(1, 100))
		values.append(row_data)

# using the built-in struct module, we have to write them to disk one row at a time
import struct
fmt = "<" + ("h" * band.XSize)
for row in range(180):
	scanline = struct.pack(fmt, *values[row])
	band.WriteRaster(0, row, 360, 1, scanline)

# alternatively, you can write the values array directly to the file as a NumPy array
'''
import numpy
array = numpy.array(values, dtype=numpy.int16)
band.WriteArray(array)
'''
