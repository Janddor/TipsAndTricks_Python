# Diferencia entre variables de clase y de instancia (objeto)
class Perro:
    no_patas = 4 # <- Variable de clase

    def __init__(self, nombre):
        self.nombre = nombre # <- Variable de instancia (del objeto)

# Definimos algunos objetos
layla = Perro('Layla')
venus = Perro('Venus')
print(layla.nombre, venus.nombre)

# La variable de clase se puede acceder con el nombre de la clase, o con los objetos
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Si tratamos de acceder la variable de instancia desde la clase no es posible
# print(Perro.nombre)

# Si queremos modificar el no_patas para todos los perros (variable de clase)
Perro.no_patas = 5
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Si queremos modificar el no_patas para un solo perro
venus.no_patas = 6 # Se crea una variable de instancia y se oculta la variable de clase
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Imprimir el valor de la variable de instancia y además la variable de clase
print(venus.no_patas, venus.__class__.no_patas)

# Si creamos una variable desde la clase
Perro.nombre = 'Clase Perro'
print(layla.nombre, venus.nombre, Perro.nombre)

# Si definimos una variable de clase que no está en los objetos
Perro.no_orejas = 2 # Si no se crea algo en el objeto sobre orejas, al llamarlo desde un objeto
# se llamará la variable de clase creada.
print(layla.no_orejas, venus.no_orejas, Perro.no_orejas)

# Implementación Errónea - contador de objetos de una clase
class ContadorObjetosErronea:
    no_instancias = 0
    def __init__(self):
        # Acá está el error
        self.no_instancias += 1

print(f'Contador de instancias Erróneo:')
print(ContadorObjetosErronea.no_instancias)
print(ContadorObjetosErronea().no_instancias)
print(ContadorObjetosErronea().no_instancias)
print(ContadorObjetosErronea.no_instancias)

# Implementación corregida
class ContadorObjetos:
    no_instancias = 0
    def __init__(self):
            self.__class__.no_instancias += 1
            # ContadorObjetos.no_instancias += 1

print('Contador Instancias:')
print(ContadorObjetos.no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)
