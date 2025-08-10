# funcion que elimina los espacios de un texto
# y devuelve el texto sin espacios
def no_espacios(texto):
    nuevo_texto = ""
    for caracter in texto:
        if caracter != " ":
            nuevo_texto += caracter
    return nuevo_texto

# funcion que invierte un texto


def invertir_texto(texto):
    texto_invertido = ""
    for caracter in texto:
        texto_invertido = caracter + texto_invertido
    return texto_invertido

# creamos la funcion general que llamara a las otras funciones


def es_palindromo(texto):
    texto = no_espacios(texto)
    texto_invertido = invertir_texto(texto)
    print(texto)
    print(texto_invertido)


es_palindromo("kenny es un buen amigo")
