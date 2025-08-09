def suma(*variosNumeros):
    total = 0
    for numero in variosNumeros:
        total += numero
    print(f"La suma de los números es: {total}")


suma(1, 2, 3, 4, 5)
suma(10, 20, 30)
suma(100, 200, 300, 400, 500, 600)
