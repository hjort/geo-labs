#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
#import urllib
import os

def get_epsg_code(epsg):
	"""
	Get the ESRI formatted .prj definition
	usage get_epsg_code(4326)
	We use the http://spatialreference.org/ref/epsg/4326/esriwkt/
	"""
	with urllib.request.urlopen("http://spatialreference.org/ref/epsg/{0}/esriwkt/".format(epsg)) as url:
		s = url.read()
	return s.decode('utf-8')
	#f = urllib.request.urlopen("http://spatialreference.org/ref/epsg/{0}/esriwkt/".format(epsg))
	#f = urllib.urlopen("http://spatialreference.org/ref/epsg/{0}/esriwkt/".format(epsg))
	#return (f.read())

# Shapefile filename must equal the new .prj filename
shp_filename = "../geodata/UTM_Zone_Boundaries"

# Here we write out a new .prj file with the same name
# as our Shapefile named "schools" in this example
with open("../geodata/{0}.prj".format(shp_filename), "w") as prj:
	epsg_code = get_epsg_code(4326)
	#print(epsg_code)
	prj.write(epsg_code)
	print("done writing projection definition to EPSG: " + epsg_code)
