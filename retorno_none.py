# De manera explícita se regresa el valor de None
def funcion1(valor):
    if valor:
        return valor
    else:
        return None

print(funcion1(False))

# De manera implícita se regresa el valor de None
def funcion2(valor):
    if valor:
        return valor

print(funcion2(False))

def funcion3(valor):
    print(valor)
    # Enviará como return None, ya que no se le mandó a retornar nada

print(funcion3(10))