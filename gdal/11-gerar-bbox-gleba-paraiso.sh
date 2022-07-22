ogr2ogr -sql "select Extent(geometry) from gleba_paraiso" -dialect SQLite gleba_paraiso_bbox gleba_paraiso.shp
