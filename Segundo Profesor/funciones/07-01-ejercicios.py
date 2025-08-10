def no_espacios(texto):
    nuevo_texto = ""
    for caracter in texto:
        if caracter != " ":
            nuevo_texto += caracter
    return nuevo_texto


def es_palindromo(texto):
    texto = no_espacios(texto)
    print(texto)


es_palindromo("amor la paloma")
