#pedir al usuario que ingrese un texto cualquiera
# ademas que ingrese 3 letras luego de ellos procesar el texto
#hacer 5 tipos de analisis de la cadena
#1. Cuantas veces se repite la letra que eligió el usuario (alamcenar en una lista)
#2. Cuantas palabras tiene el texto (almacenar en una lista)
#3. Cual es la primera letra y la última letra del texto
#4. Invertir el texto
#5. Ver si python esta en el texto

cadena_Texto = input("Ingrese un texto elección: ").lower()
letras = []
letras.append(input("Ingrese la primera letra: ").lower())  #almacena la letra en una lista vacia indice 0
letras.append(input("Ingrese la segunda letra: ").lower())  #almacena la letra en una lista vacia indice 1
letras.append(input("Ingrese la tercera letra: ").lower())  #almacena la letra en una lista vacia indice 2

print("\n")
cantidad1 = cadena_Texto.count(letras[0]) #cuenta la cantidad de veces que se repite la letra elegida
cantidad2 = cadena_Texto.count(letras[1]) #cuenta la cantidad de veces que se repite la letra elegida
cantidad3 = cadena_Texto.count(letras[2]) #cuenta la cantidad de veces que se repite la letra elegida

print(f"Hemoz encontrado la letra '{letras[0]}' repetida {cantidad1} veces")
print(f"Hemoz encontrado la letra '{letras[1]}' repetida {cantidad2} veces")
print(f"Hemoz encontrado la letra '{letras[2]}' repetida {cantidad3} veces")

print("\n")
print("Cantidad de Palabras: ")
palabras = cadena_Texto.split() #separa las palabras por espacio vacio
print(f"La cantidad de palabras en el texto es: {len(palabras)} palabras en tu texto") #imprime la cantidad de palabras
print("\n")

print("Primera y última letra: ")
primera_letra = cadena_Texto[0] #almacena la primera letra
ultima_letra = cadena_Texto[-1] #almacena la ultima letra
print(f"La primera letra es: '{primera_letra}' y la última letra es: '{ultima_letra}'") #imprime la primera y ultima letra

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras) #invierte el texto
print(f"El texto invertido es: '{texto_invertido}'") #imprime el texto invertido

print("\n")
print("VERIFICANDO SI PYTHON ESTA EN EL TEXTO")
busca_python = "python" in cadena_Texto #verifica si python esta en el texto
dic = {True:"Si", False:"No"}
print(f"La palabra 'Python': {dic[busca_python]} se encuentra") #imprime si python esta en el texto
