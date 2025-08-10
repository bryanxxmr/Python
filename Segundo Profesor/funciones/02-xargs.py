def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
        print(f"Número actual: {numero}, Suma parcial: {resultado}")
    print(f"La suma es: {resultado}")


suma(2, 4, 5)  # Llamada a la función con varios argumentos
suma(4, 5, 6, 7, 8)  # Llamada a la función con más argumentos
