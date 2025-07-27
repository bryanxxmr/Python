
#Ejemplo1
texto = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
fragmento = texto[2:6] #extraemos el texto desde el indice 2 hasta el 5 no incluido el 6
#print(fragmento)

#Ejemplo2
texto1 = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
fragmento1 = texto1[4:] #extraemos el texto desde el indice 4 hasta el final
#print(fragmento1)

#Ejemplo3
texto3 = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
fragmento3 = texto3[:5] #extraemos el texto desde el inicio hasta el indice 5 no incluido el  5
#print(fragmento3)

#Ejemplo4
texto4 = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
fragmento4 = texto4[5:15:3] #extraemos el texto desde el indice 5 hasta el 14 no incluido el 15 y de 3 en 3
#print(fragmento4)

#Ejemplo5
texto5 = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
fragmento5 = texto5[::-2] # extraemos el texto desde el final hasta el inicio de 2 en 2
#print(fragmento5)

#Practica1
#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
#"Controlar la complejidad es la esencia de la programación"
frase = "Controlar la complejidad es la esencia de la programación"
resultado = frase[:9] #extraemos el texto desde el inicio hasta el indice 9 no incluido el 9
print(resultado)

#Practica2
#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado2 = frase2[8::3] #extraemos el texto desde el indice 8 hasta el final de 3 en 3
#print(resultado2)

#Practica3
#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase3 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado3 = frase3[::-1] #extraemos el texto desde el final hasta el inicio
print(resultado3)