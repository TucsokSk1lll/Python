import random 
lst = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]
rejtett_szo = lst[random.randrange(len(lst))]
stopp = False
guess = ''
tippelesek = 0

print(rejtett_szo)


while stopp != True and guess != rejtett_szo:
	guess = ''
	print('\n')
	tipp = input('Kérem a tippet: ')
	tippelesek += 1
 
	print('Az eredmeny: ',end='')
	if tipp == 'stop':
		break
	else:
		for i in range(len(tipp)):
			if(tipp[i] == rejtett_szo[i]):
				print(tipp[i], end=' ')
				guess += tipp[i]
			else:
				print('.',end=' ')
print('\n', tippelesek, 'tippelessel sikerult kitalalni.')
			

