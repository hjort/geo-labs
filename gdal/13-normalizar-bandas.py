import numpy as np 
from PIL import Image

bandas = {}
vetores = {}
normais = {}

def normalizar(banda):
    return banda / 2 ** 16

for i in range(2, 8):
	print("[B0%i]" % i)

	banda = Image.open('B0%i_paraiso.tif' % i)
	bandas[i] = banda
	vetor = np.array(banda)
	vetores[i] = vetor

	print(type(banda), type(vetor))
	print(banda.size, vetor.shape, vetor.dtype)
	del(banda)

	print('Antes: ', np.min(vetor), 'a' , np.max(vetor))
	normal = normalizar(vetor)
	print('Depois:', np.min(normal), 'a' , np.max(normal))

	img = Image.fromarray(normal)
	img.save('B0%i_paraiso_normal.tif' % i)

	print('')

