#Diccionarios es una estructura de datos que permite almacenar pares de clave-valor,
#no tienen un orden definido, se accede a los valores a traves de la clave
#es mutable, se pueden agregar o eliminar elementos
#se define con {}

mi_diccionario = {'clave1': 'valor1','clave2': 'valor2','clave3': 'valor3'}
#print(mi_diccionario) #imprime {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}

resultado = mi_diccionario['clave1'] #acceder al valor de la clave1
#print(resultado) #imprime valor1

#Ejemplo 2
cliente = {'cliente' : 'Kenny', 'apellido' : 'Mendo', 'peso' : 90, 'altura' : 1.80}
consulta =  cliente['altura'] #acceder al valor de la clave apellido
#print(consulta)

#Ejemplo 3
diccio = {'clave1':55, 'clave2': [10,20,30], 'clave3': {'subclave1': 100, 'subclave2': 200}}
#print(diccio['clave2'][1]) #imprime 20

#Ejemplo 4
mi_dicc = {'clave1': 10, 'clave2': [1, 2, 3], 'clave3': {'subclave1': 100, 'subclave2': 200}}
#print(mi_dicc['clave3']['subclave1']) #imprime 100

#Ejemplo 5
mi_dicc2 = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f'], 'c3':['g', 'h', 'i']}
#print(mi_dicc2['c2'][1].upper()) #imprime E en mayuscula

#Ejemplo 6 Agregar un elemento a un diccionario
mi_dicc3 = {1: 'a', 2 : 'b'}
mi_dicc3[3] = 'c' #agregar un elemento al diccionario
#print(mi_dicc3)

#Ejemplo 7 Sobreescribir un elemento de un diccionario
mi_dicc4 = {1: 'a', 2 : 'b'}
mi_dicc4[1] = 'A' #sobreescribir un elemento del diccionario
#print(mi_dicc4) #imprime {1: 'A', 2: 'b'}

#Ejemplo 8 Eliminar un elemento de un diccionario
mi_dicc5 = {1: 'a', 2 : 'b'}
mi_dicc5.pop(1) #eliminar un elemento del diccionario
#print(mi_dicc5) #imprime {2: 'b'}

#Ejemplo 9 Imprimir las claves de un diccionario
mi_dicc6 = {1: 'a', 2 : 'b'}
#print(mi_dicc6.keys()) #imprime dict_keys([1, 2])

#Ejemplo 10 Imprimir los valores de un diccionario
mi_dicc7 = {1: 'a', 2 : 'b'}
#print(mi_dicc7.values()) #imprime dict_values(['a', 'b'])

#Ejemplo 11 Imprimir los elementos de un diccionario
mi_dicc8 = {1: 'a', 2 : 'b'}
print(mi_dicc8.items()) #imprime dict_items([(1, 'a'), (2, 'b')])

#Practica1
#Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
#Los nombres de las claves y valores deben ser iguales a la consigna.
mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}

#Practica2
#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición.
#Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#Practica3
#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda),
# y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
mi_dica = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dica["edad"] = 36
mi_dica["ocupacion"] = "Editora"
mi_dica["pais"] = "Colombia"