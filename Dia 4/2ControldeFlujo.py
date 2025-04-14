# Control de flujo if
#if 10 > 15:
#print("Es correcto")
#else:
#print("Es incorrecto")

# Control de flujo if-else
mascota = 'Gato'

if mascota == 'Loro':
    print("Es un loro")
elif mascota == 'Gato':
    print("Es un " + mascota)
else:
    print("No se que animal es")

#validar la edad de una persona si es mayor de edad y su calificacion
edad = 16
calificacion = 9

if edad < 18:
    print("Es mayor de edad")
    if calificacion >= 7:
        print("Aprobo")
    else:
        print("No aprobo")
else:
    print("Es un adulto")


#Practica 1
#Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):
#Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
#"num1 es mayor que num2"
#"num2 es mayor que num1"
#"num1 y num2 son iguales"
#Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.
#Aclaración:
#1. No deben imprimirse strings adicionales a la respuesta del usuario.
#2. Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas".
# Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#Practica 2
#Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo,
# y para optar por una licencia para conducir, debe de tener 18 años o más.
#Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir,
# y muestra el resultado que corresponda en pantalla:
#"Puedes conducir"
#"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
#"No puedes conducir. Necesitas contar con una licencia"
#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.
edad = 16
licencia = False
if edad >= 18 and licencia:
    print("Puedes conducir")
elif edad >= 18 and not licencia:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")