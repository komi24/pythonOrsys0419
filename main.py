# -*- coding: utf-8 -*-

#from MonPackage.MonModule import dire_bonjour 
# from AutrePackage.AutreModule import say_hi
from AutrePackage import AutreModule 

import MonPackage
import numpy

MonPackage.MonModule.dire_bonjour()
AutreModule.say_hi()

print(numpy.array([1,2]))
a = numpy.array([1,2])

fichier = open("mon_fichier.txt", "a")
fichier.write("Hello")
fichier.close()

with open("mon_fichier.txt", "r") as f:
    print(f.read())
    
import csv

a += 1

with open("tableur.csv", "w") as f:
    writer = csv.DictWriter(f, ['nom', 'prenom'])
    writer.writeheader()
    writer.writerow({'nom': 'Bolnet', 'prenom': 'Mickael'})
    