from tkinter import *

fenetre = Tk()
fenetre.title("Blokus")

fenetre.geometry("900x700")
fenetre.resizable(width=False, height=False)


grille = Frame(fenetre, borderwidth=2, relief=GROOVE)
grille.pack(side=LEFT, padx=0, pady=0)

texte_fenetre = Frame(fenetre, borderwidth=1, relief=GROOVE)
texte_fenetre.pack(side=TOP, ipadx=700, pady=0)

canvas_grille = Canvas(grille, width=700, height = 700, background = 'grey')
for i in range (21):
    ligne=canvas_grille.create_line(i*33.3333333, 0, i*33.333333, 700)
    ligne = canvas_grille.create_line(0, i * 33.3333333, 700, i * 33.3333333)
canvas_grille.pack()

canvas_texte = Canvas(texte_fenetre, width = 200, height=50, background='black')
valeur = StringVar()
valeur.set("Entrez la piece : ")
entree = Entry(canvas_texte, textvariable= valeur , width=200)
entree.pack()
canvas_texte.pack()


fenetre.mainloop()
