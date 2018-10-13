# class A:
# 	def __init__(self):
# 		print('a')

# class B(A):
# 	def __init__(self):
# 		super().__init__() #wywoluje metode klasy bazowej
# 		print('b')

# ob = B();				
# print(B.mro()) #kolejnosc dziedziczenia

#---------------------------------
# class W:
# 	def __init__(self):
#  		print('w')
#  		super().__init__()

# class A(W):
# 	def __init__(self):
#  		print('a')
#  		super().__init__()

# class V:
# 	def __init__(self):
#  		print('v')
#  		super().__init__()

# class B(V):
# 	def __init__(self):
#  		print('b')
#  		super().__init__()

# class C(A,B):
# 	def __init__(self):
#  		print('c')
#  		super().__init__()

# ob2 = C()
# print(C.mro)	
#---------------------------------
# import abc #abstract base class

# class A:
# 	__metaclass__ = abc.ABCMeta #Python 2

# class A(abc.ABC): #Python 3.4
#---------------------------------
# @abc.abstractmethod  #Python 3.4
# def met(self):
# 	pass
# ---------------------------------
# @staticmethod #statyczna
# def met():
# 	pass
# def met(): #tylko w klasie 
# 	pass	
# ---------------------------------
from types import FunctionType
import abc

#1
class Calka(abc.ABC):
	def __init__(self, start, stop, steps, function):
		if not isinstance(start, (int,float)) or not isinstance(stop,(int,float)) or not isinstance(steps, int):
			raise TypeError	
		self.xp = start	
		self.xk = stop
		self.n = steps
		self.fun = function

	@abc.abstractmethod
	def count(self):
		pass	

class MetodaTrapezow(Calka):
	# def __init(self, start, stop, steps, function):
	# 	super().__init__(start, stop, steps, function)

	def count(self):
		h = (self.xk - self.xp) / self.n
		sum = 0.0
		value = self.xp
		for i in range(self.n):
			sum += self.fun(value) + self.fun(value+h)
			value += h
		sum *= h/2.0
		return sum	
			
class MetodaSimpsona(Calka):
	# def __init(self, start, stop, steps, function):
	# 	super().__init__(start, stop, steps, function)	

	def count(self):
		h = (self.xk - self.xp) / (2*self.n)						
		value = self.xp
		sum1 = 0
		for i in range(1, 2*self.n,2):
			sum1+= self.fun(self.xp+h*i)
		sum1 = 4*sum1
		sum2 = 0	
		for i in range(2, self.n*2-1,2):
			sum2 += self.fun(self.xp+h*i)	
		sum1 += sum2*2 + self.fun(self.xk) + self.fun(self.xp)
		sum1 *= h/3.
		return sum1

Q1A = MetodaTrapezow(0, 5, 1000, lambda x: pow(x,2)+2*x)	
print(Q1A.count())
Q1B = MetodaSimpsona(0, 5, 1000, lambda x: pow(x,2)+2*x)	
print(Q1B.count())		

#2
class Stos:
	def __init__(self, lista = None):
		if isinstance(lista, Stos):
			self.lista = lista.lista
		elif(lista is None):
			self.lista = []
		else:
			raise ValueError
	def dodaj(self, nowy):
		self.lista.append(nowy)
	def usun(self):
		return self.lista.pop()
	def __len__(self):
		return len(self.lista)
	def __str__(self):
		return str(self.lista)

Q2 = Stos()
Q2.dodaj(1)
Q2.dodaj(3)
Q2.dodaj(5)
print(Q2)
Q2.usun()
print(Q2)

class SortujacyStos(Stos):
	def __init__(self, flag):
		super().__init__()
		self.flag = flag
		self.lista.sort()
		if self.flag == 'r':
			self.lista.reverse()
	def dodaj(self, nowy):
		if self.parametr == 'm':
			temp = copy.deepcopy(nowy.lista)
			temp.sort()
			temp.reverse()
			self.lista.extend(temp)
					

			
