number = input('Enter phone number: ')

number1 = ''.join(number.split())

while len(number1) < 10:
	print('Not enough numbers. Try again')
	number1 = input('Enter phone number: ')
else:
	if number1.isdigit == True:
		if number1.startswith('38'):
			print(number1)
		else:
			print('38' + number1)
	else:
		number2 = number1.replace('-', '')
		number2 = number2.replace('+', '')
		number2 = number2.replace('(', '')
		number2 = number2.replace(')', '')
		if number2.startswith('38'):
			print(number2)
		else:
			print('38' + number2)
