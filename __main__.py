import os
import random
import sys

nombre_archivo = 'words.txt'
words = []


def load_words():
    try:
        with open(nombre_archivo, 'r') as archivo:
            for palabra in archivo:
                words.append(palabra[:-1])
                print(words)
    except:
        return


load_words()


def save_words():
    global item
    with open(nombre_archivo, 'w') as file:
        for item in words:
            file.write("{}\n".format(item))


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw():
    clear()
    print("Errores {}/7".format(len(errores)))
    print('')
    global letter
    for letter in errores:
        print(letter, end=" ")
    print("\n\n")
    for letter in palabra_secreta:
        if letter in aciertos:
            print(letter, end='')
        else:
            print("_", end='')
    print("")


while True:
    start = input("Seleccione una opcion"
                  "\nJ | Comenzar la partida "
                  "\nL | Acceder a la lista de palabras "
                  "\nQ | Salir del programa\n").lower()
    if start == 'q':
        print("Gracias por jugar!")
        sys.exit()
    if start == 'l':
        while True:
            lista = input(
                "Este es el control de la lista de palabras usadas en el ahorcado "
                "\nA | Añadir palabras a la lista "
                "\nM | Mostrar la lista de palabras "
                "\nB | Borrar una palabra "
                "\nQ \ Para volver al menu anterior\n").lower()
            if lista == 'a':
                while True:
                    print(
                        "Escriba una palabra para añadirla a la lista"
                        "\nO Q para volver atras\n"
                    )
                    nueva_palabra = input('> ').lower()
                    if nueva_palabra == 'q':
                        break
                    if nueva_palabra in words:
                        print("Seleccione una palabra distinta por favor")
                    else:
                        words.append(nueva_palabra)
                        save_words()
            if lista == 'm':
                print("La lista de palabras es:\n")
                for item in words:
                    print(item)
            if lista == 'q':
                break
            if lista == 'b':
                while True:
                    borrar = input(
                        "Escriba la palabra que desea borrar de la lista o Q para volver al menu anterior").lower()
                    if borrar == 'q':
                        break
                    if borrar in words:
                        try:
                            words.remove(borrar)
                        except:
                            print('Ocurrio un error al intentar borrar la palabra')
                        save_words()
                    else:
                        print('{} no esta en la lista por favor elija otra palabra o pon Q para volver atras'.format(
                            borrar))
    if start == 'j':
        palabra_secreta = random.choice(words)
        errores = []
        aciertos = []
        while len(errores) < 7 and len(aciertos) != len(list(palabra_secreta)):
            draw()
            intento = input("Introduzca una letra o \"Salir\" para dejar de jugar").lower()
            if len(intento) != 1:
                print('Solo puedes poner una letra!')
                continue
            elif intento in aciertos or intento in errores:
                print("Ya has introducido esa letra")
                continue
            elif not intento.isalpha():
                print("Solo esta permitido introducir letras!")
                continue
            elif intento in palabra_secreta:
                aciertos.append(intento)
                global encontrado
                encontrado = True
                for letter in palabra_secreta:
                    if letter not in aciertos:
                        encontrado = False
            else:
                errores.append(intento)
            if encontrado:
                clear()
                print('Felicidades, has ganado, la palabra era {}'.format(palabra_secreta))
                break
        else:
            print('No lo has acertado, la palabra era {}'.format(palabra_secreta))
