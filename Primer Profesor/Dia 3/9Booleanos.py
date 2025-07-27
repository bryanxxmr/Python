#Ejemplo1 Imprime el tipo de dato
var1 = True
var2 = False
#print(type(var1))
#print(type(var2))

#Ejemplo2 Operaciones con booleanos
numero = 5 > 3 + 2
#print(type(numero))
#print(numero)

#Ejemplo3 Operaciones con booleanos
numero1 = 5 == 4+1
#print(type(numero1)) #imprime el tipo de dato
#print(numero1) #imprime el valor

#Ejemplo4 Operaciones con booleanos
numero2 = 5 != 4+1
#print(type(numero2)) #imprime el tipo de dato
#print(numero2) #imprime el valor

#Ejemplo5 Operaciones con booleanos
valor = bool(5>3)
#print(type(valor)) #imprime el tipo de dato
#print(valor) #imprime el valor

#Ejemplo6 Operaciones con booleanos
dato = [1, 2, 3, 4, 5]
resultado = 6 in dato
print(type(resultado)) #imprime el tipo de dato
print(resultado) #imprime False ya que 6 no está en la lista

#Practica 1
#Realiza una comparación que arroje como resultado un booleano y
#almacena el resultado (True/False) en una variable llamada prueba
prueba = 10 > 5
print(type(prueba)) #imprime el tipo de dato
print(prueba) #imprime el valor

#Practica 2
#Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
valor = 17834/34 > 87*56
print(valor)

#Practica 3
#Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano)
# en pantalla utilizando print()
valor = 25 ** 0.5 == 5
print(valor)