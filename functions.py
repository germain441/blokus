from pieces import *
import pickle
import os
from random import randint

dico = {Back.RED: get_piece(), Back.BLUE: get_piece(), Back.YELLOW: get_piece(), Back.GREEN: get_piece()}
ordre_couleur = [Back.RED, Back.BLUE, Back.YELLOW, Back.GREEN]


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


def case(couleur):
    return couleur + '  ' + Back.RESET


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
                _grille[x + i][y + j] = (case(couleur))

    dico[couleur][index] = False


def ajouter(_grille, x, y, pion, couleur, coup):
    index = pion - 1

    pion = dico[couleur][index]
    y += point_encrage(pion)
    if coup > 3:
        coin = False
        for i in range(5):
            for j in range(5):
                if pion[i][j] != 1:
                    continue
                if _grille[x + i][y + j] != '• ':
                    return False
                if _grille[x - 1 + i][y + j] == case(couleur) or (
                        _grille[x + 1 + i][y + j] == case(couleur)) or (
                        _grille[x + i][y - 1 + j] == case(couleur)) or (
                        _grille[x + i][y + 1 + j] == case(couleur)):
                    return False
                if _grille[x - 1 + i][y - 1 + j] == case(couleur) or (
                        _grille[x - 1 + i][y + 1 + j] == case(couleur)) or (
                        _grille[x + 1 + i][y - 1 + j] == case(couleur)) or (
                        _grille[x + 1 + i][y + 1 + j] == case(couleur)):
                    coin = True
        if not coin:
            return False
    else:
        if not placer_premier(_grille, pion, x, y, coup):
            return False

    return True


def fin_partie(couleur, _grille, coup):
    longueur = len(dico[couleur])

    for index in range(longueur):
        if not dico[couleur][index]:
            continue
        for x in range(1, 21):
            for y in range(1, 21):
                z = ajouter(_grille, x, y, index + 1, couleur, coup)
                if not z:
                    return False
    return True


def choix_couleur(coup):
    return ordre_couleur[coup % 4]


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


def bot(_grille, couleur, coup):
    res = []

    for elem in range(21):
        if not dico[couleur][elem]:
            continue
        for x in range(1, 21):
            for y in range(1, 21):
                if ajouter(_grille, x, y, elem + 1, couleur, coup):
                    res.append((elem + 1, x, y))

    if len(res) < 1:
        return False
    elem, x, y = res[randint(0, len(res) - 1)]

    placer(x, y, elem, _grille, couleur)
    return True


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
                    print(case(couleur), end='')
                else:
                    print(end='  ')
            print(end="  ")
        print()

    _quit = False
    x = 0
    while not _quit:
        try:
            x = int(input("Quelle rotation ?"))
        except ValueError:
            pass
        if not 1 <= x <= len(_rotation):
            print("choix non valide")
            continue
        _quit = True

    dico[couleur][index] = [pion, pion1, pion2, pion3][x - 1]


def compter_points(couleur, dernier_pion):
    score = 0
    for i in range(21):
        if dico[couleur][i]:
            for x in range(5):
                for y in range(5):
                    if dico[couleur][i][x][y] == 1:
                        score = score - 1
    if score == 0:
        if dernier_pion == 1 :
            score = 21
        else :
            score = 15
    return score


# def classement(a,b,c,d):

def jouer():
    global ordre_couleur
    coup = 0
    coup_valide = False
    dernier_pion = None
    try:
        if os.path.isfile("loads/save"):
            pion = input("A chaque coup la partie est sauvegardée\ncharger la partie ? (o/n) :")
            if pion == 'o':
                coup = charger_partie()
            else:
                os.remove("loads/save")
    except Exception as e:
        print(e)

    _bot = 0
    while not 1 <= _bot <= 3:
        _bot = int(input("Choisir ...\n \t1 - Voir 2 bots jouer\n\t2 - jouer avec un bot\n\t3 - jouer sans bot\n : "))

    if _bot == 1:
        input("Bot 1 gère le Rouge et le Bleu. Bot 2 gère le Jaune et le Vert. Appuyer sur entrer pour continuer")
    else:
        tmp = []
        while len(ordre_couleur) > 2:
            for elem in ordre_couleur:
                print(elem + "  " + Back.RESET)
            a = int(input("Joueur 1 choisi une couleur (1 - " + str(len(ordre_couleur)) + ") : "))
            if not 1 <= a <= len(ordre_couleur):
                continue
            tmp.append(ordre_couleur.pop(a-1))
        if _bot == 2:
            ordre_couleur = ordre_couleur + tmp
        else:
            ordre_couleur = tmp + ordre_couleur

    b = 0
    dernier_pion = None
    while not coup_valide:
        afficher_grille(grille)
        couleur = choix_couleur(coup)
        if not fin_partie(couleur, grille, coup) and b != 4:
            piece_dispo(dico, couleur)
            if _bot != 3 and not coup % _bot:
                if not bot(grille, couleur, coup):
                    b += 1
                coup += 1
                continue
            try:
                pion = int(input('quel pion voulez vous jouer ? '))
                dernier_pion = pion
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
            coup += 1
            if b == 4:
                input("Fin : appuyez sur entree pour voir les scores")
                break
    piece_dispo(dico, ordre_couleur[0])
    piece_dispo(dico, ordre_couleur[1])
    print('point joueur 1 :', compter_points(ordre_couleur[0], dernier_pion) + compter_points(ordre_couleur[1], dernier_pion) )
    piece_dispo(dico, ordre_couleur[2])
    piece_dispo(dico, ordre_couleur[3])
    print('point joueur 2 :', compter_points(ordre_couleur[2], dernier_pion) + compter_points(ordre_couleur[3], dernier_pion) )

