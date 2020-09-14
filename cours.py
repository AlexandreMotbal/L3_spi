for i in range(4):
    print(str(i))

print('---------------------------------------------')
n=0
while n<4:
    print(str(n))
    n = n + 1

print('--------------------------------------------')

v = "Bonjour toi"

while n < len(v):
    n = n +1
print(n)

print('--------------------------------------------')
import random

MIN = 0
MAX = 100
NUMBER = random.randint(MIN,MAX)
trigg = False
defeat = False
cpt = 0
while trigg != True:
    x = int(input('Entrez un chiffre : '))
    if x == NUMBER:
        print('Vous avez gagner')
        trigg=True
    elif x > NUMBER:
        print('C\'est moins')
    else:
        print('C\'est plus')
    cpt = cpt+1
    if cpt == 10:
        print('Defeat')
        trigg = True

