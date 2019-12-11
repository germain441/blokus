from colorama import Back

p1 = [[1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p2 = [[1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p3 = [[1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p4 = [[1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p5 = [[1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p6 = [[0, 1, 0, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p7 = [[1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p8 = [[1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p9 = [[1, 1, 0, 0, 0],
      [0, 1, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]

p10 = [[1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0]]

p11 = [[0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0]]

p12 = [[0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p13 = [[0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p14 = [[1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p15 = [[1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p16 = [[0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p17 = [[1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p18 = [[1, 1, 0, 0, 0],
       [0, 1, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p19 = [[1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p20 = [[1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

p21 = [[0, 1, 0, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]


def get_piece():
    return [x.copy() for x in
            [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21]]


def largeur_piece(piece):
    largeur = 0
    for x in range(5):
        for y in range(5):
            if piece[x][y] == 1 and largeur < y:
                largeur = y
    return largeur + 1


def numero_piece(liste):
    for i in range(1, 22):
        if liste[i - 1]:
            if i == 1 or i == 2 or i == 3 or i == 6 or i == 13 or i == 14 or i == 21:
                print(i, end='   ')
            elif i == 4 or i == 5 or i == 7 or i == 8:
                print(i, end='     ')
            elif i == 9:
                print(i, end='       ')
            elif i == 10 or i == 11 or i == 12 or i == 16:
                print(i, end='    ')
            elif i == 15 or i == 17 or i == 18 or i == 19:
                print(i, end='      ')
            elif i == 20:
                print(i, end='        ')
    print()


def piece_dispo(dico, couleur):
    print()
    numero_piece(dico[couleur])
    for j in range(5):
        for i in range(21):
            piece = dico[couleur][i]
            if piece:
                largeur = largeur_piece(piece)
                for x in range(largeur):
                    if piece[j][x] == 1:
                        print(couleur + '  ' + Back.RESET, end='')
                    else:
                        print('  ', end='')
                print('  ', end='')
        print()


def placer_premier(_grille, piece, x, y, coup):
    res = 0
    if _grille[1][1] != '• ':
        res += 1
    if _grille[1][20] != '• ':
        res += 1
    if _grille[20][1] != '• ':
        res += 1
    if _grille[20][20] != '• ':
        res += 1

    if coup != res:
        return False

    res = True

    for i in range(5):
        if i + x != 20 and i + x != 1:
            continue
        for j in range(5):
            if piece[i][j] != 1:
                continue
            if i + x > 20 or j + y > 20:
                return False
            if j + y != 20 and j + y != 1:
                continue
            res = False
            if _grille[i + x][j + y] != '• ':
                return False

    if res:
        return False
    return True
