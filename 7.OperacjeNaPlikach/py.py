from glob import glob

print('------------1-------------\n')

def fun1(nazwa, n):
	with open(nazwa) as pl:
		lines = pl.readlines()
		print('n poczatkowych wierszy')
		print(lines[:n],'\n')

		print('n koncowych wierszy')
		print(lines[-n:],'\n')

		print('n-ty wiersz')	
		print(lines[::n],'\n')

		print('n-te slowo')
		for slowo in lines: print(slowo.split(' ')[n])

		print('n-ty znak')
		for znak in lines: print(znak[n])

fun1('plik.txt', 2)

print('------------2-------------\n')

def fun2(nazwa_pliku, klucz, zamien):
	counter = 0
	with open('zamiana.txt', 'w') as plWrite, open(nazwa_pliku) as pl:
		for line in pl:
			if line.startswith(klucz):
				print(line)
				counter += 1
				plWrite.write(line.replace(klucz,zamien))
		print('krotnosc wystapienia: ', counter)


fun2('plik.txt', 'dw', 'zastap')

print('------------3-------------\n')

lista = glob('*.in')

with open('zadanie3.txt', 'w') as pl3:	
	dunno = {}
	for i in lista:
		with open(i) as next_file:
			for line in next_file:
				line = line.split()
				dunno.setdefault(int(line[0]), []).append(float(line[1]))

	for k,v in dunno.items():
		pl3.write(str(k) + ' ' + str(sum(v)/ len(v)) + ' ' + str(max(v) - min(v)) + '\n')

print('------------4-------------\n')


def fun4():
	with open(plot.p, 'w') as pl:
		pl.write(
'''set term pdf
set out 'wykres.pdf'
plot ''')
	
	lista = glob('*.in')
	#for i in lista:
	 



print('------------5-------------\n')

def fun5():
	word_list = []
	lista = glob('*.py')
	with open(lista[0]) as file0:
		for line in file0:
			for word in line.split():
				if word not in word_list:
					word_list.append(word)

	for file_next in lista[1:]:
		temporary = []
		with open(file_next) as file_current:
			for line in file_current:
				for word in line.split():
					if word in word_list and word not in temporary:
						temporary.append(word)

			word_list = temporary[:]	

	print(word_list)		
						
fun5()	






