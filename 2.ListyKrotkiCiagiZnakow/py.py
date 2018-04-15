#!/usr/bin/env python3 
from sys import argv

#1
if len(argv) == 1:
	print("Nalezy podac startowe parametry")
else: 	
	s_string = ''.join(argv[1:])
	print(s_string)

#2
l_duze = [znak for znak in s_string if znak.isupper()]
l_male = [znak for znak in s_string if znak.islower()]
l_liczby = [znak for znak in s_string if znak.isdigit()]
l_notalpha = [znak for znak in s_string if not znak.isalpha()]

print(l_duze)
print(l_male)
print(l_liczby)
print(l_notalpha)

#3
l_male_bez_powtorzen = []

for znak in l_male:
	if znak not in l_male_bez_powtorzen:
		l_male_bez_powtorzen.append(znak)

print()
print(l_male_bez_powtorzen)

krotka_dwulementowa_4 = [(znak, l_male.count(znak)) for znak in l_male_bez_powtorzen]
print(krotka_dwulementowa_4)

#4
krotka_dwulementowa_4.sort(key = lambda x: x[1])
print()
print(krotka_dwulementowa_4)

#5	
# y=ax+b
a = len([znak for znak in s_string if znak in 'aAeEiIoOuUyY'])
b = -a + len(s_string) - len(l_notalpha)
print(a)
print(b)

krotka_dwulementowa_5 = [(float(cyfra), a* float(cyfra) +b) for cyfra in l_liczby] 
print(krotka_dwulementowa_5)

#6
x_sum = sum(cyfra[0] for cyfra in krotka_dwulementowa_5)
y_sum = sum(cyfra[1] for cyfra in krotka_dwulementowa_5)
x_srednie = x_sum / len(krotka_dwulementowa_5)
y_srednie = y_sum / len(krotka_dwulementowa_5)
D = sum(((cyfra[0] - x_srednie))**2 for cyfra in krotka_dwulementowa_5)
a = (1/D) * sum((y*(x-x_srednie)) for x,y in krotka_dwulementowa_5)
b = y_srednie - a*x_srednie

print()
print(D)
print(a)
print(b)
