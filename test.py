"""
Equipe Motbal
Née 06/09/2000

"""

# Exo 1#
def calcSal():
    salaireFinal=0
    nbHeure=0
    salaire=0
    mult=1
    nbHeureSup50=0
    salaire=int(input('Salaire horaire :'))
    nbHeure=int(input('Nombre d\'heures svp :'))
    if nbHeure<0:
        print("Veuillez rentrer un nombre d'heure cohérent")
    else:
        if nbHeure>=200:
            mult=1.50
            nbHeureSup50 = nbHeure-200
            salaireFinal = salaireFinal + mult * (nbHeureSup50 * salaire)
        if nbHeure>=160:
            mult=1.25
            nbHeureSup25 = nbHeure-160-nbHeureSup50
            salaireFinal = salaireFinal + mult * (nbHeureSup25 * salaire)
            salaireFinal = salaireFinal + 160* salaire
        else:
            salaireFinal = nbHeure * salaire
            

    salaireFinal = str(salaireFinal)
    print("Votre salaire après ajout prime heure sup :" + salaireFinal)
        
#calcSal()

# Exo 2#
def upperOrLower():
    maLettre = input('Entrez un caractère')
    valeurAscii = ord(maLettre[0])
    if valeurAscii >=97 and valeurAscii <= 122:
        print('Minuscule')
    elif valeurAscii >=65 and valeurAscii <= 90:
        print('Majuscule')
    elif valeurAscii >= 48 and valeurAscii <=57:
        print('Chiffre')
    else:
        print('caractère spécial')

#upperOrLower()

#EXO 3#
def impot():
     genre = input('êtes vous un homme une femme ?')
     age = int(input('Votre age SVP'))
     if genre == "homme" and age <= 20:
         print("IMPOSABLE")
     elif genre == "femme" and age >= 18 and age <=35:
         print("imposable")
     else:
         print ("NON IMPOSABLE")

 #impot()

#projet abandonné
def facture():
    nbCopie = int(input('Nombres de copies'))
    if nbCopie < 10:
        nbCopie * 0.10
    if nbCopie > 10:
        prix=(nbCopie-10)*0.09
        prix+= 10*0.10
    if nbCopie > 30:
        prix = prix + nbCopie-30 * 0.08
    print(prix)

#facture()
##   

#EXO4     
def reproPrix():
    quantite = int(input('Veuillez indiquez une quantitée: '))
    valeur = 0
    #prix 10 première 0.10
    #prix 20 suivante 0.09
    #prix suivante 0.08

    if quantite<=10:
        valeur = quantite * 0.10
    elif quantite<30:
        valeur = 10*0.10 + (quantite-10)*0.09
    else:
        valeur = 10*0.10 + 20*0.09+ (quantite-30)*0.08
    print(valeur)

#reproPrix()   
#Exo5 de thomas
def fraisPort():
    nom = input('Nom du voilier capitaine !')
    long = int(input('La longueur ?'))
    categorie = int(input('Et la catégorie ?'))
    if long < 5:
        place= 100*12
    elif long >= 5 and long <= 10:
        place= 200*12
    elif long > 10 and long <= 12:
        place= 400*12
    else:
        place = 600*12
    if categorie == 1:
        taxe=100
    elif categorie == 2:
        taxe = 150
    elif categorie == 3:
        taxe = 250
    else:
        print("Mauvaise catégorie captain !")
    prixtotal = place + taxe
    prixtotal = str(prixtotal)
    nom = str(nom)
    print("Je précise que le prix de la place pour votre " + nom + " est de : " + prixtotal + "€" )
    
#fraisPort()

#Exo5 d'alexandre

def bateau():
    nom = input('Veuillez saisir un nom pour votre beau bateau :')
    longueur = int(input('saisie la taile de votre bateau :'))
    categorie = int(input('Saisir la categorie de votre bateau (1 2 3) :'))
    prix = 0
    if longueur < 5:
        prix = prix +100
    elif longueur<=10:
        prix =prix +200
    elif longueur<=12:
        prix =prix +400
    else:
        prix =prix +600


    prixAnnuel = 12 * prix


    if categorie == 1:
        prixAnnuel =prixAnnuel +100
    elif categorie == 2:
        prixAnnuel =prixAnnuel +150
    elif categorie == 3:
        prixAnnuel =prixAnnuel +250
    else:
        print('Il y a une erreur de la catégorie')


    print('Le coût annuel d\'une place au port pour le voilier'+ nom +'est de '+ str(prixAnnuel))

#bateau()
#EXO 6
def automobile():
    carburant=input("Veuillez indiquer par D ou E si c'est une diesel ou une essence :")
    cylindre=int(input("Pouvez-vous nous indiquez le cylindre de la voiture :"))
    km=int(input("Combien de km parcourez-vous à l'année :"))


    conso=0
    if cylindre >= 2000 and carburant=="E":    
        essence=float(input("Prix de l'essence : "))
        conso=10
        prix=conso*essence*1.50                       #impact du surcout lié à l'entretien

    elif cylindre < 2000 and carburant=="E":
        essence=float(input("Prix de l'essence : "))
        conso=7
        prix=conso*essence*1.50                     #impact du surcout lié à l'entretien
    elif carburant=="D":
        diesel=float(input("prix du diesel"))
        conso=8
        prix=conso*diesel*1.70
    else:
        print("Veuillez entrer un Carburant ou un nombre de cylindre valide.")
    prix=prix/100*km
    prix=prix/12
    km=str(km)
    prix=str(prix)
    print("Vous avez un coût " + prix + " € au " + km + "km par mois")

#automobile()


#EXO7
def elec():
    candid1=int(input("Quel est sont score ?"))
    candid2=int(input("Quel est sont score ?"))
    candid3=int(input("Quel est sont score ?"))
    candid4=int(input("Quel est sont score ?"))
    if candid1 > 50:
        print("le candidat 1 est vainqueur")
    elif candid2 > 50:
        print("le candidat 2 est vainqueur")
        print("le candidat 1 a PERDU A")
    elif candid3 > 50:
        print("le candidat 3 est vainqueur")
        print("le candidat 1 a PERDU A")
    elif candid4 > 50:
        print("le candidat 4 est vainqueur")
        print("le candidat 1 a PERDU A")
    elif candid1 > 12.5:
        print("Peut participer au second tour")
    

#elec()
# façon alex
def election():
    candidat = [1,2,3,4]
    candidatSecond =[]
    gagnant = -1
    for n in range (0,4):
        numCandidat = n+1
        candidat[n] = int(input('Veuillez saisir les scores du candidat'+str(n+1)+' '))
        if candidat[n]>50:
            gagnant = n+1
        elif candidat[n]>12.5:
            candidatSecond.append(n+1)
        n=+1

    #Test résultat du candidat 1
    if gagnant != -1:
        print('Le candidat '+ str(gagnant)+' a gagné')
        if gagnant !=1:
            print('De fait le candidat 1 a perdu')
    else:    
        if candidat[0]>50:
            print('Le candidat 1 a gagné')
        elif candidat[0]>12.5:
            print('Le candidat 1 est en ballotage favorable, il participe au second tour!')
        else:
            print('Le candidat 1 est vaincu!')

#election()
