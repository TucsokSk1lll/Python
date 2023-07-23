import random
# - - - G E N E R Á L Á S - - -

Megoldás = -1

#Generáljunk egy feltételt ami kiszűri a negatív, a nullával egyenlő és a tört eredményeket. 

while Megoldás != Megoldás//1 or Megoldás != abs(Megoldás) or Megoldás == 0:

	Megoldás = -1
	# Egy listába generáljunk n db pozitív egész számot [2;9] intervallumon, ezeket tároljuk el listában. A listában nem lehet 2 megegyező érték. (Ezt azért kell végrehajtani hogy megakadályozzuk hogy több féle képpen is meg lehessen oldani az egyenletet)

	Paraméter = 3 #input()
	Számok = []
	Lehetséges_számok = ['2','3','4','5','6','7','8','9']
	for i in range(Paraméter):
		x = Lehetséges_számok[random.randrange(len(Lehetséges_számok))]
		Számok.append(x)
		Lehetséges_számok.remove(x)
	#print(Számok)

	# Egy másik listába generáljunk n-1 db véletlenszerű operátort, Nem lehet 2 ugyan olyan operátor és nem lehet + és - egyszerre . (Ezt azért kell végrehajtani hogy megakadályozzuk hogy több féle képpen is meg lehessen oldani az egyenletet)

	Operátorok = []
	Lehetséges_operátorok = ['+', '-', '*', '/']
	Nem_megfelelő_operátorpárok = [['+','-'], ['-','+'], [ ]]

	while(Operátorok == Nem_megfelelő_operátorpárok[0] or Operátorok == Nem_megfelelő_operátorpárok[1] or Operátorok == Nem_megfelelő_operátorpárok[2]):
		Operátorok = [ ]
		for i in range(Paraméter-1):
			x = Lehetséges_operátorok[random.randrange(len(Lehetséges_operátorok))]
			Operátorok.append(x)
			Lehetséges_operátorok.remove(x)
	#print(Operátorok)

	# Az egyenletnek megfelelően fűzzük össze a két lista elemeit.

	Egyenlet = ''

	while Számok != []:
		Egyenlet += Számok[0]
		Számok.remove(Számok[0])
		if Operátorok != []:
			Egyenlet += Operátorok[0]
			Operátorok.remove(Operátorok[0])
	#print(Egyenlet)
	Megoldás = eval(Egyenlet)
	print(Megoldás)

Megoldás = int(Megoldás)
print(Egyenlet)
print(Megoldás)

# - - - M E G O L D Á S - - -

# Az egyenleteket végezzük el, ha 2 egyenletre nem kapunk egyenlő értéket, akkor az eredményt tároljuk el egy változóban. 

# Hozzunk létre ugyan ilyen egyenleteket egészen addig amíg az egyik eredménye nem lesz ugyan annyi mint az első egyenleté.

# Ha a kettő egyenlet tényezői nem egyeznek meg akkor írjuk ki a kettő egyenletet operátorok nélkül.

