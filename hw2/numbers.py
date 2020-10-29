number = int(input('Enter number from 1 to 999 '))

if number == 100 or number > 100:
	a = number //100
	b = (number - a*100) // 10
	c = number % 10
	print(a + b + c) 
	if b == c and a == b:
		print('Числа равны')
	elif b == c and a > b:
		print('Убывание')
	elif b > a and c > b :
		print('Возрастание')
	elif a > b and b > c:
		print('Убывание')
	elif a == b and c > b:
		print('Возрастание')
	else:
		print('В разброс')

elif 10 <= number < 100:
	a = number // 10
	b = number % 10
	print(a + b)
	if a > b:
		print('Убывание')
	elif a < b:
		print('Возрастание')
	else:
		print('Числа равны')
else:
	print(number)


