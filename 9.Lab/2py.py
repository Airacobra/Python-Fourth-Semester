class Wektor:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, vec):
		if isinstance(vec, Wektor):
			return Wektor(self.x + vec.x, self.y + vec.y, self.z + vec.z)

	def __iadd__(self, vec):
		if isinstance(vec, Wektor):
			self.x += vec.x
			self.y += vec.y
			self.z += vec.z
			return self

	def __str__(self):
		return '({0}, {1}, {2})'.format(self.x, self.y, self.z)
	def __setitem__(self, index, value):
		if(index == 0):
			self.x = value
		elif(index == 1):
			self.y = value
		elif(index == 2):
			self.z = value

	def __getitem__(self, index):
		if(index == 0):
			return self.x
		elif(index == 1):
			return self.y
		elif(index == 2):
			return self.z

	def iloczyn_skalarny(self, vec):
		if isinstance(vec, Wektor):
			return(self.x * vec.x + self.y * vec.y + self.z * vec.z)

	def iloczyn_wektorowy(self, vec):
		if isinstance(vec, Wektor):
			return Wektor(self.y * vec.z - self.z * vec.y, - self.x * vec.z + self.z * vec.x, self.x * vec.y - self.y * vec.x)

	def iloczyn_mieszany(self, vec, vec2):
		if isinstance(vec, Wektor) and isinstance(vec2, Wektor):
			return self.iloczyn_skalarny(vec.iloczyn_wektorowy(vec2))
					
wek_1 = Wektor(5,10,15)
wek_2 = Wektor(100,40,60)
wek_3 = Wektor(2,4,6)

print(wek_1 + wek_2)

wek_1 += wek_2
print(wek_1)

print(str(wek_1))

wek_1[2] = 100
print(wek_1)

a = wek_1[2]
print(a)

print(wek_1.iloczyn_skalarny(wek_2))

print(wek_1.iloczyn_wektorowy(wek_2))

print(wek_1.iloczyn_mieszany(wek_2, wek_3))