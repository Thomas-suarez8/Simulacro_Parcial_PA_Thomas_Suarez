#Problema 2. En una encuesta, el usuario debe responder si desea
#continuar con el proceso. La respuesta puede venir escrita de muchas
#formas: "SI", "si", "Sí", "no", etc.
respuesta = input('¿Desea continuar con el proceso? ')

respuesta = respuesta.strip().lower()

if respuesta == 'si' or respuesta == 'sí':
    print(f'Respuesta afirmativa: el proceso continuara')

elif respuesta == "no":
    print(f'Respuesta negativa: el proceso se detendra')

else:
    print(f'Respuesta invalida')