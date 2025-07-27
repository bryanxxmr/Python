#Tuplas son similares a listas, pero no se pueden modificar
# Tuplas son inmutables
#ocupan menos espacio en memoria que listas
# Tuplas son mas rapidas que listas

#Ejemplo1
mi_tuple = 1, 2, 3, 4, 5
#print(type(mi_tuple)) #imprime el tipo de dato <class 'tuple'>

#Ejemplo2
mi_tuple2 = (1, 2, 3, 4, 5)
#print(mi_tuple2[0]) #imprime el primer elemento de la tupla

#Ejemplo3
mi_tuple3 = (1, 2, 3, 4, 5)
#print(mi_tuple3[-2]) #imprime el penultimo elemento de la tupla

#Ejemplo4
mi_tuple4 = (1, 2, (10,100) , 4, 5)
#print(mi_tuple4[2][1]) #imprime el segundo elemento de la tupla dentro de la tupla

#Ejemplo5
mi_tuple5 = (1, 2, 3, 4, 5)
mi_tuple5 = list(mi_tuple5) #convertir la tupla en lista
#print(type(mi_tuple5))

#Ejemplo6
tuplaA = (1, 2, 3)
x,y,z = tuplaA #desempaquetar la tupla
#print(x,y,z) #imprime 1 2 3

#Ejemplo7
tuplaB = (1, 2, 3, 4, 5)
#print(len(tuplaB)) //imprime la longitud de la tupla

#Ejemplo8
tuplaC = (1, 2, 3, 4, 5, 1 , 1 , 1)
#print(tuplaC.count(1)) #imprime la cantidad de veces que se repite el elemento 1

#Ejemplo9
tuplaD = (1, 2, 3, 4, 5)
print(tuplaD.index(3)) #imprime la posicion del elemento 3

#Practica
#Ejercicio1
#Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2)) #imprime la cantidad de veces que se repite el elemento 2