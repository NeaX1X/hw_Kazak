from random import choice
# 1. Создайте переменную x, которая равняется 2 в степени 3

x = 2 ** 3

# 2. Прибавьте к x 3

x += 3

# 3. Сгенерируйте список num_list длиной x, из случайных чисел в диапазоне от 1 до x

counter = x
num_list = []
while counter != 0:
	counter -= 1
	num_list.append(choice(range(1, x)))

# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел

num_list.reverse()
print(num_list)

# 5. Вставьте в средину списка число 11.

num_list.insert(len(num_list)//2, 11 )


# 6. Запишите в файл list_info.txt строчки
#    - количество элементом списка
#    - количество уникальных элементов списка
#    - самое маленькое число списка
#    - сумму чисел списка кратных 3
'''
with open ('list_info.txt', 'a') as f:
	f.write(len(num_list) + len(set(num_list)) + min(num_list) + sum(i for i in num_list if i % 3 == 0)
'''
# 7. Создайте список countries_info из 3 словарей c ключами
#    'country', 'population', 'cities' и заполните их любыми значениями
#    ('country' - строка, 'population' - число, 'cities' - список строк)

countries_info = [
 	{
        'country': 'First country',
        'population': 1000000,
        'cities': ['one', 'two', 'three']
    },
    {
        'country': 'Second country',
        'population': 5555555,
        'cities': ['three', 'one', 'two']
    },
    {
        'country': 'Third country',
        'population': 1234321,
        'cities': ['one', 'three', 'two']
    }]


# 8. Отсортируйте в каждом словаре cities по длине строк в порядке убывания

#sorted(cities, key=len)

# 9. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания



# 10. Напишите функцию create_country_info, которая принимает 3 параметра
#     country, population и cities
#     и возвращает словарь типа
#     {'country': 'USA', 'population': 123, 'cities': ['New York', 'Los Angeles', 'Portland']}

#create_country_info

# 11. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info


# 12. Запуште код в репозиторий (существующий либо новый),
#     ссылку на файл прикрепите к 10 дз
