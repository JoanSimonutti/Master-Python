"""
Una variable es un contenedor de informacion
que dentro guardará un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto.

"Una variable es un espacio en memoria que se utiliza para
almacenar datos que pueden cambiar durante la ejecución del programa."

Para qué sirve?
Las variables permiten al programador guardar, modificar y utilizar datos en distintas partes del código.

Características principales:
Tiene un nombre (por ejemplo, edad, total, nombre).
Contiene un valor (por ejemplo, 25, "Juan", 3.14).
Puede cambiar su valor durante el programa (de ahí el nombre "variable").

"""

# Crear variables y asignarles un valor
texto = "Hola! Soy Joan Simonutti y éste es mi Master en Python"
texto2 = "Guacamole cha cha cha!"
numero = 327
decimal = 6.7

# Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------- barra separadora -------------")

# Reasignar el valor de algunas variables
numero = 1022
decimal = 10.22

print(numero)
print(decimal)

print("------------- barra separadora -------------")

# Concatenación 
# La concatenación de variables es el proceso de unir
# dos o más valores, generalmente cadenas de texto (strings),
# para formar una sola cadena.

# Interpolar significa insertar valores dentro de una cadena de texto,
# reemplazando marcadores con variables o expresiones. 
# Esto se conoce como interpolación de cadenas o "string interpolation"

nombre = "Joan"
apellido = "Simonutti"
web = "joansimonutti.com.ar"

print(nombre + " " + apellido + " - " + web) #Concatenar

print(f"{nombre} {apellido} - {web}") #Interpolar es incrustar variables dentro de un texto 
                                      #de forma clara y legible utilizando f-strings, 
                                      #que es el método más legible, moderno y recomendado desde Python 3.6

print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web)) #Interpolacion con el método .format

print(nombre, apellido, web) #En este caso no seria una concatenación, 
                             #ya que solo le estamos pasando variables sueltas
                             #a la funcion print para que las muestre por consola.