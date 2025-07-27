import math

print(round(1.3))  # round lo que hace es redondear un número al entero más cercano
print(round(1.7))  # round lo que hace es redondear un número al entero más cercano
print(round(1.5))  # round lo que hace es redondear un número al entero más cercano
# abs devuelve el valor absoluto de un número, # es decir, su valor sin signo
print(abs(-10))
# abs devuelve el valor absoluto de un número, # es decir, su valor sin signo
print(abs(10))

# ahora se importara un modulo llamado math en la parte superior
print(math.ceil(1.3))  # ceil redondea hacia arriba al entero más cercano
print(math.floor(1.999))  # floor redondea hacia abajo al entero más cercano
# isNaN verifica si el valor es NaN (Not a Number), si ingresamos texto nos devolvera True
print(math.isnan(1.0))
# isNaN verifica si el valor es NaN (Not a Number)
print(math.isnan(float('NaN')))
print(math.sqrt(16))  # sqrt calcula la raíz cuadrada de un número
print(math.pow(2, 3))  # pow calcula la potencia de un número
