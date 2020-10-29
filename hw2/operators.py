a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

print('Числа: ', a, b, c )

if a % 5 == 0 and b % 5 == 0 and c % 5 == 0:
	print(a + b + c)
elif  a % 5 == 0 and b % 5 == 0 and c % 5 != 0:
	print(a + b)
elif a % 5 != 0 and b % 5 == 0 and c % 5 != 0:
	print(b)
elif a % 5 != 0 and b % 5 == 0 and c % 5 == 0:
	print(b + c)
elif a % 5 == 0 and b % 5 != 0 and c % 5 != 0:
	print(a)
elif a % 5 == 0 and b % 5 != 0 and c % 5 == 0:
	print(a + c)
elif a % 5 != 0 and b % 5 != 0 and c % 5 == 0:
	print(c)
else:	
	print('Нету чисел красных 5')

if a >= 0 and b >= 0 and c >= 0:
	print(3)
	print(0)
elif a >= 0 and b >= 0 and c < 0:
	print(2)
	print(1)
elif a >= 0 and b < 0 and c < 0:
	print(1)
	print(2)
elif a >= 0 and b < 0 and c >=0:
	print(2)
	print(1)
else:
	print(0)
	print(3)

if a >= b and b >= c:
	print(a + b)
elif a >= b and c >= b:
	print(a + c)
elif b >= a and a >= c:
	print(b + a)
elif b >= a and c >= a:
	print(b + c)
elif c >= b and b >= a:
	print(c + b)
else:
	print(c + a)