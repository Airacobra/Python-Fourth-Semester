print('---------1----------')


def Fibonacci():
	i = 0
	j = 1
	while True:
		yield i
		i,j = j,j+i

def Parzyste_Nieparzyste(n, czy_parz = True):
	if czy_parz:
		for i in n:
			if i%2:
				yield i
	else:
		for i in n:
			if not i%2:
				yield i
				
def CzyWieksze(n, m):
	for i in n:
		if i <= m:
			yield i
		else:
			return	

print('parzyste: ', sum(list(Parzyste_Nieparzyste(CzyWieksze(Fibonacci(), 100), 1))))
print('nieparzyste: ',sum(list(Parzyste_Nieparzyste(CzyWieksze(Fibonacci(), 100), 0))))

print('---------2----------')

def myrange(poczatek, koniec = None, krok = 1.0):
	if koniec == None:
		i = 0
		while poczatek > i:
			yield i
			i += krok
	else:
		if krok == 0:
			return
		elif krok > 0:
			while poczatek < koniec:
				yield poczatek
				poczatek += krok
		else:
			while poczatek > koniec:
				yield poczatek
				poczatek += krok		

print(list(myrange(30, 5, -2.5)))				
					
print('---------3----------')
from random import *

def n_fun():
	n_next = 0
	n_poprzednie = random()

	while True:
		n_next = random()
		if abs(n_next - n_poprzednie) >= 0.4:
			yield round(n_next,2)
		if n_next < 0.1:
			return

print(list(n_fun()))
			 
print('---------4----------')

def r_ciag(N):
	r_ciag = [randint(0,1) for _ in range(N)]
	return r_ciag

l = r_ciag(30)
print('Losowy ciag:', l)	

def r_fun(l):
	counter = 0
	for number in l:
		if number:
			if counter:
				yield counter
				counter = 0
		else:
			counter += 1

l_2 = list(r_fun(l))
print('Srednia odleglosc: ', sum(l_2)/ len(l_2))

print('---------5----------')


def rozmien(kwota):

	nominaly = [1, 2, 5, 10, 20,  50, 100, 200]
	l = [1000 for _ in range(kwota + 1)]
	l[0] = 0

	for i in range(len(nominaly)):
		temp = []
		for j in range(kwota + 1):
			if nominaly[i] > j:
				temp.append(l[j])
			else:
				temp.append(min(l[j], 1 + temp[j - nominaly[i]]))	
		l = temp
		yield l			

print(list(rozmien(54)))





