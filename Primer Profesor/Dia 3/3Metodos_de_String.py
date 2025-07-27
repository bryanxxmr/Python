# Ejemplo 1
texto1 = "Este es el texto de Kenny Mendoza"
resultado1 = texto1.upper() #convierte el texto a mayusculas
#print(resultado1)

#Ejemplo 2
texto2 = "Este es el texto de Kenny Mendoza"
resultado2 = texto2[2].upper() #convierte el texto a mayusculas
#print(resultado2)

#Ejemplo 3
texto3 = "Este es el texto de Kenny Mendoza"
resultado3 = texto3.lower() #convierte el texto a minusculas
#print(resultado3)

#Ejemplo 4
texto4 = "Este es el texto de Kenny Mendoza"
resultado4 = texto4.split() #convierte el texto en una lista
#print(resultado4)

#Ejemplo 5
texto5 = "Este es el texto de Kenny Mendoza"
resultado5 = texto5.split("e") #separa el texto en una lista por la letra e
#print(resultado5)

#Ejemplo 6
valor1 = "Hola"
valor2 = "Mundo"
valor3 = "como"
valor4 = "estan"
valor5 = "-".join([valor1, valor2, valor3, valor4]) #une los valores en una sola cadena y el separador es un espacio
#print(valor5)

#Ejemplo 7
texto6 = "Este es el texto de Kenny Mendoza"
resultado6 = texto6.find("l") #busca la letra l y retorna el indice de la primera letra l encontrada
#print(resultado6)

#Ejemplo 8
texto7 = "Este es el texto de Kenny Mendoza"
resultado7 = texto7.replace("e", "a") #reemplaza la letra e por la letra a
print(resultado7)

#Practica 1
#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
respuesta = frase.upper()
print(respuesta)

#Practica 2
#Une la siguiente lista en un string, separando cada elemento con un espacio.
# Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado. lista_palabras = ["La","legibilidad","cuenta."]
lista_palabras = ["La","legibilidad","cuenta."]
respuesta2 = " ".join(lista_palabras) #une los valores en una sola cadena y el separador es un espacio
print(respuesta2)

#Practica 3
#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil"
#"mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
nuevafrase = frase.replace("difícil","fácil")
nuevafrase2= nuevafrase.replace("mala","buena")
print(nuevafrase2)
