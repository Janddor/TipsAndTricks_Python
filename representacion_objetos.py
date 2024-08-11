# __str__ su objetivo es que la información sea legible para el usuario
# __repr__ su objetivo es que la información no sea ambigua
# se utiliza para hacer debugging (formato  tipo constructor)
# La implementación por default del método str llama a repr

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Por default solo se muestra el nombre de la clase y id del objeto(dirección memoria)
audi_a3 = Auto('Audi', 'A3', 'Rojo')
print(audi_a3)
print()
class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'__str__: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'

    # def __repr__(self):
    #     return f'__repr__: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r},'
                f'{self.modelo!r},'
                f'{self.color!r}'
                f')')

audi_a1 = AutoStr('Audi', 'A1', 'Blanco')
# Tenemos diferentes formas de imprimir el objeto, si no existiera str, se llama repr por default
print(audi_a1)
print(audi_a1.__str__())
print(str(audi_a1))
print('{}'.format(audi_a1))
print(f'{audi_a1}')

# Sin embargo, es más recomendable usar __repr__ en lugar de __str__
# Ej. Cualquier colección utiliza repr en lugar de str para mostrar la información
print([audi_a1])
# También usando !r se llama repr
print(f'{audi_a1!r}')
print()
# También manualmente podemos escoher qué método utilizar
print(str(audi_a1))
print(repr(audi_a1))