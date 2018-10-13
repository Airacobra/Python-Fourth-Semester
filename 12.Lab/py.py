#1
class Point:
	def __init__(self):
		self.__x = 0
		self.__y = 0
	@property
	def x(self):
		return self.__x
	@property	
	def y(self):
		return self.__y	
	@x.setter
	def x(self, value):
		self.__x = value
	@y.setter
	def y(self, value):
		self.__y = value

P1 = Point()
P1.x = 3
P1.y = 2
print(P1.x, P1.y)	

#2
def dekorator2(xMax, xMin, yMax, yMin):
	def fun(f):
		def fp(*par):
			for p in par:
				if p.x<xMin or p.x>xMax or p.y>yMax or p.y<yMin:
					raise ValueError
			return f(*par)
		return fp	
	return fun

@dekorator2(5,0,5,0)
def sum(P1, P2):
	P3 = Point()
	P3.x = P1.x + P2.x
	P3.y = P1.y + P2.y
	return P3		

@dekorator2(5,0,5,0)
def substraction(P1, P2):
	P3 = Point()
	P3.x = P1.x - P2.x
	P3.y = P1.y - P2.y
	return P3				

P2 = Point()
P2.x = 1
P2.y = 1
P3 = Point()
P3 = sum(P1,P2)
print(P3.x,P3.y)
P3 = substraction(P1,P2)
print(P3.x,P3.y)

#3
from math import *

class Licz:
	@staticmethod
	def pole(a,b,c):
		A = (sqrt(pow(b.x-a.x,2)+pow(b.y-a.y,2)))
		B = (sqrt(pow(c.x-b.x,2)+pow(c.y-b.y,2)))
		C = (sqrt(pow(a.x-c.x,2)+pow(a.y-c.y,2)))
		h = (A+B+C)/3
		res = sqrt(abs(h*(h-A)*(h-B)*(h-C)))
		return res
	@staticmethod
	def pole(a,b,c,d):
		A = (sqrt(pow(b.x-a.x,2)+pow(b.y-a.y,2)))
		B = (sqrt(pow(c.x-b.x,2)+pow(c.y-b.y,2)))
		C = (sqrt(pow(d.x-c.x,2)+pow(d.y-c.y,2)))
		D = (sqrt(pow(a.x-d.x,2)+pow(a.y-d.y,2)))
		h = (A+B+C+D)/4
		res = sqrt(abs(h*(h-A)*(h-B)*(h-C)*(h-D)))
		return res
	@staticmethod
	def obwod(a,b,c,d):
		A = (sqrt(pow(b.x-a.x,2)+pow(b.y-a.y,2)))
		B = (sqrt(pow(c.x-b.x,2)+pow(c.y-b.y,2)))
		C = (sqrt(pow(d.x-c.x,2)+pow(d.y-c.y,2)))
		D = (sqrt(pow(a.x-d.x,2)+pow(a.y-d.y,2)))
		h = (A+B+C+D)
		return h
	@staticmethod
	def obwod(a,b,c):
		A = (sqrt(pow(b.x-a.x,2)+pow(b.y-a.y,2)))
		B = (sqrt(pow(c.x-b.x,2)+pow(c.y-b.y,2)))
		C = (sqrt(pow(a.x-c.x,2)+pow(a.y-c.y,2)))
		h = (A+B+C)
		return h					

A = Point()
B = Point()
C = Point()
D = Point()
A.x = 1
A.y = 1
B.x = 2
B.y = 2		
C.x = 3
C.y = 3		
D.x = 4
D.y = 4	
print(Licz.pole(A,B,C,D))
print(Licz.obwod(A,B,C))

			
			



