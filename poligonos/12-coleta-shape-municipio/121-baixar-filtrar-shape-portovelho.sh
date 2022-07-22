wget https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2021/UFs/RO/RO_Municipios_2021.zip

unzip -d RO_Municipios_2021 RO_Municipios_2021.zip 

dbf_dump RO_Municipios_2021/RO_Municipios_2021.dbf | grep "Porto Velho"

dbf_dump --info RO_Municipios_2021/RO_Municipios_2021.dbf 

MUN="RO_PortoVelho_2021"

rm -rf $MUN/ && mkdir $MUN/

ogr2ogr -f "ESRI Shapefile" \
  -where "CD_MUN = '1100205'" \
  $MUN/$MUN.shp \
  RO_Municipios_2021/RO_Municipios_2021.shp

zip -9 $MUN.zip $MUN/

find -ls

