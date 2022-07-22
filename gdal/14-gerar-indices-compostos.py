import numpy as np 
from PIL import Image

vetores = {}

for i in range(2, 8):
	print("[B0%i]" % i)

	banda = Image.open('B0%i_paraiso_normal.tif' % i)
	vetor = np.array(banda)
	vetores[i] = vetor
	del(banda)

# NDVI
b5 = vetores[5]
b4 = vetores[4]
print('B5:', np.min(b5), 'a', np.max(b5))
print(b5)
print('B4:', np.min(b4), 'a', np.max(b4))
print(b4)
ndvi = (b5 - b4) / (b5 + b4)
ndvi2 = ndvi[~np.isnan(ndvi)]
print('NDVI:', np.min(ndvi2), 'a', np.max(ndvi2))
#print(ndvi)
ndvi = (ndvi * 255.999).astype('uint16')
print(ndvi)
img = Image.fromarray(ndvi)
img.save('paraiso_ndvi.tif')

# NDWI
b5 = vetores[5]
b3 = vetores[3]
ndwi = (b5 - b3) / (b5 + b3)
#print('NDWI:', np.min(ndwi), 'a', np.max(ndwi))
img = Image.fromarray(ndwi * 255) #255.999)
img.save('paraiso_ndwi.tif')

