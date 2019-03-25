import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier  
import operator


"""
ESTE SCRPIT CREA UN .DATA CON VECTORES DE MEDIAS HORIZONTALES DE ESPECTROGRAMAS
TENER EN CUENTA QUE EL PRIMER ELEMENTO DE CADA FILA ES EL ID DE LA SECUENCIA
"""

fichero = 'dfvalid'
#fichero = 'dftrain'

with open('../' +  fichero + '.csv') as fp:
	
	i = 0
	next(fp)
	x_train = np.zeros((1,258)) # Inicializar con una row que luego se elimina

	for line in fp:
		i += 1
		lista = [float(j) for j in line.split(",")]

		indices = list(range(len(lista)))

		plt.figure()
		spectrums, freqs, bins, im = plt.specgram(lista[1:],NFFT=512,Fs=61.44,window=np.hamming(512),noverlap=256,cmap='Greys')

		# MEDIAS: https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
		medias = np.mean(spectrums, axis=1) #media de cada fila
		x_train = np.append(x_train, np.array([np.append([lista[0]], medias)]), axis=0)
		plt.close()

		if i % 100 == 0:
			print("Iteracion ", i)

	x_train = np.delete(x_train, (0), axis=0) 
	np.savetxt(fichero + '.data',  x_train, delimiter=',')