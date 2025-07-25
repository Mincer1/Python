import math

#1
# price_eur = float(input("Введите цену в евро: "))
# eur_usd = 1.17
# usd_rub = 79.51
# convector = round(price_eur * eur_usd * usd_rub,2)
# print(f"Цена в рублях {convector}")

#2
# count_num = int(input("Введите кол-во чисел: "))
# for x in range(count_num):
#     num = float(input("Введите число: "))
    
#     if num > 0:
#         num = math.ceil(num)
#         print(f"x = {num} log(x) = {math.log(num)} ")
#     else:
#         num = math.floor(num)
#         print(f"x = {num} exp(x) = {math.exp(num)}")

#3
# volume_file = int(input("Укажите размер файла для скачивания: "))
# speed_test = int(input("Скорость вашего интернета мб/с: "))
# loading = 0

# if volume_file > speed_test:
#     for sec in range(1, math.ceil(volume_file / speed_test) + 1):
#         loading += speed_test
#         if loading > volume_file:
#             loading = volume_file
#         print(f"Прошло {sec} сек. Скачено {loading} из {volume_file} ({int(loading / volume_file * 100)}%)")
# else:
#     print(f"Прошло 1 сек. Скачено {volume_file} из {volume_file} (100%)")

#4
# x = 10.25
# print(int(round(x - int(x),1)* 10))

#5
# random_planet =  float(input("Введите радиус случайной планеты: "))
# radius_earth = 1.08321 * 10 ** 12
# radius_random_planet = (4/3) * math.pi * (random_planet ** 3)

# if radius_earth > radius_random_planet:
#     print(f"Обьем планеты земля больше в {round(radius_earth / radius_random_planet, 3)} раз")
# elif radius_random_planet > radius_earth:
#     print(f"Обьем планеты земля меньше в {round(radius_random_planet  / radius_earth, 3)} раз")
# else:
#     print(f"Обьем планеты земля {radius_earth} и радиус случайной планеты {radius_random_planet} равны")
    
#6
# horse_x = float(input("Введите местоположение коня: "))
# horse_y = float(input("Введите местоположение коня: "))
# print()

# horse_cell_x = int(horse_x * 10)
# horse_cell_y = int(horse_y * 10)

# point_x = float(input("Введите местоположение точки на доске: "))
# point_y = float(input("Введите местоположение точки на доске: "))
# print()

# point_cell_x = int(point_x * 10)
# point_cell_y = int(point_y * 10)

# print(f"Конь в клетке ({horse_cell_x}, {horse_cell_y}). Точка в клетке ({point_cell_x}, {point_cell_y}).")

# dx = abs(horse_cell_x - point_cell_x)
# dy = abs(horse_cell_y - point_cell_y)

# move = (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
# if move:
#     print("Конь может ходить в эту точку.")
# else:
#     print("Конь не может ходить в эту точку.")

#7
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# max_number = (a + b + abs(a - b)) / 2

# print(f"Наибольшее число: {max_number}")