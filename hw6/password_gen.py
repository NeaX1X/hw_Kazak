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
from random import randint, sample 
from string import ascii_letters, ascii_lowercase, digits, punctuation


def main():
	pw_difficulty = input('Enter a password difficulty (1, 2 or 3): ')
	if pw_difficulty == '1':
		print(gen_pw(ascii_lowercase))
	elif pw_difficulty == '2':
		print(gen_pw(ascii_letters + digits))
	elif pw_difficulty == '3':
		print(gen_strong())


def gen_pw(chars, length = 8):
	password = ''.join(sample(chars, length))
	return password


def gen_strong():
	password = gen_pw(ascii_letters + digits + punctuation, randint(8, 16))
	upper = lower = digit = punct = 0
	for i in password:
			if i.islower():
				lower += 1
			elif i.isupper():
				upper += 1
			elif i.isdigit():
				digit += 1
			else:
				punct += 1
	if lower > 0 and upper > 0 and digit > 0 and punct > 0:	
		return password
	return gen_strong()


main()
