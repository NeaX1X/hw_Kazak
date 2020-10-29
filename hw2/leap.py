year = int(input('year: '))

if year % 4 == 0 and year % 100 != 0:
	print('year ', year, 'has 366 days') 
else:
	print('year ', year, 'has 365 days')