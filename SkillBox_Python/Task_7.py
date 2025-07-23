#1
# even_positive = 0
# for debt in 5, 8 , 9 , -8 , -10, 10, 42, -99 , 2, -88:
#     if debt > 0 and debt % 2 == 0:
#         even_positive += 1
# print(f"положительных и четных чисел: {even_positive}")
    
#2
# sum_income = 0
# total_month = 0
# for month in range(1, 3 + 1):
#     income = int(input(f"Какая зп за {month} месяц?: "))
#     sum_income += income
#     total_month += 1
# print(f"средня зп за {total_month} месяцев: {round(sum_income / total_month)}")

#3
# num = int(input("Введите число: "))
# n = 1
# for i in range(1, num +1):
#     n *= i
# print(f"факториал числа {num} равен {n}")
    

#4
# total_students =int(input("Сколько сегодня учеников?: "))
# three = 0
# four = 0
# five = 0
# for students in range(1, total_students +1):
#     grade = int(input(f"Какая оценка у {students} ученика?: "))
#     if grade == 3:
#         three += 1
#     elif grade == 4:
#         four += 1
#     else:
#         five += 1
# print(f"сегодня\n{three} тройки\n{four} четверок\n{five} пятерок ")


#5
# a = 3
# b = 33
# avg_num = 0
# for num in range(a, b + 1):
#     if num % 3 == 0:
#         avg_num += num
# print(avg_num / (b-3))


#6
# for num in range(10, 100):
#     digit1 = num // 10
#     digit2 = num % 10
#     if num == 3 * digit1 * digit2:
#         print(num)

#7
# total_cards = int(input("Введите число карт: "))
# sum_cards = 0
# x = 0 + total_cards
# for cards in range(1,total_cards):
#     x += cards
#     num_cards = int(input("Введите номер карты: "))
#     sum_cards += num_cards
# print(f"Номер пропавшей карты: {x - sum_cards}")