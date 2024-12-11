tokeletes_szamok = []
for i in range(1,100001):
    osztok = []
    for j in range(1,i):
        if i%j == 0:
            osztok.append(j)
    osszeg = 0
    for k in range(0,len(osztok)):
        osszeg += osztok[k]
    if osszeg == i:
        tokeletes_szamok.append([i,osztok])
    print(i,osztok)
print(tokeletes_szamok)