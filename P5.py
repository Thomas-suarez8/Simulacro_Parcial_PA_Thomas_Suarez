#Problema 5. En una red digital sencilla, una trama de 8 bits debe ser analizada antes de procesarse.
#Reglas:
#- Si no tiene exactamente 8 caracteres, la trama es inválida.
#- Si contiene caracteres distintos de 0 y 1, la trama es inválida.
#- Si tiene más de 5 bits en 1 → Trama de alta activación.
#- Si tiene entre 3 y 5 bits en 1 → Trama de activación media.
#- Si tiene entre 0 y 2 bits en 1 → Trama de baja activación.

trama = input("Ingrese la trama: ")

trama = trama.strip()


if len(trama) != 8:
    print(f'Trama invalida: longitud incorrecta')

elif trama.replace('0','').replace('1','') != '':
    print(f'Trama invalida: contiene caracteres no binarios')

else:
    uno = trama.count('1')

    if uno > 5:
        print(f'Trama de alta activacion')

    elif 3 <= uno <= 5:
        print(f'Trama de activacion media')

    else:
        print(f'Trama de baja activacion')