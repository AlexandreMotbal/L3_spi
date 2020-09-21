"""

Module Description
Author : Jean-eric Mommeja, Alexandre Motbal
Date : 14/09/2020
Project : Atelier 5 l3-SPI
email : alexandre.motbal2@gmail.com, jean.mommeja@gmail.com

"""

import time
from random import * 
from typing import *
from Ex1 import *
import matplotlib.pyplot as plt 
import numpy as np 
#import os
liste1 = gen_list_random_int()
#f1 = mix
#f2 = shuffle
def perf_mix(f1:callable,f2:callable,list_tailles:list, nbtest:int) :
    tableau_f1 = []
    tableau_f2 = []

    for n in (list_tailles):
        temps_f1 = 0
        temps_f2 = 0
        for i in range(nbtest) :
            lst_test = gen_list_random_int(int_nbr = n, int_binf = randint(0,3), int_bsup = randint(3,250))

            temps_debut = time.perf_counter()
            f1(lst_test)
            temps_fin = time.perf_counter()
            temps_ecoule = temps_fin - temps_debut
            temps_f1 += temps_ecoule


            temps_debut = time.perf_counter()
            f2(lst_test)
            temps_fin = time.perf_counter()
            temps_ecoule = temps_fin - temps_debut
            temps_f2 += temps_ecoule
            
        moyenne_f1 = temps_f1/nbtest
        moyenne_f2 = temps_f2/nbtest

        tableau_f1.append(moyenne_f1)
        tableau_f2.append(moyenne_f2)

        print('------'+str(n)+'-----------------')
        print('temps de calcul général pour f1'+str(temps_f1))
        print('temps de calcul général pour f2'+str(temps_f2))
        print('')
        print('temps pour mix '+ str(moyenne_f1))
        print('temps pour shuffle '+ str(moyenne_f2))
        print('')

    return (tableau_f1 , tableau_f2)



Ttaille = [2,10,500]
tableauF = perf_mix(mix_list,shuffle, Ttaille,10)
print(tableauF)
fig, ax = plt.subplots()
#plt.xlabel('Evolution du temps de traitement en fonction de la méthode', color='g')
#plt.xticks(Ttaille, color='r')

ax.plot(Ttaille,tableauF[0],'bo-',label='f1')
ax.plot(Ttaille,tableauF[1],'r',label='f2')
plt.show()

#+++++++++++++++++++++++++++++++++++++++++++++++++++

#x_axis_list = np.arange(0,1000,)
#fig,ax = plt.subplots()
