# Los decoradores permiten extender y modificar el comportamiento de las funciones métodos, y clases
# Ejemplos comunes: logging, seguridad, caching

# Un decorador es código reutilizable
# Primer ejemplo de un decorador
def decorador_envolvente(funcion_a_decorar):
    # Recibir la función y regresarla
    print(f'Estamos dentro de la función {decorador_envolvente.__name__},'
          f' decorando a: {funcion_a_decorar.__name__}')
    return funcion_a_decorar


# Utilizando el decorador
def saludar():
    return 'Saludos desde mi función...'


# Llamada sencilla del decorador (no común)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)
print()


@decorador_envolvente
def saludar_funcion_a_decorar():
    return 'Saludos desde función a decorar...'


print(saludar_funcion_a_decorar())
print()


# Decorador que convierte el texto a mayúsculas
def mayusculas(funcion_a_decorar):
    def envolvente():
        # Mandamos a llamar la función original (closure)
        print('Antes de llamada a la función a decorar')
        resultado_original = funcion_a_decorar()
        print('Después de llamada a la función a decorar')
        resultado_modificado = resultado_original.upper()
        return resultado_modificado

    return envolvente


@mayusculas
def saludar_minusculas():
    return f'Hola Buenas Tardes...'


print(saludar_minusculas())


# ____________________________________________________________________
# Decoradores Múltiples
# <strong><em>Hola</em></strong>
def negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'

    return funcion_envolvente


def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'

    return funcion_envolvente


@negritas  # Luego este
@enfatizar  # Se ejecuta primero este, (from bottom) o desde abajo.
def saludar_html():
    return 'Hola con HTML'


print(saludar_html())
print()
# ____________________________________________________________________

# Decoradores con argumentos
# *args y *kwargs


def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('Se está ejecutando el decorador...')
        print(f'con args:{args}, kwargs:{kwargs}')
        # Propagrando los parámetros a la función original
        return funcion(*args, **kwargs)
    return funcion_envolvente
@decorador_con_argumentos
def funcion_saludar(titulo, nombre):
    # imprimir el título con el nombre
    print(f'{titulo}. {nombre}')

funcion_saludar('Ingeniera', 'María Quiroz')
















