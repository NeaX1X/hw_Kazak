number = input('Enter 5 digit number: ')

try:
	number = int(number)
except:
	print('Not a number')
else:
	if number >= 10000 and number <= 99999:
		number1 = number // 10000
		number2 = (number - number1 * 10000) // 1000
		number5 = number % 10
		number4 = ((number % 100) - number5) // 10
		end_number = number - number2 * 1000 - number4 * 10
		print(end_number)
	else:
		print('Not a 5 digit number')

