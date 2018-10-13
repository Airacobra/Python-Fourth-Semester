from sys import path
path.append('build/lib.linux-x86_64-3.5/')

import mod
print(mod.met(1,2,4))

import time
from random import randint
size1 = 10
size2 = 10000
t1 = [randint(1,10) for _ in range(size1)]
t2 = t1[:]

def bub(t1):
	t_start = time.time()
	for i in range(size1):
		for j in range(size1-1):
			if t1[j]>t1[j+1]:
				t1[j],t1[j+1]=t1[j+1],t1[j]
	t_end = time.time()
	return t_end - t_start

tc1 = time.time()
mod.bubble(t1)
tc2 = time.time()
print('C: ', tc2-tc1)
print('Python: ', bub(t2))