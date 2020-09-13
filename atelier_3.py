# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:51:43 2020
test github
@author: thomas
"""

#Import de la librairie random pour generer le jeu
import random

def plusoumoins():
    #création d'un nombre aléatoire pour jouer
    randomNomber = random.randint(0,100)
    #trigger, il arretera la boucle lorsque le jeu sera terminé
    finduJeu = False
    #sert de compteur de coup
    coup = 0

    #Prends en compte le trigger et le nombre de coup max
    while not (finduJeu) or (coup == 11):
        #entrée de l'input et comparaison
        #verification du résultat et renvoie d'une réponse adapté
        monNbr = int(input("Entrez en nombre: "))
        if (monNbr > randomNomber):
            print("trop grand")
        elif (monNbr < randomNomber):
            print ("trop petit")
        else:
            print ("Tu gagnes en "+str(coup)+"coup(s)")
            finduJeu = True
        #compteur de coup
        coup +=1
    if (coup > 10):
        print("perdu")
#plusoumoins()