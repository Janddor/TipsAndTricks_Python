# Distintas formas de dar formato a cadenas en Python
# 1. Estilo Antiguo ________________________
nombre = 'Juan'
mi_cadena = 'Hola, %s' % nombre
print(mi_cadena)

# Convertir enteros a hexadecimales
error = 500
cadena_hex = 'Error en hexadecimal: %X' % error
print(cadena_hex)

# Si se requieren pasar valior valores toca usar una tupla
cadena = 'Hola %s hay un error: %X' % (nombre, error)
print(cadena)

# Podemos referenciar por sustitución de variables usando un diccionario
cadena = 'Hola %(nombre)s hay un error: %(error)X, %(nombre)s' % {'nombre':nombre,'error':error}
# Lo bueno es que se pueden reutilizar las variables varias veces en la misma expresión
print(cadena)