from pieces import *
import pickle
import os
from random import randint

dico = {Back.RED: get_piece(), Back.BLUE: get_piece(), Back.YELLOW: get_piece(), Back.GREEN: get_piece()}


def init_grille():
    _grille = []
    for i in range(22):
        _grille.append(['• '] * 22)

    for i in range(21):
        _grille[i][0] = i
        _grille[0][i] = i
    for i in range(1, 22):
        _grille[i][21] = '|'
        _grille[21][i] = '- '
    return _grille


grille = init_grille()


def afficher_grille(_grille):
    longueur = len(_grille)

    for i in range(longueur):
        print()
        for j in range(longueur):
            if i < 10 and j == 0:
                print(_grille[i][j], end=' ')
            elif j < 10 and i == 0:
                if j == 9:
                    print(_grille[i][j], end='')
                else:
                    print(_grille[i][j], end=' ')
            elif j >= 10 and i == 0:
                print(_grille[i][j], end='')
            else:
                print(_grille[i][j], end='')
    print('\n')


def point_encrage(pion):
    for j in range(5):
        if pion[0][j] == 1:
            return -j
    raise Exception("il n'y a pas de 1 sur la première ligne")


def placer(x, y, pion, _grille, couleur):
    index = pion - 1
    pion = dico[couleur][index]
    y += point_encrage(pion)

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1:
                _grille[x + i][y + j] = (couleur + '  ' + Back.RESET)

    dico[couleur][index] = False


def ajouter(_grille, x, y, pion, couleur, coup):
    index = pion - 1

    pion = dico[couleur][index]
    y += point_encrage(pion)

    if coup > 3:
        for i in range(5):
            for j in range(5):
                if pion[i][j] == 1 and (_grille[x + i][y + j] != '• ' or
                                        _grille[x - 1 + i][y + j] == couleur + '  ' + Back.RESET or
                                        _grille[x + 1 + i][y + j] == couleur + '  ' + Back.RESET or
                                        _grille[x + i][y - 1 + j] == couleur + '  ' + Back.RESET or
                                        _grille[x + i][y + 1 + j] == couleur + '  ' + Back.RESET):
                    return False
    else:
        if not placer_premier(_grille, pion, x, y, coup):
            return False

    return True


def fin_partie(couleur, _grille, coup):
    longueur = len(dico[couleur])

    for index in range(longueur):
        for x in range(1, 21):
            for y in range(1, 21):
                if dico[couleur][index] and ajouter(_grille, x, y, index + 1, couleur, coup):
                    return False
            else:
                return True


def choix_couleur(coup):
    return [Back.RED, Back.BLUE, Back.GREEN, Back.YELLOW][coup % 4]


def sauvegarder_partie(coup):
    if not os.path.isdir("loads"):
        os.mkdir("loads")
    config = {"pieces": dico, "grille": grille, "coup": coup}
    p = open("loads/save", "wb")
    pickle.dump(config, p)
    p.close()


def charger_partie():
    global grille, dico

    try:
        p = open("loads/save", "rb")
        config = pickle.load(p)
        p.close()
        dico = config["pieces"]
        grille = config["grille"]
        return config["coup"]
    except (OSError, IOError):
        print("Il n'y a pas de fichier de sauvegarde")
        input("appuyer entrer ")
        return 0


def _coup(liste):
    i = 0
    for elem in liste:
        for _elem in elem:
            if _elem:
                i += 1
    return i


def rotation(pion, couleur):
    index = pion - 1
    pion = dico[couleur][index]

    pion1 = [[0 for i in range(5)] for j in range(5)]
    pion2 = [[0 for i in range(5)] for j in range(5)]
    pion3 = [[0 for i in range(5)] for j in range(5)]

    for i in range(5):
        for j in range(5):
            pion1[i][j] = pion[4 - j][i]
            pion2[i][j] = pion[4 - i][4 - j]
            pion3[i][j] = pion[j][4 - i]

    _rotation = [pion, pion1, pion2, pion3]

    for elem in range(1, 4):
        _quit = False
        while not _quit:
            for i in range(5):
                if _rotation[elem][0][i] == 1:
                    _quit = True
                    break
            if _quit:
                break
            for i in range(4):
                _rotation[elem][i], _rotation[elem][i + 1] = _rotation[elem][i + 1], _rotation[elem][i]

        _quit = False
        while not _quit:
            for i in range(5):
                if _rotation[elem][i][0] == 1:
                    _quit = True
                    break
            if _quit:
                break
            for i in range(5):
                for j in range(4):
                    _rotation[elem][i][j], _rotation[elem][i][j + 1] = _rotation[elem][i][j + 1], _rotation[elem][i][j]

    def equals(a, b):
        t = len(a)
        if t != len(b):
            return False
        for _i in range(t):
            for _j in range(t):
                if a[_i][_j] != b[_i][_j]:
                    return False
        return True

    if equals(_rotation[0], _rotation[2]):
        _rotation.pop(2)

    if equals(_rotation[1], _rotation[2]):
        _rotation.pop(2)

    if equals(_rotation[0], _rotation[1]):
        _rotation.pop(1)

    if len(_rotation) <= 1:
        return

    for i in range(1, len(_rotation) + 1):
        print(i, "  " * 5, end='')
    print()

    for i in range(5):
        for elem in _rotation:
            for j in range(5):
                if elem[i][j] == 1:
                    print(couleur + '  ' + Back.RESET, end='')
                else:
                    print(end='  ')
            print(end="  ")
        print()

    _quit = False
    x = 0
    while not _quit:
        x = int(input("Quelle rotation ?"))
        if not 1 <= x <= len(_rotation):
            print("choix non valide")
            continue
        _quit = True

    dico[couleur][index] = [pion, pion1, pion2, pion3][x - 1]


def jouer():
    coup = 0
    coup_valide = False

    try:
        if os.path.isfile("loads/save"):
            pion = input("A chaque coup la partie est sauvegardée\ncharger la partie ? (o/n) :")
            if pion == 'o':
                coup = charger_partie()
            else:
                os.remove("loads/save")
    except Exception as e:
        print(e)

    while not coup_valide:
        afficher_grille(grille)
        couleur = choix_couleur(coup)
        if not fin_partie(couleur, grille, coup):
            piece_dispo(dico, couleur)
            try:
                pion = int(input('quel pion voulez vous jouer ? '))
                if not 1 <= pion <= 23:
                    raise Exception("wtf wtf wtf")
            except ValueError:
                print("rentrez un numéro")
                continue
            if not dico[couleur][pion - 1]:
                print("Piece non disponible ")
                continue
            rotation(pion, couleur)

            x = int(input('Entrez la ligne :'))
            y = int(input('Entrez la colonne : '))

            if 0 < x < 21 and 0 < y < 21:
                coup_valide = ajouter(grille, x, y, pion, couleur, coup)
                if coup_valide:
                    placer(x, y, pion, grille, couleur)
                    coup += 1
                else:
                    print("coup non valide")
                    input("appuyer sur entrer pour continuer...")
                    continue
                sauvegarder_partie(coup)
            else:
                print('Coordonnées non valides')

            coup_valide = False
        else:
            coup = coup + 1
