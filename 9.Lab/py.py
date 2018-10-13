import matplotlib.pyplot as plt
from random import *

class IFS:
	def __init__(self, zestaw):
		self.x = [0]
		self.y = [0]
		self.wsp = zestaw

	def przeksztalcenia(self):
		for step in range(100000):
			z = randrange(len(self.wsp))
			xt = self.wsp[z][0] * self.x[step] + self.wsp[z][1] * self.y[step] +  self.wsp[z][2]
			yt = self.wsp[z][3] * self.x[step] + self.wsp[z][4] * self.y[step] +  self.wsp[z][5] 
			self.x.append(xt)
			self.y.append(yt)
		plt.plot(self.x, self.y, ',', color = 'g' )	
		plt.show()	

		

zestaw_1 = ((0,0,0,0.2,0.16,-0.04), (0.2,-0.26,0,0.23,0.22,0.1), (-0.15,0.28,0,0.26,0.24,0.1), (0.85,0.04,0,-0.04,0.84,0.1))
zestaw_2 = ((0.7,0.109682,0.05,-0.109504,0.893292,0.1),(0.058474,-0.573783,-0.18,0.191261,0.175423,-0.21),(0.011,0,0,0,0.3,-0.35),(-0.067485,0.579556,0.21,0.292311,0.155291,-0.21))
zestaw_3 = ((0.255,0,0.3726,0,0.255,0.6714),(0.255,0,0.1146,0,0.255,0.2232),(0.255,0,0.6306,0,0.255,0.2232),(0.37,-0.642,0.6356,0.642,0.37,-0.00061))

a = IFS(zestaw_3)
a.przeksztalcenia()
