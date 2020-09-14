# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:37:40 2020
@author: Duo Motbal
"""
import math

"""
Manque Exercice 4
Penser à un format de présentation pour la DocString et les fonctions
Faire la distinction entre chaque exercice
"""

"""
Les deux prochaines fonctions sont un calcul d'imc il suffit de rentrer un int correspondant
à votre imc afin de pouvoir vous dire dans qu'elle catégorie vous vous situés
Dans la version 1 vous trouverez les palier en dure alors que dans la version 2
un code bien plus propre avec des Constantes afin de rendre le code plus évolutif
"""
#EXO1
#VALEUR TEST 28 17 1 40 30
def calculImc(imc)->int:
    #Test en cascade, chaque test retire une possibilité
    #le test s'arrête dès que la valeur est trouvé
    if imc<16.5:
        value="FAMINE"
    elif imc < 18.5:
        value="maigreur"
    elif imc < 25:
        value="corpulence normale"
    elif imc < 30:
        value="surpoids"
    elif imc < 35:
        value="obésité modérée"
    elif imc < 40:
        value="obésité sévère"
    else:
        value="obésité morbide"
    return value

"""
Création de calcul IMC avec une boucle version plus propre...
"""
def calculImc2():
    #Création du tableau des résultats d'IMC ainsi que des bornes
    INDICES = ["famine","maigreur","corpulence normale","surpoid","obésité modérée","obésité sévère","obésité morbide"]
    IMC = (16.5,18.5,25,30,35,40)
    LEN_IMC=len(IMC)
    n=0
    founded=False
    try:   #verifie si l'utilisateur rentre un réel sinon il le renvoi sur le except
        imcUser=float(input("Veuillez entrer votre IMC : "))    #L'utilisateur rentre sont imc en réel
    except:
        print("Veuillez entrer un réel")
        
    while(not founded):
        if n+1>LEN_IMC:             #test si la liste n'est pas dépassée afin de passer l'indice sur obésité morbide
            resultat = INDICES[n]
            founded=True
            
        elif imcUser<=IMC[n]:   #test si il est plus petit que l'imc et si c'est le cas alors il renvoi l'indice
            resultat = INDICES[n]
            founded=True
        else:
            n+=1
    print(str(resultat))
            
def testImc():
    #Fait tourner la fonction d'IMC en changeant son paramètre pour le tester
    while 1:
        imc=int(input("Quel est votre IMC ? "))
        if str(imc)=="stop":
            break
        print(calculImc(imc))
#testImc()

def bissextile(annee:int)->bool:
    #Une année divisible par quatre est bissextile
    if annee % 4 == 0: """Manque de condition ne doit pas être divisible par 100)"""
        return True
    else:
        return False
def testBissextile():    
    #permet de reproduire le test a l'infini
    while 1 :
        print(bissextile(int(input('Quel année voulez vous tester'))))
#testBissextile()


def discriminant(a:float, b:float, c:float)->float:
    #Fonction de calcul de delta en insérant trois paramètres
    #Calcul de delta
    delta=(b*b)-4*a*c    
    return delta

def racine_unique(a:float,b:float)->float:
    #Si A est nul, l'opération ne peut être effectué, le calcul est donc annulé
    if a==0:
        print("Veuillez entrer un a différent de Zéro")
    else:
        x=-b/(2*a)
        return x

def racine_double(a:float, b:float, delta:float, num:float):
    #Fonction de résolution
    #Applique les formules appropriés en fonction du nombre de résultat possible
    if num==1:
        x= (-b + math.sqrt(delta)) / (2 * a)
    elif num==2:
        x=(-b- math.sqrt(delta)) / (2 * a)
    #renvoi la solution sous forme d'un float
    return x

def str_equation(a:float,b:float,c:float)->str:
    equation=str(a)+"x2"+str(b)+"x"+str(c)+"=0"
    return equation  """peux return directement et ne prend pas en compte les nombres négatifs """

def solution_equation(a,b,c):  
    delta=discriminant(a,b,c)
    if delta < 0:
        result="pas de racine réelle"
        #result="solution de l'équation " + str(a) + "+x2+" + str(b) + "+x+" + str(c) + "=0"
    elif delta==0:
        result="x1=" + racine_double(a,b,delta,1) + "x2=" + racine_double(a,b,delta,2)
    else:
        result=racine_unique(a,b)
        #result="-" + str(b) + str(math.sqrt(delta)) + "/2" + str(a) + " et 2x = -" + str(b) + str(math.sqrt(delta)) + "/2" + str(a)
    return result     

def test_solution_equation():  #a7 b4 c2 a5 b4 c2 A420 B48 C12
    while 1:
        a=float(input("veuillez entrer A : "))
        b=float(input("veuillez entrer B : "))
        c=float(input("veuillez entrer C : "))    
        if a==0:
            print('A = 0 n\'est pas possible')
            break
        else:
            print("la solution à l'équation est : " + str(solution_equation(a, b, c)))

                  
test_solution_equation()
