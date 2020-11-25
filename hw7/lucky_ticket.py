"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
	ticket_num = str(ticket_num)
	half = len(ticket_num) / 2
	if half == 1.0:
		if ticket_num[0] == ticket_num[1]:
			return True
		else:
			return False
	elif half == 2.0:
		first_half = int(ticket_num[0]) + int(ticket_num[1])
		second_half = int(ticket_num[2]) + int(ticket_num[3])
		if first_half == second_half:
			return True
		else:
			return False
	elif half == 3.0:
		first_half = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
		second_half = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])
		if first_half == second_half:
			return True
		else:
			return False

assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
print('everything is ok')