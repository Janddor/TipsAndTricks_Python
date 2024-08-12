# Copia de atributos de objetos
import copy


# Definimos una clase de tipo Punto 2D
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto({self.x!r}, {self.y!r})'

    def __eq__(self, other):
        return isinstance(other, Punto) and self.x == other.x and self.y == self.y

punto_a = Punto(2, 3)
punto_b = copy.copy(punto_a)
# Copia poco profunda (shadow), son distintos objetos
print(f'Copia poco profunda (shadow)')
print(f'Punto a: {punto_a}')
print(f'Punto b: {punto_b}')
print(f'Son objetos con mismo contenido?  -> {punto_a == punto_b}') # True con el método eq
print(f'Son los mismo objetos (misma ref)?-> {punto_a is punto_b}')

# Clase rectángulo utiliza dos puntos (sup izq, inf der)
class Rectangulo:
    def __init__(self, sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der
    def __repr__(self):
        return f'Rectangulo({self.sup_izq!r}, {self.inf_der!r})'

rect_a = Rectangulo(Punto(0,1), Punto(3,4))
# Copia superficial (shadow)
rect_b = copy.copy(rect_a)
# Copia poco profunda (shadow), son distintos objetos
print(f'Copia superficial rectangulos')
print(f'Rectángulo a: {rect_a}')
print(f'Rectángulo b: {rect_b}')
# Debido a que la copia fue superficial, un cambio en un punto afectará al otro rectángulo
rect_a.inf_der.y = 6
print(f'Cambio en un punto afecta al otro rectángulo por ser copia superficial')
print(f'Rectángulo a: {rect_a}')
print(f'Rectángulo b: {rect_b}')
print()

# Creación copia profunda (deep copy)
rect_c = copy.deepcopy(rect_a)
print(f'Copia profunda de a en rect c, un cambio en c no afectará rect a')
rect_c.sup_izq.x = 2
rect_a.sup_izq.x = 3
print(f'Rectángulo a: {rect_a}')
print(f'Rectángulo c: {rect_c}')