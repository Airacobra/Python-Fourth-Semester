#!/usr/bin/env python3  #interpreter

print ('Hello world!') #python3 musi miec nawiasy dla print

s = 'a'         
print(type(s))  
s = "a" 
print(type(s))	

# komentarze jednowierszowe
""" komentarz wielowierszowy, 
tylko w stytuacjach awaryjnych
(tworzy obiekt typu string) """

s = 1
print(type(s))
s = 1.
print(type(s))

import keyword 		   #importuijemy modul
#print(keyword.kwlist) #wypisuje slowa kluczowe

import math
print(math.sqrt(7))

from math import sqrt
print(sqrt(7))

#from cmath import sqrt as csqrt #zamieniamy nazwe aby nie nadpisac powyzszego imprth sqrt


#print(dir(math)) #dir wypisuje zawartosc modulu
#print(help(math.modf)) #help wypisuje opis 
#tuple - krotka  

# ** - potega
print(2/3) #wynik zalezy od wsrji python2 - 0, python3 - 0,(6)
print(2//3) # 0 w python3
#from __future__ import division

print(abs(-4)) #zwraca zadany int lub float, usuwa -
print(math.fabs(-4)) #zwraca float, usuwa -
print(math.hypot(10,15)) #Return the Euclidean distance, sqrt(x*x + y*y).
print(pow(2,3,4)) #a^ (b mod c)

a=7
b=3
a,b = 7,3
a,*b = 7,3,'a',4 #b ma parę parametrów
print(a)
print(b)

a,b = b,a
print(a)
print(b)

print(type(())) #nawiasy okrągle stosowane w arytmetyce, funkcjach, oraz do definiowania krotki
print(type((1))) #int
print(type((1,))) #krotka jedno-elementowa

#krotka jest niemodyfikowalna (), lista tak[]
k = (1,2.,'a',[1,2,3]) #indeksowane od 0
print(k)
#k[3] = 5 krotke nie mozna modyfikowac
k[3][0] = 5 # element krotki jest modyfikowalny 
print(k)

k = (1,2.,'a',[1,2,3]) 
print(type(k))
k = [1,2.,'a',[1,2,3]]
print(type(k))

a = [1,2.,'a',[1,2,3]]
b =  [1,2.,'a',[1,2,3]]
a.append([1,2,3]) #dodaje do listy argument [1, 2.0, 'a', [1, 2, 3], [1, 2, 3]]
b.extend([1,2,3]) #wyjmuje poszczegolne elementy i roszerza nimi liste [1, 2.0, 'a', [1, 2, 3], 1, 2, 3]
print(a)
print(b)

print(len(k)) #dlugosc tablicy, ostatni element ma indkes len(k)-1 lub -1
#a = k tworzy referencje
#a = k[:] - tylko kopiujemy od do ostatniego elementu ktorego nie chcemy (nie do konca, tylko dla jednowymiarowej)
l = k[:] # kopiuje wszystko
#l[0] = 7  #ok
#l[-1][0] = 'b' #zmieni oryginał, bo schodzimy nizej
print(l)
print(k)

from copy import deepcopy #do kopiowania
l = deepcopy(k)
l[0] = 7  
l[-1][0] = 'b'
print(l)
print(k)

l2 = [0] * 20 #iteral liczbowy
print(l2)
l2[3] = 'a' #pojawi sie tylko na 4 pozycji
print(l2)

l3 = [[]] * 20
print(l3)
l3[3].append('a') #zmienie kazdy element na 'a'
print(l3)

#funkcja id() - pokazuje czy obiekty mają ten sam adres

l4 = [[] for _ in range(20)] # dodajemy do listy argument pętlą 20 razy, nie wykorzystujemy zmiennej, więc piszemy _ 
print(l4) # ^ pisac tak jesli mozna, bo szybciej i lepiej!

#w pythonie piszemy tak jak mowimy 
# c++ - a = warunek ? T : F
# python - a = T if warunek else F

#if war1:       jezeli warunek jest
#elif war2:		prosty to nie dajemy
#else 			nawiasow

"""
#rownianie kwadratowe
import 
#a = float(input("a: "))
#b = float(input("b: "))
#c = float(input("c: "))

from sys import argv # do wczytywania z klawiatury
#a = float(argv[1])
#b = float(argv[2])
#c = float(argv[3])

delta = math.sqrt(b**2 - 4*a*c)
if delta > 0: 
	wynik1 = ((-b - delta)/(2.*a))
	wynik2 = ((-b - delta)/(2.*a))
	print(wynik1)
	print(wynik2)			
else:
	wynik = b / (2*a)
	print(wynik)
"""

k = [1,2,3,4,5]
for i in k:
	i += 3 # nie zmienie wartosci przy iteracji 
print(k)

for i in range(len(k)):
	k[i] += 3
print(k)

k = [(1,2),(3,4),(5,6)]
for i,j in k:
	print(i,j)	

l5 = [(1,2),(3,4),(5,6)]
for i,j in l5:
	if(i > j):
		break
	else: 	#wykona sie po petli raz?
		print(i,j)	

#range(10) od 1 do 10
#range(2,10) od 2 do 10
#range(2,10,3) trzeci argument to krok
#range(10,2)  blad	
#range(20,2,-1)	od 10 do 2 z krokiem -1	