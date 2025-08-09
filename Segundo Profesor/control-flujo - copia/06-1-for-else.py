buscar = 3  # Valor a buscar
for numero in range(5):  # Itera sobre los números del 0 al 4
    print(numero)  # Imprime el número actual
    if numero == buscar:  # Si el número actual es igual al valor a buscar
        print("Encontrado", buscar)  # Imprime el valor encontrado
        break
else:  # Si no se encontró el valor en el bucle
    print("No se encontró el valor", buscar)  # Imprime que no se encontró

for char in "Python":  # Itera sobre cada carácter en la cadena "Python"
    print(char)  # Imprime el carácter actual
