import time
m = 1200001540.0 #szán kezdeti tömege
Houses = 5100000000 #összes házaknak a darab száma
Houses2 = 0 #hány ház mellett ment el eddig a mikulás
s = 117000000 #összes út amit meg kell tennie a mikulásnak 
F1 = 0 #rénszarvasok összereje
V0 =20.0 #F1[0]*2/0,25/1,27/15 #kezdeti sebesség 
s2 = 0.0 #két ház közötti út 
t = 0 #összes idő 
t2 = 0 #két ház közötti távolsáég megtételéhez szükséges idő

for i in range(100000):
    while(t < 111600):
        t2 += 0.01
        t += 0.01
        Houses3 = Houses2//1
        Houses2 = s2//20
		
        if Houses2-1 == Houses3:
            m = m-Houses2*4,5*3
            V0 = V0 + F1*(t-t2)/m
            s2 = s2 + V0 * t2
			
            t2 = 0 #mindig a legvégén
		
        if Houses2 == 0:
            s2 = V0*t
         


