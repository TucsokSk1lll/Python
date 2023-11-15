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

print(Dobozok)