#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# database options
db_schema = "SCHEMA=geodata"
overwrite_option = "OVERWRITE=YES"
geom_type = "MULTILINESTRING"
output_format = "PostgreSQL"

# database connection string
db_connection = """PG:dbname=pygeocb"""

# input shapefile
input_shp = "../geodata/bikeways.shp"

# call ogr2ogr from python
subprocess.call(["ogr2ogr","-lco", db_schema, "-lco", overwrite_option, "-nlt", geom_type, "-f", output_format, db_connection, input_shp])

'''
pygeocb=# \d geodata.bikeways
                                                 Table "geodata.bikeways"
    Column    |                  Type                  | Collation | Nullable |                  Default                  
--------------+----------------------------------------+-----------+----------+-------------------------------------------
 ogc_fid      | integer                                |           | not null | nextval('bikeways_ogc_fid_seq'::regclass)
 name         | character varying(30)                  |           |          | 
 type         | character varying(30)                  |           |          | 
 wkb_geometry | public.geometry(MultiLineString,26910) |           |          | 
Indexes:
    "bikeways_pkey" PRIMARY KEY, btree (ogc_fid)
    "bikeways_wkb_geometry_geom_idx" gist (wkb_geometry)
'''

