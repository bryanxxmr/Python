
mi_lista1 = ['a', 'b', 'c']
#print(type(mi_lista1)) #imprime el tipo de dato <class 'list'>

#imprimir la cantidad de elementos de la lista
mi_lista2 = ['a', 'b', 'c', 1, 2, 3]
resultado_lista2 = len(mi_lista2)
#print(resultado_lista2)

#extraer un elemento de la lista
mi_lista3 = ['a', 'b', 'c', 1, 2, 3]
resultado_lista3 = mi_lista3[0] #extrae el primer elemento de la lista
#print(resultado_lista3)

#extraer un elementos desde una posicion especifica hasta el final
mi_lista4 = ['a', 'b', 'c', 1, 2, 3]
resultado_lista4 = mi_lista4[1:4] #extrae el segundo elemento hasta el cuarto
#print(resultado_lista4)

#concatenar listas
mi_lista5 = ['a', 'b', 'c']
mi_lista6 = [1, 2, 3]
#print(mi_lista5+mi_lista6) #imprime ['a', 'b', 'c', 1, 2, 3]

#concatenar listas con otra lista
mi_lista7 = ['a', 'b', 'c']
mi_lista8 = [1, 2, 3, 4, 5, 6]
mi_lista9 = mi_lista7 + mi_lista8
#print(mi_lista9) #imprime ['a', 'b', 'c', 1, 2, 3, 4, 5, 6]

#sobreescribir un elemento de la lista
mi_lista10 = ['a', 'b', 'c']
mi_lista11 = [1, 2, 3]
mi_resultado_lista10 = mi_lista10 + mi_lista11 #concatenar listas
mi_resultado_lista10[0] = 'Alfa' #sobreescribir el primer elemento de la lista
#print(mi_resultado_lista10)

#metodo append
mi_lista12 = ['a', 'b', 'c']
mi_lista13 = [1, 2, 3]
suma_lista = mi_lista12 + mi_lista13 #concatenar listas
suma_lista.append('d') #agregar un elemento al final de la lista
#print(suma_lista) #imprime ['a', 'b', 'c', 1, 2, 3, 'd']

#metodo pop
mi_lista14 = ['a', 'b', 'c']
mi_lista15 = [1, 2, 3]
mi_lista16 = mi_lista14 + mi_lista15 #concatenar listas
mi_lista16.pop()    #eliminar el ultimo elemento de la lista
#print(mi_lista16)

#metodo pop Ejemplo 2
mi_lista17 = ['a', 'b', 'c']
mi_lista18 = [1, 2, 3]
mi_lista19 = mi_lista17 + mi_lista18 #concatenar listas
mi_lista19.pop(0) #eliminar el primer elemento de la lista
#print(mi_lista19) #imprime ['b', 'c', 1, 2, 3]

#metodo pop Ejemplo 3
mi_lista20 = ['a', 'b', 'c']
mi_lista21 = [1, 2, 3]
mi_lista22 = mi_lista20 + mi_lista21 #concatenar listas
elimindo = mi_lista22.pop(0) #eliminar el primer elemento de la lista
#print(mi_lista22)
#print(elimindo)

#meotod sort
n_lista1 = ['c', 'b', 'a', 'z', 'y', 'x']
n_lista1.sort()
#print(n_lista1)

#metodo reverse
n_lista2 = ['c', 'b', 'a', 'z', 'y', 'x']
n_lista2.sort()
n_lista2.reverse()
print(n_lista2) #imprime ['z', 'y', 'x', 'c', 'b', 'a']
