from pieces import *
import pickle
import os

dico = {Back.RED: piece_R, Back.BLUE: piece_B, Back.YELLOW: piece_J, Back.GREEN: piece_V}


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


def dans_un_coin(x, y, _grille, couleur):
    if (x - 1 > 0 and ((y - 1 > 0 and _grille[x - 1][y - 1] == couleur + '  ' + Back.RESET) or (
            y + 1 < 21 and _grille[x - 1][y + 1] == couleur + '  ' + Back.RESET))) or (x + 1 < 21 and (
            (y - 1 > 0 and _grille[x + 1][y - 1] == couleur + '  ' + Back.RESET) or (
            y + 1 < 21 and _grille[x + 1][y + 1] == couleur + '  ' + Back.RESET))):
        return True

    return False


def placer(x, y, pion, _grille, couleur):
    index = pion - 1

    pion = dico[couleur][index]
    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1:
                _grille[x + i][y + j] = (couleur + '  ' + Back.RESET)

    dico[couleur][index] = False


def ajouter(_grille, x, y, pion, couleur, coup):
    index = pion - 1

    pion = dico[couleur][index]
    y += point_encrage(pion)

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1 and _grille[x + i][y + j] != '• ':
                return False

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1:
                if _grille[x - 1 + i][y + j] == (couleur + '  ' + Back.RESET) or _grille[x + 1 + i][y + j] == (
                        couleur + '  ' + Back.RESET) or _grille[x + i][y - 1 + j] == (couleur + '  ' + Back.RESET) or \
                        _grille[x + i][y + 1 + j] == (couleur + '  ' + Back.RESET):
                    return False

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1:
                if coup > 3:
                    if _grille[x - 1 + i][y - 1 + i] == (couleur + '  ' + Back.RESET) or _grille[x - 1 + i][y + 1 + i] == (
                            couleur + '  ' + Back.RESET) or _grille[x + 1 + i][y - 1 + i] == (couleur + '  ' + Back.RESET) or \
                            _grille[x + 1 + i][y + 1 + i] == (couleur + '  ' + Back.RESET):
                        return True
    if coup > 3 :
        return False
    else :
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
    except (OSError, IOError) as e:
        print("Il n'y a pas de fichier de sauvegarde")
        input("appuyer entrer ")
        print(e)
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

    pion = input("A chaque coup la partie est sauvegardée\ncharger la partie ? (o/n) :")
    if pion == 'o':
        coup = charger_partie()
    else:
        try:
            os.remove("loads/save")
        except FileNotFoundError as e:
            print("il n'y a pas de sauvegarde")
            input("appuyer sur entrer pour continuer...")

    while not coup_valide:
        afficher_grille(grille)
        couleur = choix_couleur(coup)
        piece_dispo(dico, couleur)
        try:
            pion = int(input('quel pion voulez vous jouer ? '))
            if not 1 <= pion <= 23:
                raise Exception("wtf wtf wtf")
        except Exception as e:
            print("rentrez un numéro")
            print(e)
            continue
        if not dico[couleur][pion - 1]:
            print("Piece non disponible ")
            continue
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
            coup_valide = ajouter(grille, x, y, pion, couleur, coup)
            afficher_grille(grille)
            if coup_valide:
                placer(x, y, pion, grille, couleur)
                coup = coup + 1
            else:
                print("coup non valide")
        else:
            print('Coordonnee non valides')

        coup_valide = False
