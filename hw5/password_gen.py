'''
Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (длява 3 пункта можно генерироть пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
'''
dificulty = input()
from random import randint, sample 
from string import ascii_letters, ascii_lowercase, digits, punctuation

if dificulty == '1':
	def easy():
		password = sample(ascii_lowercase, 8)
		print(''.join(password))
	easy()

if dificulty == '2':
	def normal():
		letters_digits = ascii_letters + digits
		password = sample(letters_digits, 8)
		print(''.join(password))
	normal()

if dificulty == '3':
	def hard():
		everything = ascii_letters + digits + punctuation 
		lenght = randint(8, 16)
		password = sample(everything, lenght)
		upper, lower, punct, digit = 0, 0, 0, 0
		for i in password:
			if i.islower():
				lower += 1
			elif i.isupper():
				upper += 1
			for p in punctuation:
				if i == p:
					punct += 1
			try:
				i = int(i)
			except ValueError:
				pass
			else:
				digit += 1
		if lower >= 1 and upper >= 1 and digit >= 1 and punct >= 1:		
 			return ''.join(password)
 		else: 
 			hard()
	hard()

