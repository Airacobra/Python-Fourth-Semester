#/usr/bin/env python3.6
import keyword
import math

#print(keyword.kwlist)

#print(dir(math))
#print (help(math.erfc))

print(abs(-1))
print(math.fabs(-1.2))
print(math.pow(2,3))
print(pow(2,4,6))

print(math.modf(-1.2))

print(math.hypot(-1.2,1))

print(math.modf.__doc__)

print(2**3)

a,*b=2,3,4,5
print(a)
print(b)
print(type(b))
a,b=b,a
print(a)
print(b)

print(type(()))

s = 'Ala'*5
print (type(s), ' ' , s )
s=1.
print(type(s))


print('/////////////////////////////////////')

k=(1,2,[1,2],3.)
print(k)
k[2][0]='a'
print(k)

print('/////////////////////////////////////')

k=[1,2,[1,2],3.]
k[2]="A"
print(k)
print('/////////////////////////////////////')

l=[0]*10
l[1]='a'
print (l)

print('/////////////////////////////////////')
l2=[[]]*10
l2[1].append(2)
print (l2)

print('/////////////////////////////////////')
l3=[[] for _ in range(10)]
l3[2].append(2)

l4=l3
print (id(l3[1]))
print(id(l4[1]))
print(len(l4))

print('/////////////////////////////////////')

lista = [x**2 for x in range(9)]
lista.append([2,2])
print(lista)
nowa_lista=lista[:]
print(nowa_lista)
nowa_lista[-1][0] = 'a'
nowa_lista[0]=10
print(lista)
print(nowa_lista)

from copy import deepcopy
nowa_nowa_lista = deepcopy(lista)

nowa_nowa_lista[-1][0] = 'b'
print(lista)
print (nowa_nowa_lista)

nowa_nowa_lista.append([100,'q'])
print(nowa_nowa_lista)
nowa_nowa_lista.extend([200,'z'])
print(nowa_nowa_lista)

print('/////////////////////////////////////')
print('/////////////////////////////////////')
print('/////////////////////////////////////')
from math import sqrt
from cmath import sqrt as csqrt

#y = ax^2 + bx +c

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
delta = b*b - 4*a*c
if delta < 0:
    print("brak rozwiazan rzeczywistych")
elif delta == 0:
    print("wynik to")
    print(-b/2*a)
else:
    print("wynik to")
    print(((-1)*b - sqrt(delta)/2*a, "lub",((-1)*b + sqrt(delta)/2*a )))

print((-b - csqrt(delta)/2*a, "lub",(-b + csqrt(delta)/2*a )))
print('////////////działa jak w C2/////////////////////////')
from sys import argv
print(argv)
print('/////////////////////////////////////')
for i in range (10,3,-2):
    print(i)
print('/////////////////////////////////////')
for i in range(len(nowa_nowa_lista)):
    nowa_nowa_lista[i] = 1
print(nowa_nowa_lista)

print('/////////////////////////////////////')
lista2  = ([1,2],(3,4),[5,6])
for i,j in lista2:
    if i+j > 20:
        break
else:
    print(i, j)

print('/////////////////////////////////////')
#if warunek else F !!