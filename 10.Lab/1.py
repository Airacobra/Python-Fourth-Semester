print('---1v1---')
class LiczbaPierwsza:
	def __init__(self,e):
		self.liczba = 2
		self.stop = e
		self.flag = 1
	def __iter__(self):
		return self
	def __next__(self):
		while True:
			if self.liczba == self.stop:
				raise StopIteration
			self.flag = 1	
			for i in range(2, int(self.stop ** 0.5)):
				if not self.liczba % i:
					self.flag = 0
					break		
			self.liczba += 1
			if(self.flag):
				return self.liczba - 1	 
		# for self.liczba in range(self.start,self.stop+1):
		# 	# if self.liczba == self.stop:
		# 	# 	raise StopIteration
		# 	for number in range(2, int(self.liczba**0.5)):
		# 		if self.liczba % number == 0:
		# 			break
		# 		elif number == int(self.liczba**0.5):
		# 			self.start = self.liczba+1
		# 			return self.liczba
		# 	# 	if self.liczba % i == 0:
		# 	# 		self.czypierwsza = 0
		# 	# if self.czypierwsza:
		# 	# 	return self.liczba
		# raise StopIteration		

a = LiczbaPierwsza(15)
for i in a:
	for j in a:
		print(i,j)			

class v2A:
	def __init__(self,e):
		self.liczba = 2
		self.stop = e
		self.flag = 1
	def __next__(self):
		while True:
			if self.liczba == self.stop:
				raise StopIteration
			self.flag = 1	
			for i in range(2, int(self.stop ** 0.5)):
				if not self.liczba % i:
					self.flag = 0
					break		
			self.liczba += 1
			if(self.flag):
				return self.liczba - 1	 		

class v2B:
	def __init__(self,e):
		self.liczba = 2
		self.stop = e
		self.flag = 1
	def __iter__(self):
		return v2A(self.stop)	

print('---1v2---')
v2 = v2B(15)
for i in v2:
	for j in v2:
		print(i,j)			


#----------------------------------------------------
print('---2---')
class P:
	def __init__(self, number):
		self.level = number
		self.numer = 0
		self.wiersz = [1]
	def __iter__(self):
		return self
	def __next__(self):
		if self.numer == 0:
			self.numer += 1
			return self.wiersz
		elif self.numer == 1:
			self.numer += 1
			self.wiersz = [1, 1]
			return self.wiersz
		elif self.numer < self.level:
			self.numer += 1
			kolejny = [1]
			for x in range(0, self.numer - 2):
				kolejny.append(self.wiersz[x] + self.wiersz[x+1])
			kolejny.append(1)
			self.wiersz = kolejny
			return self.wiersz	
		raise StopIteration	
				 
a = P(5)
for j in a:
	print(j)		

print('---3---')
#----------------------------------------------------
class Los:
	def __init__(self):
		self.m = pow(2,48)
		self.a = 44485709377909
		self.c = 9
		self.xn = 1
	def __iter__(self):
		return self
	def __next__(self):
		self.xn = (self.a*self.xn+self.c)%self.m
		return self.xn


