def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("chanchito")
l = largo("Hola")
print(l)  # Debería imprimir 4
