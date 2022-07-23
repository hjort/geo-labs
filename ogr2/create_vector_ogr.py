#!/usr/bin/python3

import os, os.path, shutil, random
from osgeo import ogr, osr

if os.path.exists("example"):
	shutil.rmtree("example")
os.mkdir("example")

driver = ogr.GetDriverByName("ESRI Shapefile")
path = os.path.join("example", "shapefile.shp")
datasource = driver.CreateDataSource(path)

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS('WGS84')

layer = datasource.CreateLayer("layer", spatialReference)

field = ogr.FieldDefn("ID", ogr.OFTInteger)
field.SetWidth(4)
layer.CreateField(field)

field = ogr.FieldDefn("NAME", ogr.OFTString)
field.SetWidth(20)
layer.CreateField(field)

for i in range(100):
	id = 1000 + i
	lat = random.uniform(-90, +90)
	long = random.uniform(-180, +180)
	name = "point-{}".format(i)
	wkt = "POINT({} {})".format(long, lat)
	geometry = ogr.CreateGeometryFromWkt(wkt)

feature = ogr.Feature(layer.GetLayerDefn())
feature.SetGeometry(geometry)
feature.SetField("ID", id)
feature.SetField("NAME", name)

layer.CreateFeature(feature)

