str1 = input('Enter something: ')

upper_count = 0
lower_count = 0

str2 = ''.join(str1.split())
str3 = str1

for letter in str2:
    if letter == letter.upper():
      upper_count += 1
    elif letter == letter.lower():
        lower_count += 1
    else:
        pass

if upper_count > lower_count:
    edit1 = str1.upper()
elif lower_count > upper_count:
    edit1 = str1.lower()
else:
    edit = str1.swapcase()

if str1.istitle() == True:
    edit2 = 'done. ' + str1
else:
    edit2 = 'draft: ' + str1[6:]

if len(str1) > 20:
    edit3 = str1[:21]
else:
    while len(str3) < 20: 
        str3 += '@'
    else: 
        edit3 = str3

print(f'Исходная строка: {str1}.\nРезультат:\n{edit1}\n{edit2}\n{edit3}')
