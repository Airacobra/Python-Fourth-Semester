#list.count()
#list.index()
#list.insert() pod okreslony indeks z roszeszeniem
#list.remove()
#list.pop
#list.sort() dziala w miejscu, 
#l = l.sort() poprawne, zwraca none jet funkcja nic zwraca
#list.reverse()
#def f(x,y)
#def f(x=y) slowa kluczowe

#jezeli chcemy wymusic inne sortowanie niz domylsne, to musimy ja przeslonic
#l = [(1,7),(-3,3),(0,5)]
#l.sort(cmp = lambda x,y: cmp(x[1],y[1])) #zadziale w python2, w python3 nie istnieje
#l.sort(key = lamda x: x[1]) ten wzgledem ktorego chcemy posortowac

#[x for x in l if x[0] < x[1]] bierzemy element z listy, sprawdzamy warunek, jezeli spelniont to dodajemy
#[x if warunek else ... for ...]

#stringi sa niemodyfikalne, trzeba tworzyc nowe obiekty
#str.numerics()
#str.startswithh()
#str.fing()
#str.index()
#str.count()

# s='*'.join(['1','2','3'])    * - string, do ktorego dolaczymy sekwencje stringow
# s.split() domyslnie wzgledem bialych znakow
# s.partition()
# s.rsplit()
# s.rpartition()

#enumarate(seq) dla petli for i in lista
#dostaniemy (indeks,liczba)

#sorted(lista) tworzy nowa posortowana liste?