x = open(file='C:\\Users\\jgyor\\OneDrive\\Dokumentumok\\GitHub\\Python\\naplo.txt',mode='r',encoding="utf-8")
x = x.read()
#print(x)

lst = x.split('\n')

print(lst)

bejegyzesek = 0

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 'X' or lst[i][j] == 'O' or lst[i][j] == 'I' or lst[i][j] == 'N':
            bejegyzesek += 1
            break

print('2. feladat')
print('A naplóban',bejegyzesek,'bejegyzés van.')


igazolt = 0
igazolatlan = 0

for i in range(len(lst)):
    space = 0
    for j in range(len(lst[i])):
        if lst[i][j] == ' ':
            space += 1
        elif lst[i][j] == 'X' and space == 2:
            igazolt += 1
        elif lst[i][j] == 'I' and space == 2:
            igazolatlan += 1

print('3. feladat')
print('Az igazolt hianyzasok szama ' + str(igazolt) + ', az igazolatlanoke',igazolatlan,'óra.')
            

def hetnapja(honap, nap):
    abszolut_nap = 0
    napok = ['vasarnap','hetfo','kedd','szerda','csutortok','pentek','szombat']
        
    while(honap != 1):
        if(honap == 3):
            abszolut_nap += 28
        elif(honap % 2 == 1):
            abszolut_nap += 30
        elif(honap % 2 == 0):
            abszolut_nap += 31

        honap -= 1

    abszolut_nap += nap
    
    #print(napok[abszolut_nap % 7])
    #print(abszolut_nap)
    
    return napok[abszolut_nap % 7]

print('5. feladat')
print(hetnapja(int(12),int(31)))

print('6.feladat')
nap = 'szerda'
sorszam = 3
xdhianyzas = 0


for i in range(len(lst)):
    if lst[i][0] == '#':
        if hetnapja(int(lst[i][3:4]),int(lst[i][5:7])) == nap:
            print(int(lst[i][3:4]),int(lst[i][5:7]))
            print(hetnapja(int(lst[i][3:4]),int(lst[i][5:7])))
            while lst[i+1][0] != '#':
                print([len(lst[i+1]) - (7 - sorszam + 1)])
                if lst[i+1][len(lst[i+1]) - (7 - sorszam + 1)] == 'X' or lst[i+1][len(lst[i+1]) - (7 - sorszam + 1)] == 'I':
                    xdhianyzas += 1
                    print(' hanyzasok szama:',xdhianyzas)
                i += 1

print('hianyzas:',xdhianyzas)
