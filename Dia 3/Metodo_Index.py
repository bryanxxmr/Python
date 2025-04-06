#indice o index
mi_texto = "Esto es una prueba de texto"
resultado = mi_texto[-4]

#print(resultado)

texto = "Esto es una prueba de texto"
resultado1 = texto.index("n") #retorna el indice de la primera letra n encontrada
#print(resultado)


texto2 = "Esto es una prueba de texto"
resultado2 = texto2.index("a",5)    #lo que estamos haciendo es que busque la letra a desde el indice 5
#print(resultado2)

texto3 = "Esto es una prueba de texto"
resultado3 = texto3.rindex("o") #busca la letra o desde el final
print(resultado3)

#Ejercicio 1
#Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[4])

#Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)


#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado3 = frase.rindex("práctica")
print(resultado3)