import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier  
import operator

# analizar la media vertical de los spectogramas con Knn. EN PROCESO
class Rank(object):

	def __init__(self, ind, distance):
		self.ind = ind
		self.distance = distance


	def __repr__(self):
		return "(%i | %f)  " % (self.ind, self.distance)

with open('dftrain.csv') as fp:

	"""i = 0    DESCOMENTAR PARA CARGAR EL DATA DESDE EL FICHERO dftrain.csv EN LUGAR DE DESDE DFTRAIN.DATA
	next(fp)
	x_train = np.zeros((1,257)) # Inicializar con una row que luego se elimina

	for line in fp:
		i += 1
		lista = [float(j) for j in line.split(",")[1:]]

		indices = list(range(len(lista)))

		plt.figure()
		#plt.plot(indices, lista, '-')
		spectrums, freqs, bins, im = plt.specgram(lista,NFFT=512,Fs=61.44,window=np.hamming(512),noverlap=256,cmap='Greys')

		#medias = np.mean(a, axis=0)  https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
		medias = np.mean(spectrums, axis=1) #media de cada fila
		x_train = np.append(x_train, np.array([medias]), axis=0)
		plt.close()

		if i % 100 == 0:
			print("Iteracion ", i)


	np.savetxt('dftrain.data', x_train, delimiter=',')"""
	

	x_train = np.genfromtxt('dftrain.data', delimiter=',')
	print("--Creacion del dataset terminada--")
	x_train = np.delete(x_train, (0), axis=0) #elimino la primera row
	y_train = np.zeros((x_train.shape[0],1))



	print(x_train.shape)
	#  NORMALIZACION
	#scaler = StandardScaler()  
	#scaler.fit(x_train)
	#x_train = scaler.transform(x_train)

	#datos

	print("Entrenando:  ")
	classifier = KNeighborsClassifier(n_neighbors=5) 
	classifier.fit(x_train, y_train)  

	print("Predecir:: ")

	seqId = 0
	sumas = []
	for secuencia in x_train:
		x_test = np.array([secuencia])
		distances, indices = classifier.kneighbors(X=x_test, n_neighbors=5, return_distance=True)
		#print("Indice actual ", seqId)
		#print("Distancias ", distances)
		#print("Inices     ", indices)
		#input()

		sumas.append(Rank(seqId, np.sum(distances)))
		seqId +=1

	print(sorted(sumas, reverse=True, key=operator.attrgetter('distance')))

		


""""specgram puede devolver una matriz. Hacer una media creando un vector vertical el cual sera la entrada para un modelo knn con cross validation y v
ver cuales las clasifica como anomalas. La salida del knn es la distancia minima.


SUBIR SCRIPTS Y RESULTADOS


Testear vector a vector escogiendo la tercera distancia como comparacion

No desordenarlos y coger los indices. Asi se puede ver como es el espectograma de la anomalia.


Otra manera con aprendizaje supervisado: autoencoder y prediccion de señales



""" 