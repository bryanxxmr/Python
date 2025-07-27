#set se pueden declarar de la siguiente manera
# set1 = {1,2,3,4,5} o set1 = set([1,2,3,4,5])
#solo admite valores unicos, no estan ordenados en indices
#no se pueden organizar, no se pueden modificar

#Ejemplo1 declara un set con valores unicos y imprimir el tipo
mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)

#Ejemplo2
otro_set = {1,2,3,4,5}
#print(type(otro_set))
#print(otro_set)

#Ejemplo3 Valores unico:
A_set = {1,2,3,4,5,5,5,5,4,4,4,3,3,3,2,2,2,1}
#print(type(A_set))
#print(A_set)

#Ejemplo4 No permite Listas
#B_set = {1,2,3,[4,5]} #TypeError: unhashable type: 'list'
#print(B_set)

#Ejemplo5 No permite Diccionarios
#C_set = {1,2,3,{4:5}} #TypeError: unhashable type: 'dict'
#print(C_set)

#Ejemplo6 Si permite Tuplas
#mi_set = {(1, 2), (3, 4), (5, 6)}
#print(mi_set)

#Ejemplo7 - usar la funcion len para contar los elementos
mi_setD = set((1,2,3,4,5))
#print(len(mi_setD))

#Ejemplo8 - encontrar un valor en el set
mi_setE = set((1,2,3,4,5))
#print(2 in mi_setE) #True

#Ejemplo9 -unir dos sets
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)
#print(set3)

#Ejemplo10 - agregar un elemento a un set
setD = {1,2,3}
setD.add(4)
#print(setD)

#Ejemplo11 - eliminar un elemento de un set
setE = {1,2,3}
setE.remove(2)
#print(setE)

#Ejemplo12 - metodo discard - no lo elimina solo lo descarta
setF = {1,2,3}
setF.discard(2)
#print(setF)

#Ejemplo13 - metodo pop - elimina un elemento aleatorio
setG = {1,2,3}
sorteo = setG.pop()
#print(sorteo)

#Ejemplo14 - metodo clear - elimina todos los elementos
setH = {1,2,3}
setH.clear()
print(setH)

#Practica1
#Une los siguientes sets en uno solo, llamado mi_set_3:
#{1, 2, "tres", "cuatro"}
#{"tres", 4, 5}
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
#print(mi_set_3)

#Practica2
#Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
#sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

#Practica3
#Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
#sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")


