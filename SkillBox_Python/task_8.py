#1
# total_buckwheat = 100
# for month in range(1,100//4 +1):
#     total_buckwheat -= 4
#     print(f" На конец {month} месяца должно остаться {total_buckwheat} кг гречки")
#     print(f"Сьедено каллорий в день: {4000/100*340/30}")

    
#2
# count_debt = int(input('Введите кол-во должников: '))
# sum_debt = 0
# for debt_man in range(0,count_debt, 5):
#     print(f"должник с номером: {debt_man}")
#     debt = int(input("Сколько должен?: "))
#     sum_debt += debt
# print(f"Общая сумма долка: {sum_debt}")


#3
# time = int(input("Сколько времени греем еду?: "))
# time_left = 0
# for reverse_time in range(time, 0-1, -1):
#     if reverse_time == 0:
#         print(f"Ваша еда готова, осторожно горячo!")
#         break
        
#     print(f"осталось {reverse_time} секунд")
#     yes_no = int(input("Продолжаем греть еду?\n1 - Да, еда готова\n0 - нет, еда еще не готова\n "))
#     time_left = reverse_time
    
#     if yes_no == 1:
#         time_left = reverse_time
#         print(f"Ваша еда готова можете забирать {time_left}" )
#         break
    

#4
# a = int(input("введи число а: "))
# b = int(input("введи число б: "))
# c = int(input("введи число с: "))
# iteration = 0
# avg = 0
# for num in range(a, b):
#     if num % c == 0:
#         iteration += 1
#         avg += num 
# print(avg / iteration)


#5
# start = int(input("введи начало отрезка: "))
# stop = int(input("введи конец отрезка: "))
# step = int(input("введи шаг: "))
# for x in range(stop, start - 1, step):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print(f"В точке {x} Функция равна {y}")


#6
# educational_grant = int(input("Стипендия: "))
# expenses = int(input("Расходы на проживание: "))
# summ = 0
# for month in range(1,10+1):
#     summ += expenses - educational_grant
#     print(f"{month}. месяц траты {round(expenses, 1)} не хватает {round(summ, 1)}")
#     expenses *= 1.03
# print(f"{round(summ, 2)} руб. Нужно попросить у родителей")


#7
# stop = int(input("Введите чисто n: "))
# summ = 0
# print(f"При  N = {stop} выразения будет равны ")
# for n in range(stop):
#     print(f"n ={n}") 
#     formula = ((-1) ** n) * (1 / (2 ** n))
#     print(f"(-1) ** {n} * 1/2 ** {n} = {formula}")
#     summ += formula
# print(f"сумма равна:\n s =  {summ}")
    
    
#8
x = int(input("Введите число мальчиков: "))
y = int(input("Введите число девочек: "))
man = "B "
woman ="G "
row = ""
for i in range((x+y)//2):
    print(i)
    if x == y:
        row += man + woman
    elif x > y:
        row += man + woman + man 
        
print(row)