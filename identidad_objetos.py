# Comparación del uso de operador == o el operador is en POO

# El operador == compara el contenido de dos objetos (contenido igual)
# no necesariamente son el mismo objeto, pueden apuntar a objetos distintos

# Operador is revisa si dos objetos son iguales (objetos son idénticos)
# Ambos deben estar apuntando a la misma dirección de memoria para considerarse iguales

# Ejemplo de una lista
lista_a = [1 ,2 ,3]
lista_b = lista_a

# lista a y b tienen mismo contenido == sería True
# y también apúntan a la misma referencia
print(f'Lista a y b tienen mismo contenido: {lista_a==lista_b}')
print(f'Lista a y b apuntan al mismo objeto: {lista_a is lista_b}\n')

# Sin embargo, si creamos un nuevo objeto
lista_c = list(lista_a)
# La lista c tiene el mismo contenido que a, por lo que == verdadero
# Pero la lista c apunta a un objeto diferente en memoria por lo que IS false
print(f'Lista a y c tienen mismo contenido: {lista_a==lista_c}')
print(f'Lista a y c apuntan al mismo objeto: {lista_a is lista_c}')
