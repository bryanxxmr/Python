#Primer operador logico "and" "or" "not"

#Primer operador logico "and"
variable1 = (10 == 10) and ('Perro' == 'Perro')
#print(variable1) #Imprime True ya que ambas condiciones son verdaderas

#Segundo operador logico "or"
variable2 = (10 == 10) or ('Perro' == 'Gato')
#print(variable2) #Imprime True ya que al menos una de las condiciones es verdadera

#Tercer operador logico "not"
variable3 = not (10 == 10)
print(variable3) #Imprime False ya que la condición es verdadera y el operador not la niega

#Practica 1
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1 > num2) and (num1 < num3)

#Practica 2
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1 > num2) or (num1 < num3)

#Practica 3
#Verifica si las palabras almacenadas en las siguientes variables:
#palabra1 = "éxito", y
#palabra2 = "tecnología"
#no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
#"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
mi_bool = not (palabra1 in frase) and not (palabra2 in frase)
print(mi_bool) #Imprime True ya que ambas palabras no están en la frase