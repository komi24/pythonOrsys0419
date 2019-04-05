# -*- coding: utf-8 -*-


class Pompier:
	def __init__(self, position):
		self.position = position
		self.busy = 0
	def se_deplacer(self, feu, board):
		if self.busy > 0:
			self.busy -= 1
			return	
		if self.position[0] != feu[0]:
			self.position[0] += 1 if self.position[0] < feu[0] else -1
		elif self.position[1] != feu[1]:
			self.position[1] += 1 if self.position[1] < feu[1] else -1	
		else:
			self.busy = 5
			board.liste_feux.remove(feu)
	def __repr__(self):
		return "Pompier : pos : {pos} busy: {busy}".format(
			pos=self.position,
			busy=self.busy
			)

if __name__ == "__main__":
    print("Je suis dans le module Pompier")