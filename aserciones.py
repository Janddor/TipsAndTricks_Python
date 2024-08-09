# Tip. Aserciones ayudan a depurar programas de errores que no nos podemos recuperar

# Ejemplo 1. Revisar si la división es entre 0
def dividir(a, b):
    # Nos aseguramos que el valor de b no es 0 para poder continuar
    assert b != 0, 'División entre cero'
    print(f'Resultado división: {a/b}')

# Ejemplo 2. Realizar el cálculo del promedio de una lista de calificaciones
def obtener_promedio(calificaciones):
    # Si la lista de calificaciones está vacía, no debería continuar el programa
    assert len(calificaciones) !=0, 'Lista de calificaciones vacía'
    print(f'El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}')

# Ejmplo 3. realizar un descuento a un produto proporcionado
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0-descuento)
    print(f'Nuevo precio del producto: {precio_con_descuento}')
    assert 0<=precio_con_descuento<=productos['precio'], f'Descuento Invalido {precio_con_descuento}'
    print('Descuento válido...')

if __name__ == '__main__':
    # Prueba ejemplo 1
    # dividir(10, 0)
    dividir(10, 1)
    # Prueba ejemplo 2
    calificaciones= []
    calificaciones= [10, 8, 7, 9]
    obtener_promedio(calificaciones)
    # Prueba ejemplo 3
    productos = {'nombre':'Camisa', 'precio':1500}
    # aplicar_descuento(productos, 1.1)
    aplicar_descuento(productos, 0.1)