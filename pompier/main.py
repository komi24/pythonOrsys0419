# -*- coding: utf-8 -*-


"""
    Les pompiers se déplacent d'une case par tour (gauche, droite, haut, bas).
    Il faut 5 tours pour effacer un feu à partir du moment ou le pompier arrive
    SUR la case du feu.
    Les pompiers peuvent se croiser
    Un seul pompier sur une case en feu
    
    CONSEILS : 
        - faire une classe Pompier, une classe Feu et une classe Manager
        - commencer par le cas un pompier et un feu
        - se déplacer simplement (d'abord selon un axe puis selon l'autre)
"""

import time
import os

# from MonPackage.MonModule import sayHi
#from MonPackage.BoardManagerUI import BoardManagerUI
from MonPackage.BoardManager import BoardManager

# bm = BoardManagerUI()
bm = BoardManager()

#while bm.liste_feux	:
#	os.system('cls')
#	bm.run()
#	bm.display()
#	time.sleep(0.6)
#	print(bm.liste_pompiers)


