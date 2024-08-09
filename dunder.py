# dunder = Double underscore

class Padre:
    def __init__(self):
        # Al usar dunder no se aplica el concepto de name mangling
        self.__variable_privada = 10
        self.__variable_dunder__ = 15

if __name__ == '__main__':
    padre = Padre()
    print(dir(padre))
    print(f'Accediendo a la variable dunder: {padre.__variable_dunder__}') # No se aplicó name mangling así que se accede normal
    print(f'Accediendo a la variable privada: {padre._Padre__variable_privada}') # Toca así porque si se aplicó name mangling