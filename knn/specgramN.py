import numpy as np
import matplotlib.pyplot as plt
import signal

with open('../dfvalid.csv') as fp:

	seqId = 401
	# Lectura de csv linea por linea. Cada linea es una secuencia de una sola variable medida varias veces. 

	i = 0
	next(fp)   # Salto de la primera linea del archivo. En dftrain.csv la primera linea es una enumeracion de las columnas de 0 a 61439
	for line in fp:
		#print ("Secuencia ", i)
		if i >= seqId:
			print(i)
			print(line.split(",")[0])
			lista = [float(j) for j in line.split(",")[1:]] #la primera columna es el id de la secuencia. Se elimina para poder ver la grafica. 
			plt.figure()
			plt.specgram(lista,NFFT=512,Fs=61.44,window=np.hamming(512),noverlap=256,cmap='Greys')
			plt.show()
			plt.close()

			indices = list(range(len(lista)))
			plt.figure()
			plt.plot(indices, lista, '-')
			plt.show()
			plt.close()
		
		i += 1

# comentar en el slack

# https://github.com/kvfrans/variational-autoencoder descargar y probar. Intentar usarlo para train

# Pintar tambien con el tiempo ademas del spectrogram threads