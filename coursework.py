"""
    Casino

    ** для высшего балла хранить статистику игроков в файле
        и при каждом запуске casino запрашивать имя игрока.

    При запуске программы:
        - игроку необходимо ввести имя
        - попадаем в Главное меню
        * возможно у игрока должно быть изначально какое-то количество очков

    Главное меню:
    1. Magic
    2. Blackjack (21)
    3. Посмотреть статистику
    4. Сбросить игровой прогресс

    При выборе пункта 1.
        - выводятся правила игры
        - запускается игра magic (hw3/magic.py)
        - в игре ограниченное количество попыток
        * придумать правила начисления очков при угадывании с 1, 2 .. N попыток
        * придумать правила потери очков при проигрыше

    При выборе пункта 2.
        - выводятся правила игры
        - игрок делает ставку (не больше, чем у него имеется очков)
        - запускается игра blackjack (21)

    При выборе пункта 3.
        - выводится подробная статистика игрока:
            Имя игрока: Max
            Количество очков: 190

            Magic
            Всего игр сыграно: 20
            Выиграно: 5
            Коэффициент выигрышей: 0.25
            Рекордное количество попыток: 2

            Blackjack
            Всего игр сыграно: 0
            Выиграно: 0
            Коэффициент выигрышей: -

    При выборе пункта 4.
        - удаляются данные игрока
        - запрашивается имя нового игрока
        - попадаем в Главное меню


    Реализаци blackjack (правила https://en.wikipedia.org/wiki/Blackjack):
        - формируется колода карт
            от двойки до десятки — от 2 до 10 соответственно,
            у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1),
            у т.н. картинок (король, дама, валет) — 10.

            в итоге колода - [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        - колода перетосовывается с помощью random.shuffle()
        - игроку предлагается на выбор:
            1. взять ещё карту
                - из колоды исключается одна карта и дается игроку
            2. остановиться

        - если у игрока в сумме выходит 21 - победа (игроку возвращается удвоенная ставка)
        - если у игрока в сумме выходит больше 21 (перебор) - проигрыш (ставка снимается в пользу казино)
        - если игрок остановился на сумме меньше 21 - ставка возвращается игроку

        * описынные выше правила можно дополнить по желанию
"""

import random, time

class Player:
    name = None
    points = 200
    magic_played = 0
    magic_win = 0
    bj_played = 0
    bj_win = 0 
    magic_record = 0

    def __init__(self, name=None):
        self.name = name 


def main():
	register()
	menu()


def register():
	global player
	player = Player(input('Enter your name: '))
			

def menu():
	print(
		'\nCASINO',
		'\n1. Magic',
		'\n2. Blackjack (21)',
		'\n3. See statistics',
		'\n4. Reset',
		)

	to_do = input('\nWhat do you want to do?\n')
	if to_do.lower() == 'magic' or to_do == '1':
		print('\nMAGIC\n',
			'\nRULES:',
			'\nGame generates a number, which you need to guess in 20',
			'\nattempts or less. Else you lose also with every guess',
			'\nyour score goes down by 5(max 100)'
			)
		magic()
	elif to_do.lower() == 'blackjack' or to_do == '2' or to_do == '21':
		print('\nBLACKJACK\n', '\nRULES:\nYou get 2 cards and then you can',
		'\ndraw a card(hit) or stop. When you stop dealer draws till gets 17 ',
		'\npoints (2-10 has 2-10 points, Jack, Queen and King 10 and Ace 11)',
		'\nThe goal is to get more points then dealer, but if you go',
		'\nover 21 you lose, if you get 21 you win automaticaly.\n '
		)
		
		blackjack()
	elif to_do.lower() == 'see statistics' or to_do == '3':
		print('hi')
		statistic()
	elif to_do.lower() == 'reset' or to_do == '4':
		print('')
		reset()


def magic():
	random_number = random.randint(1, 100)  
	record = player.magic_record
	score = 100
	player.magic_played += 1 
	print('The game started. Guess the number.\n')

	while True and score!= 0:
		try:
			number = int(input('Your guess: '))
		except ValueError:
			continue

		if number > random_number:
			print('Magic number is smaller')
			score -= 5
		elif number < random_number:
			print('Magic number is larger')
			score -= 5
		else:
			print('\nYou won! Magic number was', number)
			player.points += score
			player.magic_win += 1 
			if score > record:
				print('New record! Your score is:', score)
				player.magic_record = score
			else:
				print('Score: ', score)

			if input('\nContinue? (y/n)\n') == 'n':
				menu()
			else:
				magic()

		if score == 0:
			player.points -= 100
			if input('You lost. Do you want to try again?(y/n)\n') == 'n':
				menu()
			else:
				score = 100
				magic()


def blackjack():
	global bet
	bet = int(input("Enter your bet: "))
	deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
	random.shuffle(deck)
	dealer_hand = deck.pop()
	user_hand = deck.pop() + deck.pop()
	while user_hand < 21:
		if input('You have ' + str(user_hand) + ' points.'
		+' What to do?(hit = h,stop = s)') == "h":
			user_hand += deck.pop()
		else:
			while dealer_hand < 17:
				dealer_hand += deck.pop()
				print('Dealer has', dealer_hand, 'points')
			else:
				if dealer_hand > user_hand and dealer_hand <= 21:
					print('Dealer wins')
					lose()
					break
				elif dealer_hand == user_hand:
					print('Tie')
					player.bj_played += 1
					break
				else:
					win()
					break
	if user_hand == 21:
		print('Blackjack!(21 points)')
		win()
	elif user_hand > 21:
		print(user_hand, 'is more than 21, so:')
		lose()
	
	if input('\nContinue(y/n) ') == 'n':
		menu()
	else:
		blackjack()
	

def win():
	print('You won! You got', bet * 2, 'points')
	player.bj_played += 1
	player.bj_win += 1
	player.points += bet


def lose():
	print('You lost', bet, 'points')
	player.bj_played += 1
	player.points -= bet



def statistic():
	if player.bj_played != 0 or player.bj_win != 0:
		win_bj = round(player.bj_win * 100 / player.bj_played , 2)
	else:
		win_bj = '---'
	if player.magic_played != 0 or player.magic_win != 0:
		win_magic = round(player.magic_win * 100 / player.magic_played , 2)
	else:
		win_magic = '---'

	print(
		'Name:', player.name,'\nPoints:', player.points,
		'\n\nMAGIC\nPlayed:', player.magic_played, '\nWin:', player.magic_win,
		'\nRecord', player.magic_record, '\nWin %:', win_magic,
		'\n\nBLACKJACK\nPlayed:', player.bj_played, '\nWins:', player.bj_win,
		'\nWin %:', win_bj)
	time.sleep(3)
	menu()


def reset():
	player = None
	main()


main()