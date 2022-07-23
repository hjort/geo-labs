#!/usr/bin/python3

from osgeo import ogr

shapefile = ogr.Open("example/shapefile.shp")
layer = shapefile.GetLayer(0)

for i in range(layer.GetFeatureCount()):
	feature = layer.GetFeature(i)
	id = feature.GetField("ID")
	name = feature.GetField("NAME")
	geometry = feature.GetGeometryRef()
	print(i, name, geometry.GetX(), geometry.GetY())

