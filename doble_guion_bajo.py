# Con doble guin bajo, es convensión pero también lo entiende python como privado
# tanto a atributos o métodos

class Padre():
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2 # Pura convensión
        self.__variable_privada = 3  # privada de verdad

    def get_variable_privada(self):
        return self.__variable_privada

    def __metodo_privado(self):
        print('Accediendo metodo privado desde padre...')

class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'Sobreescrita 1'
        self._variable_protegida = 'Sobreescrita 2'
        self.__variable_privada = 'Sobreescrita 3'

    def __metodo_privado(self):
        print('Accediendo metodo privado desde hijo...')

# Prueba usando una variable global
_Prueba__variable_global = 10

class Prueba:
    def obtenerVar(self):
        return __variable_global

if __name__ == '__main__':
    # Imprimir todos los atributos de la clase
    padre = Padre()
    print(dir(padre))
    '''
    ['_Padre__variable_privada' # name mangling
    , '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
    '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
    '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_variable_protegida', 'variable_publica']
    '''

    # Acceder a los atributos de la clase
    print(f'Variable pública: {padre.variable_publica}')
    print(f'Variable protegida: {padre._variable_protegida}')
    # print(f'Variable privada manda error: {padre.__variable_privada}')
    print(f'Variable privada usando name mangling: {padre._Padre__variable_privada}')

    # Name mangling es transparente para el programador
    print(f'Variable privada por medio de get: {padre.get_variable_privada()}')

    # Prueba clase hijo
    hijo = Hijo()
    print(f'Acceso publico desde hijo: {hijo.variable_publica}')
    print(f'Acceso protegido desde hijo: {hijo._variable_protegida}')
    # print(f'Acceso privado desde hijo: {hijo.__variable_privada}')
    # Namemangling desde lña clase hijo
    print(f'Variable privada desde hijo usando name mangling: {hijo._Hijo__variable_privada}')
    print(f'Acceso privada desde hijo a la clase padre: {hijo._Padre__variable_privada}')

    # También se puede usar métodos con doble guión bajo
    # hijo.__metodo_privado()
    padre._Padre__metodo_privado()
    hijo._Hijo__metodo_privado()
    hijo._Padre__metodo_privado()

    # Accediendo a la variable global
    print(f'Accediendo var global: {_Prueba__variable_global}')
    # Usando name manglign y la clase para acceder a la variable global
    prueba = Prueba()
    print(f'Accediendo variable global desde una clase: {prueba.obtenerVar()}')