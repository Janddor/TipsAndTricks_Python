# El guion bajo simple se usa por convensión (buena praxis)
# Para indicar que es variable temporal o sin importancia

for _ in range(3):
    print('Hola...')

# También se usa para tuplas
valores = ('Juan', 'Perez', 31)
nombre, _, edad = valores # Unpacking indicando que el apellido no importa o no se usará
print(f'Nombre: {nombre}, Edad: {edad}')

# Se puede usar como variable temporal de cualquier tipo
_ = list()
_.append(1)
_.append(2)
_.append(3)
print(f'Variable temporal que apunta a una lista: {_}')