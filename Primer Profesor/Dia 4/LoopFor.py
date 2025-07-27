lista = ['A', 'B', 'C', 'D']

for letra in lista: #letra toma el valor de cada elemento de la lista
    numero_letra = lista.index(letra) + 1 #letra toma el valor de cada elemento de la lista
    print(f"Letra {numero_letra}: {letra}") #imprime el valor de letra y su posición

#Ejemplo de bucle con if
nombres = ['Juan', 'Pedro', 'Maria', 'Ana', 'Luis'] #lista de nombres
for nombre in nombres:  #nombre toma el valor de cada elemento de la lista
    if nombre.startswith('J'): #si el nombre empieza con J
        print(f"Hola {nombre}, bienvenido!") #imprime el nombre que empieza con J
    else:
        print(f"Tu nombre no empieza con J, pero igual bienvenido {nombre}!")

#Otro ejemplo de bucle con if
numeros = [1, 2, 3, 4, 5] #lista de numeros
suma = 0 #inicializa la suma en 0
for elemento in numeros: #elemento toma el valor de cada elemento de la lista
    suma = suma + elemento #suma el elemento a la suma
print(suma) #imprime la suma

#Loop for con lista
for a in [[1, 2], [3, 4], [5, 6]]:
    print(a)

#Loop for con lista
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

#Loop con diccionario
dic = {'clave1' : 'a', 'clave2' : 'b', 'clave3' : 'c'} #diccionario
for clave in dic.values(): #clave toma el valor de cada elemento del diccionario
    print(clave) #imprime la clave y el valor


#Practica1
#Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
#Por ejemplo: "Hola María"
#alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"] #lista de alumnos
for alumno in alumnos_clase: #alumno toma el valor de cada elemento de la lista
    print(f"Hola {alumno}") #imprime el nombre del alumno

#Practica2
#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For
# y almacena el resultado de la suma en una variable llamada suma_numeros:
#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] #lista de numeros
suma_numeros = 0 #inicializa la suma en 0
for numero in lista_numeros: #numero toma el valor de cada elemento de la lista
    suma_numeros = suma_numeros + numero #suma el numero a la suma
print(suma_numeros) #imprime la suma

#Practica3
#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:
#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
#*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar
#num % 2 == 0 (valores pares)
#num % 2 == 1 (valores impares)
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] #lista de numeros
suma_pares = 0 #inicializa la suma de pares en 0
suma_impares = 0 #inicializa la suma de impares en 0
for numero in lista_numeros: #numero toma el valor de cada elemento de la lista
    if numero % 2 == 0: #si el numero es par
        suma_pares = suma_pares + numero #suma el numero a la suma de pares
    else: #si el numero es impar
        suma_impares = suma_impares + numero #suma el numero a la suma de impares

