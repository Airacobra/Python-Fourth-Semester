#!/usr/bin/env python3 

#1
def ifPalindrom(number):
	return str(number)[::-1] == str(number)

print(ifPalindrom(454))
print(ifPalindrom(723,),'\n\n')


#2
import random
counter = 0
s2 = {}

while counter < 100:
	number = random.randrange(100, 10001)
	if number not in s2:
		s2[number] = ifPalindrom(number)
		counter += 1

print(s2,'\n\n')

#3
newList3 = [random.randrange(0,20) for _ in range(0,100)]
sParzyste = {}
sNieparzyste = {}
for index, value in enumerate(newList3):
	if index % 2 == 0:
		sParzyste.setdefault(index,[]).append(value)
	else:
		sNieparzyste.setdefault(index,[]).append(value)

print(sParzyste,'\n')
print(sNieparzyste,'\n')

rozstep = max(sParzyste) - min(sParzyste)
mediana = 0
##lParzyste = [sParzyste[i] for i in sParzyste]
##if len(lParzyste) % 2 == 0:
##	mediana = (lParzyste[len(lParzyste)//2] + lParzyste[len(lParzyste//2)-1])/2
##else:
##	mediana = lParzyste[len(lParzyste)//2]
	

#s3 = {key : (,) for key in sParzyste}
print('\n\n')

#4
s4 = {}
from sys import argv
if len(argv[:]) > 1:
	s4 = {k : random.randrange(2,15) for k in range(int(argv[1]))}
	newList4 = [(value, key) for key, value in s4.items()]
	s4ButReverse  = {s4[key] : key for key in s4}
	print(s4)
	print(newList4)
	print(s4ButReverse,'\n\n')

#5	
s5 = {}
newList5 = [random.randrange(0,11) for _ in range (10)]

s5 =  { index : [] for index in range(0,11)}
currentIndex = 0
for j in newList5:
    s5[j].append(newList5.index(j, currentIndex))
    currentIndex+=1

print(newList5)
print(s5,'\n\n')

	
#6
di1 = {index : random.randrange(1,100) for index in range(10)}	
di2 = {index : random.randrange(1,100) for index in range(10)}
di3 = {}

print(di1)
print(di2,'\n')
di1 = {value : key for key, value in di1.items()}
di2 = {value : key for key, value in di2.items()}
print(di1)
print(di2)

di3 = {key:(di1[key],di2[key]) for key in di1 if key in di2}
print(di3)