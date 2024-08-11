import copy
#----------------------------------------------------------------------------------------------------------------------
# Clonación (copia) de objetos
# Copia superficial (shadow) o copia poco profunda
lista_a = [[1,2],
           [3,4],
           [5,6],
           ]
# Copia superficial (shadow)
lista_b = list(lista_a)
# Las listas a y b son objetos distintos, apuntan a diferente memoria, pero los niveles
# más internos solo se copió la referencia, no se crearon nuevos elementos para las sublistas.
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
# Comprobación de que los objetos son distintos
# Un cambio en el nivel superior de la lista a, ver que no afecta a lista b
lista_a.append([7,8])
print(f'Son distintos objetos(nivel superior)')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
# Comprobación de que objetos internos si tienen la misma referencia (copia superficial)
# Un cambio en un elemento de una sublista, afecta a la sublista de la otra lista
lista_a[0][1]='A'
print(f'La copia fue superficial, de los elementos internos solo se copió la referencia')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
print()

#----------------------------------------------------------------------------------------------------------------------
# Crear copias profundas (import copy) esto utiliza más tiempo de procesamiento, y solo debe usarse
# cuando sea estríctamente necesario.
lista_c =[[1,2],
           [3,4],
           [5,6],
           ]
lista_d = copy.deepcopy(lista_c)
# Comprobación de que son objetos distintos
lista_c.append([7,8])
print(f'Son distintos objetos (nivel superior)')
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
print(f'La copia fue profunda, las sublistas son nuevos objetos también')
lista_c[0][1]='A'
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
#----------------------------------------------------------------------------------------------------------------------

