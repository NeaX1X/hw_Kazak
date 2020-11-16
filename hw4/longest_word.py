str1 = input('Введитe текст: ')

max_lenght = '0' 

for i in str1.split():
	if len(i) > len(max_lenght):
		max_lenght = i
	else: 
		pass

print(f'Длинна строки {len(str1)} символов. Самое длинное слово {max_lenght}'
	+ f' и его длинна {len(max_lenght)} символов.')
