"""
    Выполните все пункты.

    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

file = open('file_practice.txt', 'w')
file.write('Starting practice with files\n')
file.close()

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

file = open('file_practice.txt', 'r')
print(file.read())
file.close()

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее количество,
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

file = open('files/text.txt', 'r+')
i_count = e_count = 0
data = file.read()
for i in data:
	if i == 'i':
		i_count += 1
	elif i == 'e':
		e_count += 1		
if i_count > e_count:
	data = data.replace('e', 'i')
else:
	data = data.replace('i', 'e')
with open('file_practice.txt', 'a') as f:
	f.write('\n' + data + '\n')
file.close()	

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое

file = open('file_practice.txt', 'a')
file.write('\n*some pasted text*')
if file.tell() % 2 == 0:
	file.write('\nthe end')
else:
	file.write('\nbye')
file.close()