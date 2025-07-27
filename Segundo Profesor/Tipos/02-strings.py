nombre_curso = "Ultimate Pyhton"
descrpcion_curso = """
Curso de Python desde cero hasta experto.
Incluye temas avanzados como programación orientada a objetos, manejo de excepciones y más.
Mas de 100 horas de contenido.
Además, incluye ejercicios prácticos y proyectos reales."""
print(nombre_curso, ":", descrpcion_curso)
# len es una función que devuelve la longitud de un objeto en particular.
print(len(nombre_curso))  # el tamaño de la cadena es 15
print(nombre_curso[0])  # el primer carácter es 'U'
print(nombre_curso[0:6])  # los primeros 6 caracteres son 'Ultima'
print(nombre_curso[9:])  # desde el carácter 9 hasta el final es 'Python'
print(nombre_curso[:6])  # los primeros 6 caracteres son 'Ultima'
print(nombre_curso[:])  # toda la cadena es 'Ultimate Pyhton'
