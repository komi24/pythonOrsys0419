# -*- coding: utf-8 -*-

from random import randint as ri
from .Pompier import Pompier
from tkinter import *



class BoardManager:
    def __init__(self):
        self.size = [20,20]
        self.liste_feux = [[ri(0,self.size[0]-1),ri(0,self.size[0]-1)] for i in range(6)]
        self.liste_pompiers = [Pompier(
            [ ri(0,self.size[0]-1), ri(0,self.size[1]-1)]
            ) for i in range(4)]
        # Initialisation de Tkinter    
        self.fen = Tk()
        self.canvas = Canvas(self.fen,
                    width=self.size[0]*32,
                    height=self.size[0]*32)
        self.canvas.pack()
        self.photo_pompier = PhotoImage(file="robot.png")
        self.photo_feu = PhotoImage(file="fire.png")
        
        # Lance la simulation
        self.one_step()
        
        self.fen.mainloop()
    
    
    def closest_fire(self, pompier):
        closest = self.liste_feux[0]
        distance_min = (
                abs(pompier.position[0] - self.liste_feux[0][0])
                + abs(pompier.position[1] - self.liste_feux[0][1]))
        for feu in self.liste_feux:
            distance = (
                abs(pompier.position[0] - feu[0])
                + abs(pompier.position[1] - feu[1]))
            if distance < distance_min:
                closest = feu
                distance_min = distance
        return closest
    
    def run(self):
        for pompier in self.liste_pompiers:
            if(self.liste_feux):
                pompier.se_deplacer(self.closest_fire(pompier), self)

    def one_step(self):
        self.run()
        self.draw_everything()
        if self.liste_feux:
            self.canvas.after(400, self.one_step)
    
    def draw_everything(self):
        print("dessin")
        self.canvas.delete("all")
        for pompier in self.liste_pompiers:
            # Je dessine mon pompier
            self.canvas.create_image(
                    pompier.position[0]*32+16,
                    pompier.position[1]*32+16,
                    image=self.photo_pompier)
            
        for feu in self.liste_feux:
            # Je dessine ma liste de feux
            self.canvas.create_image(
                    feu[0]*32+16,
                    feu[1]*32+16,
                    image=self.photo_feu)
        
    def display(self):
        for i in range(self.size[0]):
            line = ''
            for j in range(self.size[1]):
                #line += 'i' if liste_feux.count((i,j))!=0 else ' '
                line += 'i' if [i,j] in self.liste_feux else '.'
                line += 'x' if [i,j] in [p.position for p in self.liste_pompiers] else '.'
            print(line)

if __name__ == "__main__":
    print("Je suis dans le module BoardManager")