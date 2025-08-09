print('Bienvenido a la calculadora')
print('Para salir, escribe "salir"')
print('Para realizar una operación, escribe "suma", "resta", "multiplicación" o "división"')

resultado = ""

while True:
    # Verifica si 'resultado' está vacío
    if resultado == "":
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            print("Saliendo de la calculadora.")
            break
        resultado = int(resultado)
    operacion = input("Ingrese operación: ").lower()
    if operacion == "salir":
        print("Saliendo de la calculadora.")
        break
    numero2 = input("Ingrese otro numero: ")
    if numero2.lower() == "salir":
        print("Saliendo de la calculadora.")
        break
    numero2 = int(numero2)
    if operacion.lower() == "suma":
        resultado += numero2
    elif operacion.lower() == "resta":
        resultado -= numero2
    elif operacion.lower() == "mult":
        resultado *= numero2
    elif operacion.lower() == "div":
        if numero2 != 0:
            resultado /= numero2
        else:
            print("Error: División por cero no permitida.")
    else:
        print("Operación no reconocida. Intente de nuevo.")
    print(f"Resultado: {resultado}")
