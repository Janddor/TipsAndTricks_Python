# Las funciones en python son ciudadanos de primera clase
# First Citizen Class

def mayusculas(texto):
    return texto.upper()


# Normal use of function
# In Python u cannot use function before define it.
print(mayusculas('hola'))

# Use of a function as an Object
# set the reference of a function to a var, without parenthesis

var_function = mayusculas  # Now you can call var_function(args)
print(f'mayusculas  : {mayusculas}')  # the dir is the same in memory
print(f'var_function: {var_function}')  # the dir is the same in memory

# Use of var_function
print(f'Result: {var_function("text")}')

# Demonstrating that functions are really objects deleting original
# del mayusculas
print(f'var_function: {var_function}')  # the dir is the same in memory
print(f'Result: {var_function("new text")}')
# print(f'Result: {mayusculas("new text")}') # Shows an error if mayusculas was deleted

# We can know the default name of a function
print(f'Name by default of function: {var_function.__name__}')
''' # Output:
Name by default of function: mayusculas
'''

# Saving a function in a data structure type (list)
function_list = [mayusculas, var_function, str.upper]
print(function_list)

for function in function_list:
    print(function, function('Greetings since function.'))

# Or we can use directly a function in the list
text_normal = 'Calling directly a function from list'
print(function_list[0](text_normal))
print(function_list[1](text_normal))
print(function_list[2](text_normal))

###____________##########
# We can pass functions as arguments to other functions
# higher-order functions
def greetings(function_arg):
    # Using the function as arg and return the reference of this function
    function_reference_returned = function_arg('Hi, Greetins since High Order Function')
    print(function_reference_returned)

# Calling the function greetings, passing a function as arg
greetings(mayusculas)

# We can pass a nuevo implementation of function that we passed as argument
def minusculas(text):
    return text.lower()

greetings(minusculas)

# Classic example of higher order functions is the map function
# it takes a function as reference and an iterable
# Calls the function with each iterable element
print(list(map(mayusculas,['TeXt1','TExt2','TexT3',])))
print(list(map(minusculas,['TeXt1','TExt2','TexT3',])))


# nested functions
def show_(text):
    # Definition of internal function or nested
    def convert_lower(t):
        return t.lower()
    # Once defined we can call the internal function
    # return convert_lower(text)
    return convert_lower(text)

# Each time that we call show_ function, it creates the convert_lower function
print(show_('TEXT from nested function'))

# We cannot use the internal function from outside the show_ function
# convert_lower('Probe text') # Error
# print(show_.convert_lower('Probe text')) # Error

# If we return the nested function (the reference) we can use it from outside
def speak(volume):
    def speak_lower(text):
        return text.lower()
    def speak_upper(text):
        return text.upper()
    if volume > 0.5:
        return speak_upper
    else:
        return speak_lower

# Using the nested function
print(speak(0.6)('Speaking with high Volume'))
print(speak(0.2)('Speaking with low Volume'))

var_lower = speak(0.4)
print(var_lower('Other text with low volume'))

###########################
# Closures
# The inner function can get and save the state of the outside function
def speak(text, volume):
    # Now the inner function is not receiving args
    # bc use the states of parent function (external)
    def minusculas():
        return text.lower() # Accessing to text var
    def mayusculas():
        return text.upper()
    if volume > 0.5:
        return mayusculas()
    else:
        return minusculas()
# Now calling speak function but with 2 args
print(speak('Speaking high volume...', 0.9))
print(speak('Speaking low volume...', 0.1))

# Other closure example
# we can pre-configure a function
def mostrar(title):
    # we define nested function
    def saludar(message):
        return title + '. ' + message
    return saludar
mostrar_ing = mostrar('Ingeniero') # Saving the state of the inner function
mostrar_lic = mostrar('Licenciado') # Saving the state of the inner function
# The title is now out of the scope
print(mostrar_lic('Alvaro Ruiz'))# Only sending the message, bc the title was saved in the preconfigured function
print(mostrar_ing('Jan Suarez'))

###########################
# with the function "callable" we can know if an object is a function or if it is callable
print(f'We can call the object mostrar as function?: {callable(mostrar)}')
print(f'We can call the object mostrar_lic as function?: {callable(mostrar_lic)}')
print(f'We can call the object text_normal as function?: {callable(text_normal)}')

# If we want a class that can define objects callables
# we need to rewrite the __call__ method
class Mostrar:
    def __init__(self, title):
        self.title = title

    def __call__(self, message):
        return self.title + '. ' + message

mostrar_doctor = Mostrar('Doctor')
print(mostrar_doctor('Carlos Ugalde'))
print(f'We can call the object mostrar_doctor as function?: {callable(mostrar_doctor)}')
