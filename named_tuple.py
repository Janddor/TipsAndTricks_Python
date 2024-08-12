# NamedTuples son una extensión del tipo tupla
# Una buena alternativa para escribir clases (atributos tipos inmutables)
# Asignar un identificador a cada elemento de la tupla
from collections import namedtuple
# Definimos una clase con atributos inmutables pero usando namedtuple
Persona1 = namedtuple('Persona1', 'nombre apellido edad')
# Crear una instancia de la clase (se agrega un constructor por default con los atributos)
persona1 = Persona1('Juan', 'Perez', 28)
# En automático se crea un método __repr__ con los atributos proporcionados
print(persona1)

# Crear nuestra clase con los atributos usando una lista
Persona2 = namedtuple('Persona2', ['nombre', 'apellido', 'edad']) # Funciona igual al de Persona1
persona2 = Persona2('Karla', 'Gomez', 30)
print(persona2)

# Podemos acceder a los atributos de manera individual por nombre
print(f'Nombre: {persona2.nombre}')
print(f'Apellido: {persona2.apellido}')
print(f'Edad: {persona2.edad}')
# Acceder a los atributos por índice
print(f'Nombre: {persona2[0]}')
print(f'Apellido: {persona2[1]}')
print(f'Edad: {persona2[2]}')
# Convertir los valores a una tupla
print(tuple(persona2))
# Podemos hacer unpacking de los elementos se la tupla
nombre, apellido, edad = persona2
print(f'Valores tupla persona: {nombre}, {apellido}, {edad}')
# Podemos hacer unpacking pasando como argumento
print(*persona2)
# Las tuplas son inmutables
# persona2.edad = 32 # Error

# Subclases de namedtuples
class Persona3(Persona2):
    # Agregamos un nuevo método a la clase hija
    def convertir_mayusculas(self):
        return f'Nombre Completo: {self.nombre.upper()} {self.apellido.upper()}'

persona3 = Persona3('María', 'Lara', 35)
print(persona3)
print(persona3.convertir_mayusculas())

# Existe otra forma de hacer extends de la clase ( una mejor forma con namedtuple)
print(Persona2._fields)
Persona4 = namedtuple('Persona 4', Persona2._fields + ('email',))
# Crear objeto de la clase Persona4
persona4 = Persona4('Armando', 'Quintero', 38, 'aquintero@gmail.com')
print(persona4)
