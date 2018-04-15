from random import *

def pierwsza(a):
	slownik = {}
	for i in range(randrange(0,20)):
		k = random()
		slownik[k] = '{:.3f}'.format(eval('{}+{}'.format(k,a)))
	return slownik

print("===========1===========")
nowy_slow = pierwsza(6)
print(nowy_slow)

print("=============2=========")
def dowolna(*a):
	l = []
	for i in a[0]:
		for j in a[1:]:
			if i not in j:
				break
		else:
			l.append(i)
	return l

nowa_lista = dowolna([1,2,3,4],[2,3,4,5],[3,4,5,6])
print(nowa_lista)
nowa_lista = dowolna('qwer','aseraw','ewqr')
print(nowa_lista)

print("=======3==========")
def sekwencja(a,b, tryb = True):
	if tryb:
		x = min(len(a),len(b))
		l = [(a[i],b[i]) for i in range(x)]
		return l
	else:
		l = [(a[i] if i < len(a) else None ,b[i] if i < len(b) else None) for i in range(max(len(a),len(b)))]
		return l

lista3 = sekwencja([1,2,3,4,5,7,98,12],[6,7,8,9,10,19],0)
print(lista3)


print("=========4=========")
def min(*a):
	temp = a[0]
	for i in a:
		if temp > i:
			temp = i
	return temp

def max(*a):
	temp = a[0]
	for i in a:
		if temp < i:
			temp = i
	return temp

def min_max(fun,*a):
	return fun(*a)

min_val = min_max(min,*[9,2,7,4])
print(min_val)
max_val = min_max(max,*[76,4,23,12,74,109,77])
print(max_val)


print("=====5======")
def rozmien(kwota, a = (10,5,2)):
	l = []
	for i in a:
		while True:
			if kwota - i >=0:
				l.append(i)
				kwota = kwota-i
			else:
				break
	return l
print(rozmien(148))


print("========6========")
def ostatnie(a,b,c,tryb = 'r'):
	while True:
		los = randrange(b,c) if tryb == 'r' else (b+c)//2
		if los == a:
			return los
		b = los if a>los else b
		c = los if a<los else c


print(ostatnie(42,0,100,0))