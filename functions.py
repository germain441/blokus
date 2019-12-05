from pieces import *


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
    encrage = 0
    j = 0
    while pion[0][j] == 0 :
            encrage = encrage + 1
            j = j +1
    return encrage


def ajouter(_grille, x, y, pion, couleur):
    index = pion - 1

    pion = dico[couleur][index]

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1 and _grille[x + i][y + (j-point_encrage(pion))] != '• ':
                return False

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1:
                _grille[x + i][y + (j-point_encrage(pion))] = (couleur + '  ' + Back.RESET)

    dico[couleur][index] = False

    return True


def choix_couleur(coup):
    return [Back.RED, Back.BLUE, Back.GREEN, Back.YELLOW][coup % 4]


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

    for elem in [pion1, pion2, pion3]:
        _quit = False
        while not _quit:
            for i in range(5):
                if elem[0][i] == 1:
                    _quit = True
                    break
            if _quit:
                break
            for i in range(4):
                elem[i], elem[i + 1] = elem[i + 1], elem[i]

        _quit = False
        while not _quit:
            for i in range(5):
                if elem[i][0] == 1:
                    _quit = True
                    break
            if _quit:
                break
            for i in range(5):
                for j in range(4):
                    elem[i][j], elem[i][j + 1] = elem[i][j + 1], elem[i][j]

    print(1, " " * 4, 2, " " * 4, 3, " " * 4, 4)
    for i in range(5):
        for elem in [pion, pion1, pion2, pion3]:
            for j in range(5):
                if elem[i][j] == 1:
                    print(couleur + ' ' + Back.RESET, end='')
                else:
                    print(end=' ')
            print(end="  ")
        print()

    _quit = False
    x = 0
    while not _quit:
        x = int(input("Quel rotation ?"))
        if not 1 <= x <= 4:
            print("choix non valide")
            continue
        _quit = True

    dico[couleur][index] = [pion, pion1, pion2, pion3][x - 1]


def jouer():

    coup = 0
    coup_valide = False

    while not coup_valide:
        couleur = choix_couleur(coup)
        piece_dispo(couleur)
        pion = int(input('quel pion voulez vous jouer ? '))
        if not dico[couleur][pion - 1]:
            print("Piece non disponible ")
        rotation(pion, couleur)

        if coup == 0:
            x = 1
            y = 1
        elif coup == 1:
            x = 20
            y = 1
        elif coup == 2:
            x = 1
            y = 20
        elif coup == 3:
            x = 20
            y = 20
        else:
            x = int(input('Entrez la ligne :'))
            y = int(input('Entrez la colonne : '))
        if 0 < x < 21 and 0 < y < 21:
            coup_valide = ajouter(grille, x, y, pion, couleur)
            afficher_grille(grille)
            if coup_valide:
                coup = coup + 1
            else:
                print("coup non valide")
        else:
            print('Coordonnee non valides')

        coup_valide = False
