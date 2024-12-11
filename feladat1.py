import random #ez csak arra kell, hogy a random számokat tudjunk majd generálni mert ezt a sima python nem tudja így hozzá kell adni

lista = [] #ebbe a listába fogjuk majd a random számokat tenni

for i in range(10): #az ez alatt lévő beljebb kezdett dolgokat 10-szer megcsinálja a program
    lista.append(random.randint(200, 500)) #a random számokat 200 és 501 között generáljuk (mivel az intervallum )

print(lista) #kiírjuk a listát
print(max(lista)) #kiírjuk a legnagyobb számot a listában
print(min(lista)) #kiírjuk a legkisebb számot a listában
