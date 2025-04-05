#integers (numeros enteros) y float (numeros decimales)

mi_numero = 5.8
mi_numero = mi_numero + mi_numero
print(mi_numero)

#imprimir el tipo de dato
print(type(mi_numero)) #int

edad = input("Dime tu edad: ")
print("Tu edad es: " + edad)


print(type(edad)) #str

nueva_edad = input("Dime tu edad: ")
print(nueva_edad + nueva_edad)


#Practica 1
#Declara una variable numérica llamada num_entero que contenga un valor de tipo entero de tu elección.
#Imprime el tipo de dato de dicha variable.
num_entero = 5

print(type(num_entero))

#Practica 2
#Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.
#Imprime el tipo de dato de dicha variable.
num_decimal = 3.5
print(type(num_decimal))


#Practica 3
#¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.
#Para ello, crea dos variables:
#num1 = 7.5
#num2 = 2.5
#A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

num1 = 7.5
num2 = 2.5

print(type(num1 + num2))