# ABC - Abstract Base Class
# No se pueden instanciar
# Permiten asegurar que las clases que heredan implementen los métodos de padres
# ABC permite escribir una jerarquía de clases más robusta y escribir código más mantenible

from abc import ABCMeta, abstractmethod


# Ej- sin usar ABC
class ClaseBase1:
    def metodo_1(self):
        raise NotImplementedError
    def metodo_2(self):
        raise NotImplementedError

class ClaseConcreta1(ClaseBase1):
    # Implementación de la clase padre
    def metodo_1(self):
        print('Metodo 1 implementado...')
    # Método 2 no se va a implementar
    # Es un problema porque no se reporta la falta de implementación

# Hay un problema, se puede instanciar la clase base y no se desea esto.
# clase_base = ClaseBase1()
# clase_base.metodo_1()

# Esto funciona según lo esperado
clase_concreta = ClaseConcreta1()
# clase_concreta.metodo_1()
# El método2, se llama el método heredado
# clase_concreta.metodo_2() # Manda error si no fue implementado en ClaseConcreta1

# Resolviendo los detalles anteriores usando ABC (Abstract Base Class)
class ClaseBase2(metaclass=ABCMeta):
    # No tenemos que agregar la implementación al ser un método abstracto, no tiene init
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass

class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Método 1 implementado...')

    # Si se deja sin implementar metodo_2 no dejará crear objetos de esta clase
    def metodo_2(self):
        print('Método 2 implementado...')

# clase_base = ClaseBase2()

# Instanciar clase concreta 2
clase_concreta = ClaseConcreta2()
clase_concreta.metodo_1()
clase_concreta.metodo_2()

