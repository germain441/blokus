import colorama
from colorama import Fore, Back, Style
from pieces import *


def init_grille():
    grille = []
    for i in range (22):
        grille.append(['• ']* 22)

    for i in range(21):
        grille[i][0]=i
        grille[0][i]=i
    for i in range(1,22):
        grille[i][21]='|'
        grille[21][i]='- '
    return grille


grille = init_grille()


def afficher_grille(grille):
    longueur = len(grille)

    for i in range(longueur):
        print()
        for j in range (longueur):
            if (i < 10) and (j == 0) :
                print(grille[i][j], end=' ')
            elif ( j < 10) and (i==0):
                if j==9 :
                    print(grille[i][j], end ='')
                else :
                    print(grille[i][j],  end=' ')
            elif (j >= 10) and (i == 0):
                print(grille[i][j],  end='')
            else:
               print(grille[i][j], end= '')
    print()
    print()


def ajouter(grille, x, y, pion, couleur):
    index = pion - 1
    pion = piece[index]

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1 and grille[x + i][y + j] != '• ':
                return False

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1:
                grille[x + i][y + j] = (couleur + '  ' + Back.RESET)

    dico[couleur][index] = False

    return True


def choix_couleur(coup):
    return [Back.RED, Back.BLUE, Back.GREEN, Back.YELLOW][coup % 4]


def rotation(pion, couleur):
    index = pion -1
    pion = piece[index]
    pion1 = pion2 = pion3 = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]

    for i in range(5):
        for j in range(5):
            if pion[i][j] == 1 :
                pion1[i][2-(j-2)] = 1
                pion2[(2-(i-2))][j] = 1
            else :
                pion1[i][2 - (j - 2)] = 0
                pion2[2 - (i - 2)][j] = 0
            #pion3[2 - (i - 2)][2 - (j - 2)] = pion[i][j]
    rotation_pion = [pion, pion1, pion2, pion3]
    for i in range(5):
        print()
        for j in range(5):
            print(pion2[i][j], end='')
    #for x in range(0,2):
     #    for i in range(5):
      #      print()
       #     for j in range(5):
        #        if rotation_pion[x][i][j]==1:
         #           print(couleur + '  '+ Back.RESET, end='')
          #      else:
           #         print('  ', end='')
         #print(' ', end='')



def jouer():
    coup=0
    fin = True
    coup_valide = False

    while fin:
        while not coup_valide:
            couleur = choix_couleur(coup)
            piece_dispo(couleur)
            pion = int(input('quel pion voulez vous jouer ? '))
            rotation(pion, couleur)
            if dico[couleur][pion - 1]:
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
                    print('Coordonnee non valides')
            else:
                print("Piece non disponible ")
        coup_valide = False
