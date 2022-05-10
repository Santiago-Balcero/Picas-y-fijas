import random

print ("JUEGO PICAS Y FIJAS\nAdivina el número de 4 cifras: _ _ _ _\n\nPistas:\n-No se repiten números.\n-Pica: cifra que está en el número a adivinar pero en diferente \nposición.\n-Fija: cifra que está en el número a adivinar y que está en la \nmisma posición.")

#Generación de número aleatorio sin repetir
start = False
while start == False:
	n1 = random.randint(0,9)
	n2 = random.randint(0,9)
	while n1 == n2:
		n2 = random.randint(0,9)
	n3 = random.randint(0,9)
	while n3 == n2 or n3 == n1:
		n3 = random.randint(0,9)
	n4 = random.randint(0,9)
	while n4 == n3 or n4 == n2 or n4 == n1:
		n4 = random.randint(0,9)
	start = True

numbers = str(n1)+str(n2)+str(n3)+str(n4)
#print (numbers)
fijas = 0
intentos = 0
nums_ok = False

while fijas < 4:
	#Validación entrada de usuario
	while nums_ok == False:
		user_nums = input("\nDigita 4 números que no se repitan: ")
		picas = 0
		fijas = 0
		if len(user_nums) == 4 and user_nums.isdigit() == True:
			break

	#Comparación usuario vs juego
	for n in numbers:
		for n_user in user_nums:
			if n_user == n:
				picas += 1
				if user_nums.index(n_user) == numbers.index(n):
					fijas += 1

	print ("Picas:", picas-fijas)
	print ("Fijas:", fijas)
	intentos += 1

print ("Ganaste en", intentos, "intentos!")