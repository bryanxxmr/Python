#Conversion implicita
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

#Conversion explicita
valor1 = 5.8
print(valor1)
print(type(valor1))

valor2 = int(valor1)
print(valor2)
print(type(valor2))

edad1 = input("Dame tu edad: ")
edad1 = int(edad1)
nueva_edad = edad1 + 5
print(nueva_edad)

#Ejercicio 1
#Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
num1 = 7.5
num1 = int(num1)
print(type(num1))

#Ejercicio 2
#Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
num2 = 10
num2 = float(num2)
print(type(num2))

#Ejercicio 3
#Suma los valores de num1 y num2.
#No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print()
num1 = "7.5"
num2 = "10"
print(float(num1) + int(num2))