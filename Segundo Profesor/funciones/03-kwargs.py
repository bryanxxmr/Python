def funcion_kwargs(**varios_Datos):
    # imprime nombre y apellido de la persona
    print(varios_Datos["nombre"], varios_Datos["apellido"])


funcion_kwargs(dni=46706865, nombre="Kenny", apellido="Mendo", edad=35)
