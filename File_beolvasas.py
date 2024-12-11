x = open(file="C:\\Users\\gyo.joz.2008.01.TAG\\Documents\\webpage\\Kozep_szintu_erettsegi_py\\tomeg.txt", mode="r", encoding="utf-8")
x = x.read()
x =  x[0:len(x)-1]
lst = x.split(', ')
print(lst)