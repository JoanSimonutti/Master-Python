nada = None # NoneType - Ausencia de valor - Ejemplo: None

cadena = "Hola soy Joan Simonutti" # str (String) - Cadenas de texto - Ejemplo: "hola", 'mundo'

entero = 99 # int (Integer) - Números enteros (positivos o negativos) - Ejemplo: 6, -16, 101

flotante = 4.2 # float - Números decimales - Ejemplo: 3.14, -4.2

booleano = True # bool (boolean) - Verdadero o Falso - Ejemplo: True, False

lista = [10, 20, 30, 100, 200] # list (Lista) - Lista ordenada, modificable - Ej: [1, 2, 3], ["a", "b", "c"]

listaString = [44, "treinta", 27, "noventa"]

tupla = ("Master", "en", "Python") # tuple (Tupla) - Lista ordenada, no modificable - Ej: (1, 2, 3)

diccionario = {            
    "nombre": "Joan",        # dictionary - Diccionario de pares clave-valor - Ej: {"nombre": "Ana", "edad": 25}
    "apellido": "Simonutti",
    "edad": 37
}

rango = range(9)  # range - Rango de números Ej: range(5)

dato_bytes = b"Prueba" # bytes - Dato bytes, el tipo de dato bytes representa una secuencia inmutable 
                         # de valores de bytes, es decir, números enteros entre 0 y 255. 
                         # Se usa principalmente para trabajar con datos binarios, 
                         # como archivos (.pdf), imágenes (.jpg), conexiones de red, audio, etc. 
                         # NOTA: Qué es un byte en Python? 
                         # Es una unidad de datos que puede representar un valor entre 0 y 255.
                         # Un objeto de tipo bytes es como una lista inmutable de estos valores.


# Imprimir variable
print(diccionario)

# Mostrar tipo de dato
print(type(diccionario))