def bissextile(annee:int):
    #Test pour savoir si l'année est bissextile
    if annee % 4 == 0:
        res = True
    #si elle n'est pas bissextile
    else:
        res = False 
    #renvoi de la solution
    return res


def date_est_valide(jour:int,mois:int,annee:int):
    #Test pour savoir si c'est un mois en 30 ou 31
    #Si est un jour en un mois pair ou juillet aout ou bissextile
    if mois %2 == 1 or mois !=7 or mois != 8 :
        moisMax = 30
    #si mois de février
    #Test pour savoir si le mois de février sera long ou court
    elif mois == 2:
        if bissextile(annee):
            moisMax = 30
        else:
            moisMax = 28
    #Dans tous les autres cas (mois en 31)
    else:
        moisMax = 31

    if mois > 12 or mois < 0:
        return print('error')

    if jour>moisMax or jour<0:
        return print('error')
    
    else:
        return 1

def saisie_date_naissance():
    #Saisie de la date de naissance
    j = int(input('Saisir le jour'))
    m = int(input('saisir le mois'))
    a = int(input('saisir année'))
    #Test  
    if date_est_valide(j,m,a):
        dateValide = [j,m,a]
        return dateValide
    
def age(date_naissance):
    age = 0
    print('il va falloir nous donner la date')

    year = int(input('Veuillez saisir l\'année'))
    month = int(input('Veuillez saisir le mois'))
    day = int(input('Veuillez saisir le jour'))
    
    age = year - date_naissance[2]

    if date_naissance[1]> month:
        age =+1
    
    elif date_naissance[1]== month and date_naissance[0]>day:
        age =+1
    
    return age

#age(saisie_date_naissance())
def est_majeur(date_naissance):
    if age(date_naissance) >= 18:
        return True
    else:
        return False

def test_acces():
    date_naissance = saisie_date_naissance()
    if est_majeur(date_naissance):
        print('Bonjour vous avez'+str(age(date_naissance))+'Vous pouvez passer')
    else:
        print('Bonjour vous avez'+str(age(date_naissance))+'Vous ne pouvez pas passer')

test_acces()