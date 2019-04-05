from .BoardManager import BoardManager
from tkinter import *

class BoardManagerUI(BoardManager):
	def __init__(self):
		BoardManager.__init__(self)
		self.fen = Tk()
		self.h = 128
		self.w = 128
		self.photo = PhotoImage(file="pomp.gif")
		self.photoFeu = PhotoImage(file="feu.gif")
		self.canvas = Canvas(self.fen, 
			width=self.w*self.size[0], 
			height=self.h*self.size[1])
		self.canvas.pack()

		self.display()
		self.start()

		self.fen.mainloop()

	def display(self):
		self.canvas.delete('all')
		for pompier in self.liste_pompiers:
			self.canvas.create_image(
				self.w/2+pompier.position[0]*self.w,
				self.h/2+pompier.position[1]*self.h, 
				image=self.photo)
		for feu in self.liste_feux:
			self.canvas.create_image(
				self.w/2+feu[0]*self.w,
				self.h/2+feu[1]*self.h, 
				image=self.photoFeu)

	def start(self):
		self.run()
		self.display()
		if self.liste_feux:
			self.canvas.after(500, self.start)