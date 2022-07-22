import numpy as np 
from PIL import Image

# converte valores para números entre 0.0 e 1.0
# assume-se que o tipo de entrada é UInt16 (inteiro positivo de 16 bits)
def normalizar(dados):
    return dados / 2 ** 16

# realça o contraste da imagem através da alteração do histograma (percentual cumulativo)
def realcar_contraste(img, min_percent=2, max_percent=98):
  lo, hi = np.percentile(img, (min_percent, max_percent))
  res_img = (img.astype(float) - lo) / (hi - lo)
  return np.maximum(np.minimum(res_img * 255, 255), 0).astype(np.uint8)

bandas = {}
bandas_necessarias = (4, 5)

for i in bandas_necessarias:
	print("[B0%i]" % i)

	banda = Image.open('B0%i_paraiso.tif' % i)
	vetor = np.array(banda)
	normal = normalizar(vetor)

	bandas[i] = normal

	print("Tipos:", type(banda), type(vetor), type(normal))
	print(banda.size, vetor.shape, vetor.dtype)
	del(banda)

	print('Antes: ', np.min(vetor), 'a' , np.max(vetor))
	print('Depois:', np.min(normal), 'a' , np.max(normal))

	#img = Image.fromarray(normal)
	#img.save('B0%i_paraiso_normal.tif' % i)

	print('')

# NDVI
b5 = bandas[5]
b4 = bandas[4]

print('B5:', np.min(b5), 'a', np.max(b5))
print(b5)

print('B4:', np.min(b4), 'a', np.max(b4))
print(b4)

ac = 0.05 #1e-5
ndvi = (b5 - b4 - ac) / (b5 + b4 + ac)
print('NDVI:', np.min(ndvi), 'a', np.max(ndvi))
print(ndvi)

ndvin = ndvi[~np.isnan(ndvi)]
print('NDVIn:', np.min(ndvin), 'a', np.max(ndvin))
print(ndvin)

ndvim = (ndvi * 255.999).astype('uint16')
print('NDVIm:', np.min(ndvim), 'a', np.max(ndvim))
print(ndvim)

ndvic = realcar_contraste(ndvi)
print('NDVIc:', np.min(ndvic), 'a', np.max(ndvic))
print(ndvic)

img = Image.fromarray(ndvic)
img.save('paraiso_ndvi3.tif')

ndvif = ndvic / 255.0 * 2 - 1
print('NDVIf:', np.min(ndvif), 'a', np.max(ndvif))
print(ndvif)

img = Image.fromarray(ndvif)
img.save('paraiso_ndvi5.tif')

