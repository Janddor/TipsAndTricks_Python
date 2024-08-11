# 2. Nuevo estilo de formato de cadenas en Python _______________
nombre = 'Juan'
# {} placeholders
mi_cadena = 'Hola, {}'.format(nombre)
print(mi_cadena)

# Podemos convertir enteros a hexadecimales
error = 500
cadena_hexadecimales = 'Error en hexa: {error:X}'.format(error=error)
print(cadena_hexadecimales)
# Int to Float
entero = 50
cadena_flotante = 'Numero flotante: {entero:0.2f}' .format(entero=entero)
print(cadena_flotante)

# Podemos hacer lo mismo, pero usando String Interpolation (f-string literal)
mi_cadena = f'Hola, {nombre}'
print(mi_cadena)
# Imprimir directamente sin variable
print(f'Hola, {nombre}')
# Mismo ejemplo hexa con String Interpolation
print(f'Error Hexa: {error:X}')
# Mismo ejemplo de Int to Float
print(f'Numero Flotante: {entero:.2f}')
# Incluir expresiones o llamadas a funciones
a = 10
b = 3
print(f'Result Div and Format in-line: {(a/b):.2f}')