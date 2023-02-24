import random

#GENERATE

goperators = ['+','-','*','/']
gside1 = '-10/3'
gside2 = '-10/3'
gside2a = 0
gside1a = None
numbers = 3
glst1 = []
glst2 = []


while(float(eval(gside1))%1 != 0 or float(eval(gside1)) < 0 or float(eval(gside1)) > 100):
    gside1 = ''
    for i in range(numbers):
        gside1 += (str(random.randrange(3,10)))
        gside1 += (str(goperators[random.randrange(0,4)]))
    gside1 = gside1[0:(numbers+(numbers-1))]
gside1a = (int(eval(gside1)))
#print(gside1)
#print('összeg:',gside1a)
    
while(gside2a != gside1a or gside1 == gside2):
    gside2 = ''
    for i in range(numbers):
        gside2 += (str(random.randrange(3,10)))
        gside2 += (str(goperators[random.randrange(0,4)]))
    gside2 = gside2[0:(numbers+(numbers-1))]
    gside2a = (int(eval(gside2)))
#print(gside2)
#print('összeg:',gside2a)
    
print('Problem to solve:')
for i in range(0,numbers*2,2):
    glst1 += gside1[i]
    print(gside1[i]+' ',end='')
print(' = ',end='')
for i in range(0,numbers*2,2):
    glst2 += gside2[i]
    print(gside2[i]+' ',end='')
print('\n')

input('Type anything here if you wanna see the right answer(s):' )

#SOLVE

#lst1 = ['8','4','6']
#lst2 = ['6','7','4']
#operators = ['+','-','*','/']
side1 = []
aside1 = []
side2 = []
aside2 = []
operator_variations = []

for i in range(4):
    str = goperators[i]
    for j in range(4):
        str2 = goperators[j]
        operator_variations += str
        operator_variations += str2
        
#SIDE 1
            
for j in range(0,32,2):
    mstr = ''
    mstr += glst1[0]
    mstr += operator_variations[j]
    mstr += glst1[1]
    mstr += operator_variations[j+1]
    mstr += glst1[2]
    aside1.append(mstr)
    side1.append(eval(mstr))
    #print(mstr)
    
#SIDE 2
  
for j in range(0,32,2):
    mstr = ''
    mstr += glst2[0]
    mstr += operator_variations[j]
    mstr += glst2[1]
    mstr += operator_variations[j+1]
    mstr += glst2[2]
    aside2.append(mstr)
    side2.append(eval(mstr))
    #print(mstr)
    
    
for i in range(len(side1)):
    for j in range(len(side2)):
        if side1[i] == side2[j]:
            print(aside1[i],'=',aside2[j])
            
            
#print(side1)  
#print(aside1)
#print(side2)
#print(aside2)