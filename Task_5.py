# 1
# experience_point = int(input("Введите число опыта: "))
# lvl = 1
# if experience_point >= 1000 and experience_point < 2500:
#     lvl +=1
# elif experience_point >= 2500 and experience_point < 5000:
#     lvl +=2
# else:
#     lvl +=3
# print(f"Ваш уровень {lvl}")
    

# 2
# x = int(input("Введите х: "))
# if x > 0:
#     x -=12
# elif x == 0:
#     x = 5
# else:
#     x **= 2
# print(f"Y равен {x}")
 
    
#3
# top = int(input("Введите место в списке: "))
# if top >0 and top < 10:
#     print("Поздравляю вы поступили!")
#     point = int(input("Введите кол-во баллов за экзамен: "))
#     if point >= 290:
#         print("Бонус вам будет степендия!")
#     else:
#         print("Без стипендии ((")
# else:
#     print("Ты не поступил!")


#4
# rating = int(input('Что получил по математике? '))
# if rating == 2 or rating == 3:
#     print('Плохо. Марш учиться!')
# else:
#     print('Молодец! Можешь отдохнуть.')


#5
# num_1 = 1
# num_2 = 3
# num_3 = 1
# if num_1 == num_2 or num_1 == num_3:
#     if num_2 == num_3:
#         print("вcе совпадают")
#     else:
#         print("два совпадают")
# elif num_2 == num_3 and (num_1 != num_3 or num_1 != num_2):
#     print("два совпадают")
# else:
#     print("все числа разные")


#6
# apartment_S = int(input("Какая площадь квартиры?: "))
# price_apartment = int(input("Стоимоть квартиры: "))
# if (apartment_S >= 100 and price_apartment <= 10) or apartment_S >= 80 and price_apartment <= 7:
#     print("Хата подходит!")
# else:
#     print("хата не подходит")



#7 v_1
# time_now = int(input("Сколько время?: "))
# if 8 <= time_now < 10 or 12 <= time_now < 14 or 15 <= time_now < 18 or 20 <= time_now < 22:
#     print("посылку можно забрать!")
# else:
#     print("Хуй угадал")

# #7 v_2 через not
# time_now = int(input("Сколько время?: "))
# if not((time_now >= 8 and time_now < 10) or (time_now >= 12 and time_now < 14) or (time_now >= 15 and time_now < 18) or (time_now >= 20 and time_now < 22)):
#     print("Хуй угадал")
# else:
#     print("забирай")