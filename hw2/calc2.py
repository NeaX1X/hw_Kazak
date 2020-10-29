number1 = input('Enter first number ')
number2 = input('Enter secind number ')
operator = input('Enter operator ')

try: 
	number1, number2 = int(number1), int(number2)
except:
	print('This in not a number')
else:
	if operator == '-':
		print(number1 - number2)
	elif operator == '+':
		print(number1 + number2)
	elif operator == '*':
		print(number1 * number2)
	elif operator == '//':
		print(number1 // number2)
	elif operator == '**':
		print(number1 ** number2)
	elif operator == '/':
		if number2 == 0: 
			print('Error: zero division')
		else:
			print(number1 / number2)
	else:
		print('Invalid operator')

