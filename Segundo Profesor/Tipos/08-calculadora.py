numero1 = input("Ingresa primer número: ")
numero2 = input("Ingresa segundo número: ")
numero1 = int(numero1)  # Convertimos el primer número a entero
numero2 = int(numero2)  # Convertimos el segundo número a entero

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

mensaje = f"""
Para los numoros {numero1} y {numero1}, los resultados son:
Suma: {suma}
Resta: {resta}
Multiplicación: {multiplicacion}
División: {division}
"""
print(mensaje)
