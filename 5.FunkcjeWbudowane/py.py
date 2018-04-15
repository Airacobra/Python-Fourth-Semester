print('---------1----------')

from time import time
from sys import version

powt=1000
N=10000
		
def tester(fun):
	t_start = time()
	for i in range(powt):
		fun(N)
	t_end = time()
	return t_end - t_start

def	forStatement(n):
	list = []
	for i in range(n):
		list.append(i*i)

def listComprehension(n):
	list = [(i*i) for i in range(n)]

def mapFunction(n):
    list = map(lambda i: i*i, range(n))

def generatorExpression(n):
	list = ((i*i) for i in range(n))	


print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
 print(testFunction.__name__.ljust(20), '=>', tester(testFunction))


print('\n---------2----------')
from random import *

list2_1 = [randrange(0,20) for _ in range(100)]
list2_2 = [randrange(0,20) for _ in range(100)]
print(list2_1,'\n')
print(list2_2,'\n')

#list2_3 = list(filter(lambda x: 3<x<15, (lambda x,y: x+y, zip(list2_1,list2_2))))
list2_3 = list(filter(lambda l: 3<sum(l)<15, zip(list2_1, list2_2)))
print(list2_3)


print('\n---------3----------')
from math import sqrt

def funkcja3(l_x, l_y):
	x_srednie = sum(l_x)/len(l_x)
	y_srednie = sum(l_y)/len(l_y)
	D = sum(list(map(lambda x: pow(x-x_srednie,2), l_x)))
	print('D = ', D, '\n')
	a = 1/D * sum(list(map(lambda x,y: y*(x-x_srednie), l_x, l_y)))
	print('a = ', a, '\n')
	b = y_srednie - a * x_srednie
	print('b = ', b, '\n')
	delta_y = sqrt(sum(map(lambda x,y: pow(y - a*x + b ,2),l_x, l_y))/len(l_x))
	print('delta_y = ', delta_y, '\n')
	delta_a = delta_y/sqrt(D)
	print('delta_a = ', delta_a, '\n')
	delta_b = delta_y * sqrt(1/len(l_x) + pow(x_srednie,2)/D)
	print('delta_b = ', delta_b, '\n')
	return 'End of fun'

list3_1 = [6,2,8,6,1] 
list3_2	= [1,9,5,0,2]
print(funkcja3(list3_1,list3_2))

print('\n---------4----------')

def myreduce(fun, seq):
	nextOne = seq[0]
	for i in seq[1:]:
		nextOne = fun(nextOne, i)
	return nextOne	

print(myreduce(lambda x,y: x+y, [5,2,3,5]),'\n')
print(myreduce(lambda x,y: x*y, [5,2,3,5]))		

print('\n---------5----------')

list5 = [(randrange(1,11), randrange(1,11)) for _ in range(1,11)]
print(list5,'\n')

#list5_2 = myreduce(lambda x,y: map() ,list5)
#print(list5_2)