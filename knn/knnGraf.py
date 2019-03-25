import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier  
import operator


K = 5

# analizar la media vertical de los spectogramas con Knn. EN PROCESO
class Rank(object):

	def __init__(self, ind, distance):
		self.ind = ind
		self.distance = distance


	def __repr__(self):
		return "(%i | %f)  " % (self.ind, self.distance)


	
	
x_train = np.genfromtxt('dftrain.data', delimiter=',')
x_valid = np.genfromtxt('dfvalid.data', delimiter=',')
print("--Creacion del dataset terminada--")
y_train = np.zeros((x_train.shape[0],1))


print(x_train.shape)

#  NORMALIZACION No es necesaria de hacer.
#scaler = StandardScaler()  
#scaler.fit(x_train)
#x_train = scaler.transform(x_train)

#datos
print("Entrenando:  ")
classifier = KNeighborsClassifier(n_neighbors=K) 
classifier.fit(np.delete(x_train, 0, axis=1), y_train)  

print("Predecir:: ")

seqId = 0
sumas = []
for secuencia in x_valid:
	x_test = np.array([secuencia])
	distances, indices = classifier.kneighbors(X=np.delete(x_test, 0, axis=1), n_neighbors=K, return_distance=True)
	#print("Indice actual ", seqId)
	#print("Distancias ", distances)
	#print("iind     ", indices)
	#input()

	sumas.append(Rank(x_test[0][0], np.sum(distances)))
	seqId +=1

ordenado = sorted(sumas, reverse=True, key=operator.attrgetter('distance'))
print(ordenado)
ordenado = [j.distance for j in ordenado]
numeroDeSeq = list(range(len(ordenado)))
plt.figure()
plt.plot(numeroDeSeq, ordenado, '-')
plt.show()
plt.close()


""""
Otra manera con aprendizaje supervisado: autoencoder y prediccion de señales
""" 