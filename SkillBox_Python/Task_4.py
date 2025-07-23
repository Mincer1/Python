#1
# rain = int(input("На улице идет дождь?: "))
# if rain == 1:
#     print("На улице идет дождь!")
# else:
#     print("На улице нет дождя")


#2
# ru = int(input("Введите количество баллов по русскому языку: "))
# math = int(input("Введите количество баллов по математике: "))
# inf = int(input("Введите количество баллов по информатике: "))
# summ = ru + math + inf
# if summ > 220:
#     print("Ты прошел на бюджет")
# else:
#     print("Ты не прошел на бюджет")


#3
# num = int(input("Введите число: "))
# if num % 2 == 0:
#     print("отдыхай")
# else:
#     print("Работай")

#4
# product_1 = int(input("Введите стоимость первого товара: "))
# product_2 = int(input("Введите стоимость второго товара: "))
# product_3= int(input("Введите стоимость третьего товара: "))
# check = product_1 + product_2 + product_3
# if check > 10000:
#     check -= check * 10 / 100 
#     print(f"сумма чека {check}")
# else:
#     print(f"сумма чека {check}")
# print("Хорошего дня !")

#5 
# num = int(input("Введите число: "))
# if num < 0:
#     print(f"Ввели {num} , ответ {abs(num)}")
# else:
#     print(f"Ввели {num}, ответ {num}")

#6
# num_1 = int(input("Введите число 1: "))
# num_2 = int(input("Введите число 2: "))
# if num_1 >= num_2:
#     print(f"Разница {num_1 - num_2}, игрок платит!")
# else:
#     print(f"Разница {num_2 - num_1}, владелец платит!")
# print("game over")

#7
# hours_work = int(input("Введите отработанные часы: "))
# remainder_kred = int(input("Введите остаток по кредиту: "))
# expenses_food = int(input("Введите траты на еду: "))
# formula_income = ((200 * hours_work) / 2**3) + hours_work
# if formula_income >= expenses_food + remainder_kred:
#     formula_income -= expenses_food+ remainder_kred
#     print(f"Денег хватает! Остаток {formula_income}")
# else:
#     print(f"Денег не хватит, работай больше!")

#8
# num_1 = int(input("Введите 1 число: "))
# num_2 = int(input("Введите 2 число: "))
# num_3 = int(input("Введите 3 число: "))
# max = 0
# if num_1 > num_2:
#     max = num_1
# else:
#     max = num_2
# if max < num_3:
#     max = num_3

# print(max)
