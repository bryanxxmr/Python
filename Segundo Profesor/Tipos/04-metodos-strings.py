animal = " chanChitO feliz "  # cadena de texto
print(animal.upper())  # convierte a mayúsculas, upper es un método de cadena
print(animal.lower())  # convierte a minúsculas, lower es un método de cadena

# capitaliza la primera letra, capitalize es un método de cadena
# convierte la primera letra a mayúscula y el resto a minúsculas
print(animal.capitalize())

# title capitaliza la primera letra de cada palabra, title es un método de cadena
print(animal.title())  # convierte a título
print(animal.strip())  # elimina espacios al inicio y al final

# elimina espacios y capitaliza la primera letra
print(animal.strip().capitalize())

print(animal.rstrip())  # elimina espacios al final
print(animal.lstrip())  # elimina espacios al inicio
# encuentra la posición de "ch", find es un método de cadena
print(animal.find("ch"))

# sino encuentra la subcadena, find devuelve -1
print(animal.find("noexiste"))  # -1
print(animal.replace("feliz", "triste"))  # reemplaza "feliz" por "triste"
# verifica si "cha" está en la cadena, devuelve True o False
print("ch" in animal)
# verifica si "noexiste" está en la cadena, devuelve True o False
print("noexiste" in animal)  # False
