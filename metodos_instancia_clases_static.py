# Métodos de instancia, clase y static. con sus diferencias
class MiClase:
    def metodo_instancia(self):
        # Retornar tupla de valores
        return 'Método de instancia ejecutado.', self

    @classmethod
    def metodo_clase(cls):
        # Retornar una tupla de valores
        return 'Método de clase ejecutado.', cls

    @staticmethod # Métodos de utilería, no acceden al estado de la clase ni de las instancias.
    def metodo_estatico():
        return 'Metodo estático ejecutado.'
print()

objeto = MiClase()
# Caso 1. Ejecutando el método de instancia de manera explícita
print(objeto.metodo_instancia())
# Caso 2. Ejecutando el método de instancia de manera explícita
print(MiClase.metodo_instancia(objeto))
# Caso 3. Ejecutando el método de instancia desde la clase
print(MiClase.metodo_instancia(MiClase),'\n')

# Caso 4. Ejecutando el método de clase de manera implícita
print(MiClase.metodo_clase())
# Caso 5. Ejecutando el método de clase desde las instancias
print(objeto.metodo_clase(), '\n')

# Caso 6. Ejecutando el método estático desde clase
print(MiClase.metodo_estatico())
# Caso 7. Ejecutando el método estático desde instancia
print(objeto.metodo_estatico())
