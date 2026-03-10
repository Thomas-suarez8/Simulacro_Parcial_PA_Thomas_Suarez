#Punto 1. En un sistema básico de control, un usuario ingresa un código
#que supuestamente representa un número binario. Sin embargo, la
#entrada puede contener espacios al inicio o al final, letras en
#mayúscula o caracteres inválidos.

codigo = input('Ingrese un numero binario: ')

codigo = codigo.strip()

if set(codigo) <= {'0', '1'}:
    decimal = int(codigo, 2)
    print(f'El numero binario en decimal es:", decimal')

else:
    print(f'Error: el código ingresado no es un numero binario.')