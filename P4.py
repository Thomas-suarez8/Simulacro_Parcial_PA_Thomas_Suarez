#Problema 4. Diseñe un programa que lea una entrada y determine si el dato puede considerarse:
#- un número entero,
#- un número decimal,
#- un valor booleano (true o false),
#- o una cadena de texto general.

dato = input('Ingrese un valor: ')

dato = dato.strip()

if dato.lower() == "true" or dato.lower() == "false":
    print(f'El dato es un valor booleano')

elif dato.isdigit():
    print(f'El dato es un numero entero')

elif dato.replace(".", "", 1).isdigit():
    print(f'El dato es un numero decimal')

else:
    print(f'El dato es una cadena de texto')