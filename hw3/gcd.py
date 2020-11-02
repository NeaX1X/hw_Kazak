a = int(input('a: '))
b = int(input('b: '))
 
if a > b:
	c = a % b
	if c == 0:
		print(b)
	else:
		c = a % b 
		while c % b != 0:
			c = c % b 
		else:
			print(c)
elif a < b:
	c = b % a 
	if c == 0:
		print(a)
	else:
		while c % a != 0:
			c = c % a
		else:
			print(c)
