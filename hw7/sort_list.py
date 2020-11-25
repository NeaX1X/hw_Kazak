"""
    Напишите функцию, которая принимает список чисел
    и возвращает отсортированный список,
    при условии, что все числа -1 остаются на своих местах.
"""
test = [-1, 7, 4, 54, -1]

def sort_ascending(x):
	other_digits = []
	list_ = []
	for i in x:
		if i != -1:
			other_digits.append(i)

	other_digits.sort()

	for i in x: 
		if i == -1:
			list_.append(i)
		else:
			for l in other_digits:
				list_.append(l)

	print(list_)
		
sort_ascending(test)

t_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(t_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

t_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(t_2) == [-1, -1, -1, -1, -1]

t_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(t_3) == [2, 2, 4, 9, 11, 16]

t_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(t_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

t_5 = [-1]
assert sort_ascending(t_5) == [-1]
