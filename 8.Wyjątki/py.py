import os
from glob import glob
from types import FunctionType	

class Wyjatek(Exception):
	pass	

print('------------1-------------\n')
def fun1(*n):
	for numer in n:		
		if not isinstance(numer, (int, float)):
			raise Wyjatek('Nie wszystkie parametry sa liczbami')
	for i in range(1, len(n) - 1):
		if n[i] < n[i-1]:
			raise Wyjatek('Liczby nie sa posortowane')

	if len(n)%2:
		return (n[len(n)//2 - 1] + n[len(n)//2+1])/2
	else:
		return n[len(n)/2]		

try: 
	print(fun1(1,3,2,4,5,6,7,8,9))
	print(fun1(1,2,3,4,5,6,'a',8,9))
	print(fun1(1,2,3,4,5,6,7,8,9))	

except Wyjatek as error:
	print(error)


print('------------2-------------\n')

def fun2(function, start, end, n):
	if not isinstance(start, (int, float)):
		raise Wyjatek('Nie wszystkie parametry sa liczbami')
	if not isinstance(end, (int, float)):
		raise Wyjatek('Nie wszystkie parametry sa liczbami')	
	if not isinstance(n, (int, float)):
		raise Wyjatek('Nie wszystkie parametry sa liczbami')
	if not isinstance(function, FunctionType):
		raise Wyjatek('Nie przekazano funkcji')	
	if end < start:
		raise Wyjatek('Zle parametry, wartosc konca jest wieksza niz poczatku')	
	if n < 0:	
		raise Wyjatek('Krok jest ujemny')

	step = (end - start) / n
	pole = 0
	i = start

	while i < end:
		pole = pole + function(i) * step	
		i += step
	return pole		

try:
	print(fun2(lambda x: x**2, 5, 15, 10000))

except Wyjatek as error:
	print(error)



print('------------3-------------\n')

def fun3(elementy, n):
	if len(elementy)%n:
		raise Wyjatek('Rozmiar listy sie nie zgadza')
	ifTrue = True
	krok = 0
	parzyste = 0
	nieparzyste = 0
	potegi = 0
	while krok < len(elementy) - 1 - n:
		for i in range(n-1):
			if elementy(i - krok) > elementy[n + krok -1]:
				raise Wyjatek('Ostatnie liczba nie jest najwieksza')
			if (elementy[i - 1] % 2 == 1):
				nieparzyste += 1
			else:
				parzyste += 1
			potegi += elementy[krok + i] ** 2

		if (elementy[n + krok - 1] % 2 == 1):
			nieparzyste += 1
		else: 
			parzyste += 1 	

		if potegi != elementy[n + krok - 1] ** 2:
			ifTrue = False

	return ifTrue					

l_1=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l_2=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
l_3=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l_4=(3,4,5,5,13,12,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)	

try:
	print(fun3(l_1, 4))

except Wyjatek as error:
	print(error)

print('------------4-------------\n')

def aver(nazwa):
	if os.access(nazwa, os.R_OK):
		file = open(nazwa)
		temp = []
		wiersze = file.readlines()
		
	try:
		
		if len(wiersze) == 0:
			raise Wyjatek('Plik jest pusty')
		for wiersz in wiersze:
			wiersz = wiersz.rstrip()
			cyfry = wiersz.split("\t")
			for cyfra in cyfry:
				if not cyfra.isdigit():
					raise Wyjatek('Cos nie jest cyfra')
				if len(cyfry) != 2:
					raise ArithmeticError('Problem z kolumnami')
				temp.append(int(cyfry[0]))
				temp.append(int(cyfry[1])) 	

				with open('wynik.dat', 'w') as saveToFile:
					saveToFile.write(str(sum(temp)/ len(temp)) + '\n')

	finally:
		file.close()

for file in glob('*.dat'):
	try:
		print(aver(file))
	except Wyjatek as error:
		print(error)
	except ArithmeticError as error:
		print(error)						