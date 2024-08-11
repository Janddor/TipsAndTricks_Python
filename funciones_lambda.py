# Las funciones lambda nos permiten declarar funciones anónimas en una sola línea de código

# Ejemplo de función normal
def sumar(a, b):
    return a+b
print(f'Sumando con sumar(): {sumar(3, 5)}')

# Función lambda
sumar_lambda = lambda a, b : a + b
print(f'Sumando con lambda: {sumar_lambda(9, 5)}')

# Utilizando en una sola línea de código
print(f'En una sola linea de codigo: {(lambda a, b: a+b)(5,6)}')

# Podemos usar una función lambda siempre que necesitemos una función muy específica
# Ej. Ordenar una lista de tuplas, por us segundo valor proporcionando una llave (key)
lista_tuplas = [(1, 'b'),(5, 'f'),(2, 'h'), (3, 'c'),]
# lista_tuplas_ordenada = sorted(lista_tuplas, key = lambda tupla: tupla[0]) # Ordenar por números
lista_tuplas_ordenada = sorted(lista_tuplas, key = lambda tupla: tupla[1]) # Ordenar por letras
print(lista_tuplas_ordenada)

# Otro ejemplo de ordenamiento utilizando una expresión lambda
print(list(range(-3, 4)))
# Si queremos ordenar por el valor absoluto
for valor in range(-3, 4):
    print(valor, valor*valor)

# Ahora se aplicará a una expresión lambda
lista_ordenada = list(sorted(range(-3, 4), key= lambda valor: valor*valor))
print(lista_ordenada)

# Las funciones lambda también pueden tener el concepto de closure
def mostrar(titulo):
    return lambda mensaje: titulo + ' ' + mensaje
mostrar_lic = mostrar('Licenciado') # Gracias al concepto de closure, se guarda el estado de la función interna
mostrar_ing = mostrar('Ingeniero')
print(mostrar_ing('Jan Nicol Suárez.'))
print(mostrar_lic('Andrés Felipe Herrera.'))

# Ejemplos de casos de funciones lambda que no son recomendables
class Prueba:
    mostrar = lambda self: print('Funcion Mostrar...') # Mala práxis, complejidad innecesaria
    saludar = lambda self: print('Funcion Saludar...') # Mala práxis, complejidad innecesaria

prueba = Prueba()
prueba.mostrar()
prueba.saludar()


# Otro ejemplo donde una función lambda agregaría complejidad innecesaria
lista_pares = list(filter(lambda valor : valor % 2 == 0, range(10)))
print(lista_pares)

# Mismo ejercicio con list comprehensions
lista_pares_modificada = [valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)


