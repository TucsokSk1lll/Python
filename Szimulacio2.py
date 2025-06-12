import random

def szimulacio(szam,lst):
    legnagyobb = 0
    for i in range(0,szam):
        if lst[i] > legnagyobb:
            legnagyobb = lst[i]
    for i in range(szam,len(lst)):
        if lst[i] > legnagyobb:
            return lst[i]
    return lst[99]
    
atlag = []

def szamitas(kereses,hossz):
    lst2 = []
    for i in range(hossz):
        lst = []
        for j in range(hossz):
            lst.append(random.randrange(0,101))
        lst2.append(szimulacio(kereses,lst))

    osszeg = 0
    for i in lst2:
        osszeg += i
    print([kereses,osszeg/len(lst2)])
    atlag.append([kereses,osszeg/len(lst2)])

for i in range(1,101):
    szamitas(i,3000)

print(atlag)