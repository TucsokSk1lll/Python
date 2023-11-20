lst = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
Dobozok = []
osszesen = 0
Doboz = 0

while lst != []:
	
	if Doboz + lst[0] <= 20:
		Doboz += lst[0]
		lst.remove(lst[0])
		#print(Doboz)
		#print(lst)
		
	else:
		Dobozok.append(Doboz)
		Doboz = 0
  
if Doboz > 0:
		Dobozok.append(Doboz)
		Doboz = 0

for i in range(len(Dobozok)):
    osszesen += Dobozok[i]
print('2. feladat')
print('A targyak tomegenek osszege:',osszesen,'kg')
print('\n')
print('3. feladat')
print('A dobozok tartalmanak tomege (kg): ',end='')
for i in range(len(Dobozok)):
    print(Dobozok[i],end=' ')
print('\n')
print('Szukseges dobozok szama:',len(Dobozok))
