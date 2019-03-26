import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier  
import operator


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
classifier = KNeighborsClassifier(n_neighbors=5) 
classifier.fit(np.delete(x_train, 0, axis=1), y_train)  

print("Predecir:: ")

seqId = 0
resultado = []
positivos = 0
negativos = 0

for secuencia in x_valid:
	x_test = np.array([secuencia])
	distances, indices = classifier.kneighbors(X=np.delete(x_test, 0, axis=1), n_neighbors=5, return_distance=True)
	#print("Indice actual ", seqId)
	#print("Distancias ", distances)
	#print("iind     ", indices)
	#input()

	if np.sum(distances) >= 58.834819: # anomalia
		clase = 1
		positivos +=1
	else:  # normal
		clase = 0
		negativos +=1

	resultado.append([x_test[0][0], clase])
	seqId +=1


print('positivos ', positivos)
print('negativos ', negativos)
resultado = np.array(resultado, dtype=int)
np.savetxt("result" + '.csv',  resultado, fmt='%i', delimiter=',')

		


""""
Otra manera con aprendizaje supervisado: autoencoder y prediccion de señales
""" 