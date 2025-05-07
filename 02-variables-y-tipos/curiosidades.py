# Curiosidades
# En Python (y en muchos otros lenguajes), la barra invertida \ se llama:
# "carácter de escape" (escape character) y su función principal es que
# permite escapar caracteres especiales o introducir caracteres no imprimibles dentro de cadenas (str) 
# Ejemplo: 
# texto = "Ella dijo: \"Hola\""
# print(texto)  # Ella dijo: "Hola"

mi_texto = '"Master"' # En Python, también podés alternar entre comillas simples (') y dobles (") 
                      # para evitar el uso del carácter de escape \
                      # Esto es una forma práctica y legible de escribir strings que contienen comillas.

mi_texto2 = "en \"Python\"" # Otro ejemplo de escapar de la funcionalidad 
                            # nativa que llevan las comillas dentro de un string usando \

texto_unido = mi_texto + " " + mi_texto2

print(texto_unido)

print("------------- barra separadora -------------")

# \n Pega un salto de linea
texto_unido = mi_texto + " \n " + mi_texto2

print(texto_unido)

print("------------- barra separadora -------------")

# \t Mete una tabulación (tab)
texto_unido = mi_texto + " \t " + mi_texto2 
print(texto_unido)

print("------------- barra separadora -------------")

# \r Borra todo lo que este por detras
texto_unido = mi_texto + " \r " + mi_texto2 
print(texto_unido)