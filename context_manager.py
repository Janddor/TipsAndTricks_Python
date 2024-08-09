from contextlib import contextmanager

with open('prueba.txt', 'w') as archivo:

    archivo.write('Hola desde python')

# # Esto es equivalente a:
# archivo = open('prueba.txt', 'w')
# try:
#     archivo.write('Hola desde Python')
# finally:
#     archivo.close()
#

# # Esto NO es equivalente
# archivo = open('prueba.txt', 'w')
# archivo.write('Hola sin with')
# # Esto no asegura el cierre de recursos en caso de error
# archivo.close()

# Manejo de Contect Manager en Clases
# 1. Implementando el protocolo con las funciones (__enter__) y (__exit__)
# 2. Utilizando la librería de contextlib

# Veamos la opcion 1
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.archivo = open(self.nombre, 'w')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()


# Este método es un generador. 1ero adquiere el recurso y luego suspende la ejecución al utilizar yield
# Cuando termina de ser utilizado el método, regresa a la ejecución y cierra el recurso
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w')
        yield archivo
    finally:
        archivo.close()

# Ejercicio de Identador
class Identador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1

    def imprimir(self, texto):
        print(' '*self.nivel + texto)

# Mismo ejercicio de identador con contextlib
class Identador2():
    def __init__(self):
        self.nivel = 0
    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1
    def imprimir(self, texto):
        print(' '*self.nivel + texto)


if __name__ == '__main__':
    # Prueba implementando el protocolo de Context Manager
    with ManejoArchivos('prueba.txt') as archivo:
        archivo.write('Prueba desde ManejoArchivo()')

    # Prueba con librería contextlib
    with manejador_archivos('prueba.txt') as archivo:
        archivo.write('prueba desde decorador')
        archivo.write('\nadios')

    # Prueba de Identador
    with Identador() as identador:
        identador.imprimir(f'Primer Nivel')
        with identador:
            identador.imprimir('Segundo Nivel')
            identador.imprimir('Sigue siendo segundo nivel')
            with identador:
                identador.imprimir('Tercer Nivel')
                identador.imprimir('Sigue siendo tercer nivel')
        identador.imprimir('Fin primer nivel')

    # Prueba identador2
    print('________________')
    objeto = Identador2()
    with objeto.identador():
        objeto.imprimir('primer nivel')
        objeto.imprimir(f'Más del nivel: {objeto.nivel}')
        with objeto.identador():
            objeto.imprimir('segundo nivel')
            objeto.imprimir(f'Más del nivel: {objeto.nivel}')
            with objeto.identador():
                objeto.imprimir('segundo nivel')
                objeto.imprimir(f'Más del nivel: {objeto.nivel}')