from fonctions import *

from tkinter import *
#Tk, Button, Label, Canvas, Frame, StringVar

MaFenetre = Tk()
MaFenetre.title('Jeu du pendu')
#MaFenetre['bg']='bisque'
MaFenetre.geometry("300x200+100+100")

Framemot = Frame(MaFenetre ,bg = "white" ,borderwidth = 2, relief='groove')
Framemot.pack(side = 'left', padx=5, pady=5)

Framedessin = Frame(MaFenetre, bg = "blue" ,borderwidth = 2,relief = 'groove')
Framedessin.pack(side = 'right', padx = 10, pady = 10)

Frameproposition = Frame(MaFenetre, bg = "red" ,borderwidth = 2,width=100, height=100,relief='groove')
Frameproposition.pack(side = 'bottom', padx=5, pady=5)

boutonQuitter = Button(Frameproposition, text= "Quitter", command= MaFenetre.destroy)
boutonQuitter.pack()

proposition= StringVar
propostionchamp = Entry(Frameproposition, textvariable= proposition, show = "*").pack(side = 'left' , padx = 5, pady= 5)
MaFenetre.mainloop()