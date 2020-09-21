"""
Module Description
Author : Jean-eric Mommeja, Alexandre Motbal
Date : 14/09/2020
Project : Atelier 5 l3-SPI
email : alexandre.motbal2@gmail.com, jean.mommeja@gmail.com

"""


from random import *
from typing import *

def gen_list_random_int (int_nbr = 10, int_binf = 0, int_bsup = 10)->list :
    """
    gen_list_random_int return a list,
    there is 3 parameters, the size (int_nbr), the minimum (int_binf)
    and the max(int_bsup) the first parameters is the size of the list,
    by default the size is on 10, int binf determined the inferior limits
    and the int_bsup is the opposite to int_binf
    """ 
    list_Rdm = []
    for n in range(int_binf, int_nbr+1):
        val=randint(int_binf , int_bsup-1)
        list_Rdm.append(val)

    return list_Rdm
print(gen_list_random_int(6,1,50))

#ex2
def mix_list (list_to_mix:list)->list:
    """mix_list is a shuffle function, use it to mix randomly the value of a list
    mix_list got one parameter:list_to_mix, this is the list to mix
    mix list return the list put in parameters but shuffled
    """
    ma_liste = list_to_mix[:]

    for i in range(0,len(ma_liste)):
        rng =randint(0,len(ma_liste)-1)
        ma_liste[i], ma_liste[rng] = ma_liste[rng] , ma_liste[i]
        
    return ma_liste

listvide=[]
la_liste = [1,2,3,4,5,6,7,8,9]
print(mix_list(la_liste))

#ex3
def choose_element_list (list_in_wich_to_choose:list)->any:
    """
    choose_element_list return a random element, from a list
    in paramaters
    """
    val = randint(0,len(list_in_wich_to_choose)-1)
    value_to_return = list_in_wich_to_choose[val]

    return value_to_return
print(choose_element_list(la_liste))

#ex 4
def extract_element_list(list_in_wich_to_choose:list,int_nbr_of_element_to_extract:int)-> list:
    """extract_element_list, create a list with random elements
    parameters:
        list_in_wich_to_choose: put a list to choose the elements
        int_nbr_of_element_to_extract : select the size of the list
    """
    list_Rdm=[]
    for i in range (0,int_nbr_of_element_to_extract) :
        val = randint(0,len(list_in_wich_to_choose)-1)
        list_Rdm.append(list_in_wich_to_choose[val])
        #Faire le Pop 
    return list_Rdm
print (extract_element_list(la_liste , 8))

