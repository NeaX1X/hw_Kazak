"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).

    Перед записью в файл привести номер к формату +380501234567.
"""
import re

def name():
	
	names = []
	numbers = []
	new = []
	with open('phone_book.txt', 'r') as f:
		data = f.read()	
		data = data.split('\n')
		for i in data:
			num = re.sub(r'\D', '', i)
			numbers.append(num)
			nam = re.sub(r'[^a-zA-Z]', '', i)
			names.append(nam)
		for i in names: 
			if i.startswith('M') or i.endswith('a'):
				edited_number = '380' + numbers[names.index(i)][-9:]
				file = open('edited_phone_book.txt', 'a')
				add = i + ' ' + edited_number + '\n'
				file.write(add)			
				file.close()
						
name()

'''
tmp = []
path = '~/file1.txt' #substitute your path to file1
path_final = '~/file2.txt' #substitute your path to file2
with open(path, 'r') as file:
    for x in file:
     x = x.replace('\n','').replace(' ', '')
     x = x[4:]   
     tmp.append(x)
 
for x in range(len(tmp)):
 for i in tmp[x]:
    more3 = tmp[x].count(i)
    if more3 > 3:
        with open(path, 'r') as f:
         data = f.readlines()[x]
         with open(path_final, 'a') as file2:
             file2.write(data)
         break
'''