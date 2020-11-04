n = int(input('Enter quantiy of numbers: '))
operator = input('Enter operator (+, -, *, /):')
outcome = 0

while n > 0:
	number = int(input('Enter a number '))
	n -= 1
	if operator == '+':
		outcome += number 
	elif operator == '-':
		number -= number
		outcome = number
	elif operator == '*':
		outcome = 1
		outcome *= number
	elif operator == '/':
		outcome /= number 
	
print(outcome)

