import numpy as np
import matplotlib.pyplot as plt

with open('dftrain.csv') as fp:

	# Lectura de csv linea por linea para representar una grafica de los valores en Y y el tiempo en X.

	i = 0
	next(fp) # Salto de la primera linea del archivo. En dftrain.csv la primera linea es una enumeracion de las columnas de 0 a 61439
	for line in fp:
		i += 1
		lista = [float(j) for j in line.split(",")[1:]] #la primera columna es el id de la secuencia. Se elimina para poder ver la grafica. 

		print ("Secuencias leidas: ", i)
		indices = list(range(len(lista)))

		plt.figure()
		plt.plot(indices, lista, '-')
		plt.show()
		#plt.savefig('graf/general/' + str(i) + 'graf.png') GUARDAR GRAFICA