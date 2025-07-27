#Multiplicacion de cadenas
texto1 = "Ken"
#print(texto1*5)

#saltos de linea
texto2 = """Hola estoy
llevando el 
curso de Python"""
#print(texto2)

#consulta de palabra o caracteres
texto3 = """Hola estoy
llevando el 
curso de Python"""
#print("Libro" in texto3) #True


#consulta de palabra o caracteres
texto4 = """Hola estoy
llevando el 
curso de Python"""
print("Libro" not in texto4) #True

#propiedad len
texto5 = """Hola estoy
llevando el 
curso de Python"""
print(len(texto5))

#Practica1
#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla.
#Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
texto6 = "Repetición"
print(texto6*15)

#Practica2
#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#"Tierra mojada,"
#"mis recuerdos de viaje"
#"entre las lluvias"
haiku = """Tierra mojada,
mis recuerdos de viaje
entre las lluvias"""
print("agua" not in haiku) #True

#Practica3
#Imprime la longitud del siguiente string. Debes utilizar la función len() para obtener el resultado.
#"""El cielo es azul,
#las nubes son blancas
#y el sol brilla radiante."""
haiku2 = """El cielo es azul,
las nubes son blancas
y el sol brilla radiante."""
print(len(haiku2)) # 64