# Crear una clase para definir una clase de excepcion personalizada
# Ej. Validar que un nombre no pueda tener menos de 3 caracteres

# Este tipo de validación no indica cuál es el problema en específico
def validar(nombre_completo):
    if len(nombre_completo) < 3:
        raise ValueError
    else:
        print('Validación correcta...')

nombre = 'Juan'
# validar(nombre)

# # Validación personalizada, indica cuál es el problema, y queda autodocumentado
# class NombreDemasiadoCorto(ValueError):
#     pass
#
# def validar_mejorado(nombre_completo):
#     if len(nombre_completo) < 3:
#         raise NombreDemasiadoCorto(nombre_completo)
#     else:
#         print('Validación mejorada correcta')
#
# nombre = 'Ju'
# validar_mejorado(nombre)

# Es buena idea crear una clase base y de allí extender las demás clases
class ClaseExcepcionBase(TypeError):
    pass

class NombreDemasiadoCorto(ClaseExcepcionBase):
    pass

def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('Validación mejorada correcta')

nombre = 'Ju'
try:
    validar_mejorado(nombre)
except ClaseExcepcionBase as e:
    print(f'{type(e).__name__}, línea {e.__traceback__.tb_lineno} en {__file__}: {e}')

