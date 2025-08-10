# al segundo parámetro se le asigna un valor por defecto de "Sin apellido"
def funcion_parametroOpcional(nombre, apellido="Sin apellido"):
    print("Bienvenido a Python")
    print(f"Nombre: {nombre}  Apellido: {apellido}")


funcion_parametroOpcional("Juan", "Pérez")
# imprime "Sin apellido" porque no se le pasó un segundo argumento
funcion_parametroOpcional("Ana")
