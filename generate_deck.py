from ast import literal_eval


class Deck():		# поле
	""" поля на... поле?... """
	def __init__(self, ID, name, b_price, color, rent):
		self.ID = ID
		self.name = name
		self.b_price = b_price
		self.color = color
		self.rent = rent 	# запиши потом в виде массива
		self.s_price = b_price // 2	# равен половине от b_price
		self.owner = None
		self.upgrade = 0


def data_in_arr(STR_NAMES,B_PRICES, COLORS, RENTS):
	""" преобразует считанные файлы в массивы и выводит их"""

	b_prices = []
	colors = []
	rents = []
	str_names = []

	for i in range(40):	# один цикл для всех списков
		b_prices.append(int(B_PRICES.readline()))	# заполняем цены покупки
		colors.append(int(COLORS.readline()))		# заполняем цвета

		# заполняю названия улиц
		x = STR_NAMES.readline()
		str_names.append(x.strip())	# ф-я str.strip() удаляет всякую лишнюю херь в начале и в конце строки

	for i in RENTS.readlines():
		i = literal_eval(i.strip())
		rents.append(i)
	return tuple(str_names), tuple(b_prices), tuple(colors), tuple(rents)

# блок открытия файлов
B_PRICES = open("B_PRICES.txt", "r")
COLORS = open("COLORS.txt", "r")
RENTS = open("RENTS.txt", "r")
STR_NAMES = open("STR_NAMES.txt", "r")

# КОРТЕЖИ, хранящие параметры полей
STR_NAMES, B_PRICES, COLORS, RENTS = data_in_arr(STR_NAMES, B_PRICES, COLORS, RENTS)

# создаём кортеж с полями, имеющими параметры
FIELD = []
for i in range(40):
	FIELD.append(Deck(i ,STR_NAMES[i], B_PRICES[i], COLORS[i], RENTS[i]))

FIELD = tuple(FIELD)	# кортеж с полями

"""
Пояснение за FIELD.color
1-8 - улицы
9 - коммуналка
10 - жд
0 - служебные поля
"""