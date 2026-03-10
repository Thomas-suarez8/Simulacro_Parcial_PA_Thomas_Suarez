#Problema 3. Una plataforma académica define que un identificador válido debe cumplir estas condiciones:
#- Debe iniciar con la palabra 'est'.
#- Debe tener exactamente 8 caracteres.
#- Los últimos 3 caracteres deben ser dígitos.

identificador = input('Ingrese el identificador: ')

identificador = identificador.strip()

if not identificador.startswith('est'):
    print(f'Error: no inicia con est')

elif len(identificador) != 8:
    print(f'Error: longitud incorrecta')

elif not identificador[-3:].isdigit():
    print(f'Error: terminación numerica inválida')

else:
    print(f'Identificador válido')
