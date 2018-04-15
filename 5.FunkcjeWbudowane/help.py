all(sekwencja) #zwracaja wartosc logiczna
any(sekwencja)

def fun(a,b)
	return a + b
f = lambda a,b: a + b #jedna instrukcja

map(funkcja, sekwencja) #tyle zmiennych ile przeslemy sekwencji
zip(sekwencja, ...) #zwracany iterator
filter(fun, seq) #zwraca te elementy z seq, dla której wykonanie fun = true
reduce(fun,seq) #bierzemy dwa pierwsze elementy, zwracamy wynik fun, dokladamy kolejny element i znowu zwracamy wartosc itd.
^from functools import reduce