# Diccionarios - dicts
# maps, hashmaps, lookup tables, etc. en otros lenguajes de programación (llave-valor) llave única
# Ejemplo clásico: directorio (llave=nombre, valor=teléfono)
import collections

directorio = {
    'Juan': 34982984,
    'Alicia': 134982984,
    'Carlos': 34982984
}
# Imprimir el diccionario
print(directorio)

# Recuperar un elemento
print(directorio['Juan'])

# Arroja unn error KeyError al no encontrar una llave
# print(directorio['juan'])

# Podemos utilizar una expresión para crear un diccionario
valores_al_cuadrado = {x : x * x for x in range(5)}
print(valores_al_cuadrado)
# print(type(valores_al_cuadrado)) # dict


# Los tipos mutables no pueden ser llaves de un diccionario
# lista = [1,2,3]
# diccionario_erroneo = {lista:'A'} # una lista es mutable, no se puede como llave.
# print(diccionario_erroneo)

# Los tipos inmutables sí pueden ser llaves de un diccionario
tupla = (1,2,3)
diccionario_correcto = {tupla:'A'}
print(diccionario_correcto)

print()
# Si queremos garantizar un orden de inserción, OrderedDict
from collections import OrderedDict # Esto debería estar al inicio por buena práxis

diccionario_ordenado = OrderedDict(uno = 1, dos = 2, tres = 3)
print(diccionario_ordenado)
# Agregar un nuevo elemento
diccionario_ordenado['cuatro'] = 4
print(diccionario_ordenado)
# Obtenemos las llaves
print(f'Llaves diccionario ordenado:\n{diccionario_ordenado.keys()}')
# Si cambiamos algún valor de alguna llave
diccionario_ordenado['uno'] = -1
print(diccionario_ordenado)
# Eliminamos una llave
diccionario_ordenado.pop('tres')
print(diccionario_ordenado)
# volver a insertar un elemento
diccionario_ordenado['tres'] = 3
print(diccionario_ordenado)

# defaultdict es una subclase de dict
from collections import defaultdict
diccionario_default = defaultdict(lambda : 'Valor Erróneo')# Cuando una llave no se pueda encontrar, mandará este valor
diccionario_default['a'] = 1
diccionario_default['b'] = 2
print(diccionario_default['c']) # Enviará: Valor Erróneo

# Podemos crear valores por default como una lista
diccionario_default_lista = defaultdict(list)
# Si accedemos a una llave no existente, la crea y los valores se asignan como una lista
diccionario_default_lista['nombres'].append('Juan')
diccionario_default_lista['nombres'].append('Karla')
diccionario_default_lista['nombres'].append('Laura')
print(diccionario_default_lista)
print(diccionario_default_lista.items())
print(diccionario_default_lista.keys())
print(diccionario_default_lista.values())


# Buscar en múltiples diccionarios como si fuera un diccionario único
from collections import ChainMap

diccionario1 = {'uno':1, 'dos':2, 'tres':3, 'cinco':'A'}
diccionario2 = {'cuatro':4, 'cinco':5}
# Combinación de diccionarios
combinacion_diccionarios = ChainMap(diccionario1, diccionario2)
print(combinacion_diccionarios)
# Buscamos en todos los diccionarios ( de izq a derecha en caso de haber una llave duplicada)
print(combinacion_diccionarios['cinco'])
# Una llave no existente arroja un KeyError
# print(combinacion_diccionarios['seis'])

print()
# Obtención de diccionarios de solo lectura (read only)
from types import MappingProxyType
diccionario_modificable = {'uno':1, 'dos':2, 'tres':3}
diccionario_solo_lectura = MappingProxyType(diccionario_modificable)
# Leemos el valor del diccionario
print(diccionario_solo_lectura)
print(diccionario_solo_lectura['uno'])
# Arroja error si queremos modificar un valor
# diccionario_solo_lectura['uno'] = -1
# Si modificamos el diccionario mutable, afectará al de solo lectura
diccionario_modificable['dos'] = 22
# ver los cambios
print(diccionario_modificable)
print(diccionario_solo_lectura)