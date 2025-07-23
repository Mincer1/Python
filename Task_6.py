#1
# num = int(input("Введите число: "))
# stepen = 1
# while stepen <= num:
#     print(f"{stepen} = {stepen ** 3}")
#     stepen +=1


#2
# name_debtor = input("Имя должника?: ")
# debt = int(input("Сколько должен?: "))
# print(f"{name_debtor} верни {debt} рублей")
# while debt >= 0:
#    debt_repayment = int(input("Сколько денег внес?: "))
#    debt -= debt_repayment
#    if debt <= 0:
#        print(f"Отлично, {name_debtor}! Вы погасили долг. Спасибо!")
#        break
#    print("чет мало!" )
                        

#3
# num = int(input("Введите число: "))
# count_num = 1 if num != 0 else 1
# while num // 10 != 0:
#     num = num // 10
#     count_num += 1
# print(count_num)    

#4
# flag = True
# count_plus = 0
# count_minus = 0
# while flag:
#     grade = int(input("Введите оценку: "))
#     if grade > 0:
#         count_plus += 1
#     elif grade < 0:
#         count_minus +=1
#     else:
#         flag = False
    
# print(f"Кол-во положительных чисел: {count_plus}\nКол-во отрицательных чисел: {count_minus}")

#5
# hour = 0
# task_count = 0
# shop =False
# print("Начался восьмичасовой рабочий день.")
# while hour < 8:
#     hour +=1
#     task_count += 1
#     print(f"час: {hour}")
#     print(f"Сколько задач решит Максим? {task_count}")
#     if shop == False:
#         shop += int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#         # if coll == 1:
#         #     shop = True
# print(f"Рабочий день закончился. Всего выполнено задач: {task_count}")
# if shop:
#     print("Нужно зайти в магазин.")