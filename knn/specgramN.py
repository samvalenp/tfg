import numpy as np
import matplotlib.pyplot as plt

with open('dftrain.csv') as fp:

	seqId = 1010
	# Lectura de csv linea por linea. Cada linea es una secuencia de una sola variable medida varias veces. 

	i = 0
	next(fp)   # Salto de la primera linea del archivo. En dftrain.csv la primera linea es una enumeracion de las columnas de 0 a 61439
	for line in fp:
		print ("Secuencia ", i)
		if i >= seqId:
			lista = [float(j) for j in line.split(",")[1:]] #la primera columna es el id de la secuencia. Se elimina para poder ver la grafica. 
			plt.figure()
			plt.specgram(lista,NFFT=512,Fs=61.44,window=np.hamming(512),noverlap=256,cmap='Greys')
			plt.show()
		
		i += 1
		