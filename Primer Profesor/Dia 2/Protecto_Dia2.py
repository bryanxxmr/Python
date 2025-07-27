#Se trabaja en una empresa donde los vendedores reciben comisiones de 13% de sus ventas totales
#ayudar a calcular sus comisiones. Crear un programa que pida tu nombre y cuanto has vendido
#este mes. El programa debera responder con un "Ok nombre, este mes ganaste $XXX".

nombre = input("Hola, ¿cuál es tu nombre? ")
ventas = float(input("¿Cuánto has vendido este mes? "))
ventas = int(ventas) #convertir a entero

comision = ventas * 13 / 100 #convertir a porcentaje
comision = round(comision, 2) #redondear a dos decimales

print(f"Hola {nombre}, este mes ganaste ${comision}") #imprimir el resultado