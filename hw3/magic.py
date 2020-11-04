range1 = int(input('Enter start number: '))
range2 = int(input('Enter end number: '))

cont = 1
while cont == 1:
	import random
	random_number = random.randint(range1, range2)

	number = int(input('Enter your guess '))
	atempt = 1

	while number != random_number:
		if number > random_number:
			print('Bigger')
			number = int(input('Enter your guess '))
			atempt += 1
		elif number < random_number:
			print('Smaller')
			number = int(input('Enter your guess '))
			atempt += 1 
	else:
		print('Number was', random_number, 'and it took you ', atempt, 'guesses.')
		answer = input('Continue y/n ')
		if answer == 'y':
			cont = 1
		elif answer == 'n':
			cont = 0
		else:
			cont = 0
			print('Invalid answer')
