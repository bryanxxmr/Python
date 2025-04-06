x = 10
y = 5

#print("la suma de los numeros {} y {} es {}".format(x, y, x+y))

#otra forma de hacerlo
color = "rojo"
placa = 852262
print(f"El color del auto es {color} y la placa es {placa}")

#Ejercicio 1
#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
#Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado,numero_asociado))

#Ejercicio 2
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
puntos_nuevos = 350
puntos_totales = 1225
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_totales))

#Ejercicio 3
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
#En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores + puntos_nuevos
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos, puntos_totales))

