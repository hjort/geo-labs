for url in `cat inpe_catalog_2022_7_7_15_32_18.txt`; do arq=`echo $url | sed 's/^.*WGS84\/\(AMAZONIA_1.*\)?.*$/\1/'`; echo "[$arq]"; wget $url -O $arq; done
