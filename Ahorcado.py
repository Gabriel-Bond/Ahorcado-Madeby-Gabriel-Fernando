#AHORCADO DEL BIENESTAR
#Version 1.05
#programado por: Gabriel Rodrigo Enríquez Guerra y Fernando Alejandro Hernandéz Ramos


import random #se importa random para aleatorizar la selección de palabras
#Gráfico del ahorcado
dibujo_ahorcado = [ 
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''', 
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    ''',
]
#Lista de palabras y niveles
palabras_nivel_1 = ['carro','pato','pollo','carne']
palabras_nivel_2 = ['calavera','java','talacha','python']
palabras_nivel_3 = ['chocolate','batman','vehiculo','bubblesort']
palabras_nivel_4 = ['astonmartin','bienestar','tecnologias','esternomastoideo']

niveles = {
    1: {"palabras": palabras_nivel_1, "intentos": 6},
    2: {"palabras": palabras_nivel_2, "intentos": 5},
    3: {"palabras": palabras_nivel_3, "intentos": 4},
    4: {"palabras": palabras_nivel_4, "intentos": 2}
}


lista_abecedario = list('abcdefghijklmnñopqrstuvwxyz')
letras_descartadas = []
#se define la muestra del estado de juego
def mostrar_estado():
    print(f'Intentos restantes: {intentos}')
    print(f'Letras descartadas: {", ".join(letras_descartadas)}\n')
    print(f'Palabra: {" ".join(palabra_oculta)}\n')
    print(dibujo_ahorcado[6 - intentos])

def letra_valida(letra):
    if len(letra) != 1 :
        print('Has puesto más de una letra, inténtalo de nuevo.')
        return False
    elif letra not in lista_abecedario:
        print('No has introducido una letra del abecedario')
        return False
    elif letra in palabra_oculta:
        print('La letra que has introducido ya la has acertado, inténtalo de nuevo.')
        return False
    elif letra in letras_descartadas:
        print('Esa letra ya la habías dicho, inténtalo de nuevo.')
        return False
    else:
        return True

def gestion_letra(letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            palabra[i] = '_'
#Menú
while True:
    print("\n==============================")
    print("      🔥AHORCADO DEL BIENESTAR🔥")
    print("==============================")
    print("1 - Fácil")
    print("2 - Medio")
    print("3 - Difícil")
    print("4 - Modo Diablo 😛😈🔥")
    print("0 - Salir")
    print("==============================")
    quieres=input("Selecciona una opcion: ")
    if quieres == "0":
        print("\nGracias por jugar viejo, eres la onda. ¡Hasta luego!")
        break

    if quieres not in ["1", "2", "3", "4"]:
        print("\n Opción inválida.")
        continue
    nivel=int(quieres)  
    palabras_restantes = niveles[nivel]["palabras"][:]
    #Inicio del juego
    while palabras_restantes:
        palabra_seleccionada = random.choice(palabras_restantes)
        palabras_restantes.remove(palabra_seleccionada)

        palabra = list(palabra_seleccionada)
        palabra_oculta = ['_'] * len(palabra)
        intentos = niveles[nivel]["intentos"]
        letras_descartadas.clear()
    print(f"\nNueva palabra ({len(palabra)} letras). ¡Suerte!\n")
    while intentos > 0 and '_' in palabra_oculta:
        mostrar_estado()
        print('-'*50)
        letra = input('INTRODUCE LETRA: ').lower()

        while not letra_valida(letra):
            letra = input('INTRODUCE OTRA LETRA: ').lower()
#Acierto
        if letra in palabra:
            gestion_letra(letra)
            print('-'*50)
            print('¡Has acertado la letra! Sigue así.')
#Fallo
        else:
            print('-'*50)
            print('¡Has fallado la letra!')
            letras_descartadas.append(letra)
            intentos -= 1

    if '_' not in palabra_oculta:
        print("\n✔️ ¡Palabra completada!")
        print("La palabra es: ",palabra_seleccionada)

    else:

        print(f'\nOh! :( Lo siento, ¡has perdido!'
        '''\n
       +---+
       |   |
      💀   |
      /|\  |
      / \  |
           |
    =========
    ''')
        continue