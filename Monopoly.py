from random import randint
from generate_deck import FIELD
import time

class Player():			# ИГРОК
	""" основные характеристики и действия игроков """
	def __init__(self, ID):
		self.ID = ID
		self.name = input("input name: ")
		self.balance = 1500
		self.cards = []
		self.inPrison = False
		self.position = 0 	# позиции на поле: 0-39
		self.colors_available = [0] * 11
		self.parking = False
		self.prison = False


def create_players():
	""" инициализируем объекты класса Players """
	global player_count
	Players = dict()
	players = []

	player_count = int(input("2-6 players: "))

	if player_count < 2:
		print("ERROR: player_count MUST BE > 2")
		exit()

	for i in range(player_count):
		Players["player_%i" % (i+1)] = Player(i + 1)
		players.append(Players["player_%i" % (i+1)])

	return players


def dice():
	""" бросаем кубики """
	return (randint(1, 6)), (randint(1, 6))


def double_max(arr):
	""" выводит результат: есть ли в массиве два одинаковых максимальных значения?"""

	doubleMax = 0
	maxim = 0
	for i in arr:
		if i > maxim:
			maxim = i
			doubleMax = 0

		elif i == maxim:
			doubleMax = 1

	return doubleMax


def who_start(players):
	""" выводит ИНДЕКС(не номер) игрока по списку"""
	print("\n ---Кто ходит первый?--- \n")
	line = []

	for i in range(player_count):
		result = dice()
		print("Игрок", players[i].name, "выбил", result, sum(result))
		line.append(sum(result))

	if double_max(line):
		print("У некоторых игроков выпало одинаковое количество очков. Перебрасываем!")
		return who_start(players)

	index = line.index(max(line))
	print("Игрок", players[index].name, "ходит первый!")
	return index


def confirm():
	""" отвечает на вопрос: пользователь согласен или нет"""
	if input() == "y":
		return 1
	else:
		return 0


def calculate_deck(player):	# обновлённое место игрока лежит в хар-ке объета, так что ничего больше не передаём
	""" обрабатывает перемещение по полю(улицы, штрафы, бонусы и пр.)"""
	card = FIELD[player.position]
	if (card.color != 0):	# если улица
		if card.owner == None and card.owner != player.ID:
			print("Вы можете купить эту карту (y/n): ", end = "")
			if confirm():
				# покупаем карту
				player.balance -= card.b_price 	# сняли деньги за покупку
				player.cards.append(card.ID)			# присвоили карту человеку
				card.owner = player.ID
				print("Вы купили эту карту!")
				print("Ваш баланс:", player.balance)
			else:
				print("АУКЦИОН!")
		elif card.owner == player.ID:
			print("Это ВАШЕ поле!")
		else:
			print("Оплатите ренту игроку", players[card.owner-1].name)
	else:
		print("Возьмите карточку", card.name)


def player_move(player, value):
	""" функция осуществляет изменение player.position na value"""
	player.position = (player.position + value) % 40
	print("Игрок", player.name, "перешёл на клетку", player.position, ":", FIELD[player.position].name)
	calculate_deck(player)
	return 0


def player_motion(player):
	""" передаём в функцию объект класса Players() и делаем с ним всякое"""
	print("\n\n-----------------------")
	print(str(player.name), "делает ход!", "\n")
	double = 0
	value = dice()
	if value[0] == value[1]:
		double = 1
		print(value, "у вас дубль!")
	print("Игрок", player.name, "выбил", value)

	player_move(player, sum(value))


def main():
	global players
	players = create_players()
	turn_player_number = who_start(players) + 1	# это НОМЕР игрока в списке
	time.sleep(2)
	print(players[0].ID)
	print(players[1].ID)
	while True:
		player_motion(players[turn_player_number - 1])
		turn_player_number = (turn_player_number + 1) % player_count
		time.sleep(2)


main()