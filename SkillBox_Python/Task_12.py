import random
#1
# def summa_n (num):
#     summ = 0
#     for i in range(1,num +1):
#         summ += i
#     print(f"Я знаю, что сумма от 1 до {num} = {summ}")
    
# summa_n(55)
    
#2
# def test(num):
#     if num > 0:
#         positive()
#     else:
#         negative()


# def positive(): print("Позитивное число")


# def negative(): print("отрицательное число")


# test(5)

#3
# def MyCalculator(number):
#     operacia = int(input("Выберете действие:\n"
#                          "1 - сумма цифр числа\n"
#                          "2 - максимальная цифра числа\n"
#                          "3 - минимальная цифра числа\n"))
#     if operacia == 1:
#         summ(number)
#     elif operacia == 2:
#         max_number(number)
#     elif operacia == 3:
#         min_number(number)
#     else:
#         print("Ошибка ввода.")
#         MyCalculator()
        
        
# def summ(num):
#     summ = 0
#     num2 = num
#     while num2:
#         summ += num2 % 10
#         num2 = num2 // 10
#     print(f"сумма цифр числа {num} = {summ}")
#     input("нажмите любую кнопку что бы вернутся в калькулятор: ")
#     MyCalculator(num)


# def max_number(num):
#     max_num = 0
#     num2 = num
#     while num2:
#         search_max = num2 % 10
#         if search_max > max_num:
#             max_num = search_max
#         num2 = num2 // 10
#     print(f"Максимальная цифра в числе {num} это {max_num}")
#     input("нажмите любую кнопку что бы вернутся в калькулятор: ")
#     MyCalculator(num)
    

# def min_number(num):
#     min_num = 9
#     num2 = num
#     while num2:
#         search_min = num2 % 10
#         if search_min < min_num:
#             min_num = search_min
#         num2 = num2 // 10
#     print(f"минимальная цифра в числе {num} это {min_num}")
#     input("нажмите любую кнопку что бы вернутся в калькулятор: ")
#     MyCalculator(num)


# number = int(input("Введите число: "))
# MyCalculator(number)

#4
# def ReNum():
#     number = int(input("Введите число: "))
#     new_number = ""
#     if number > 0:
#         for num in str(number):
#             new_number = num + new_number
#         print("Число наоборот", int(new_number) * 1)
#         ReNum()
#     else:
#         print("Программа завершина")


# ReNum()

#5
# def search_letter(text):
#     num = input("Какую цифру ищем?: ")
#     let = input("Какую букву ищем?: ")
#     num_count = 0
#     let_count = 0
    
#     for i in text:
#         if i == num:
#             num_count += 1
#         elif let.lower() == i.lower():
#             let_count += 1
            
#     print(f" Кол-во цифр {num}: {int(num_count)}")
#     print(f" Кол-во букв {let}: {let_count}")
    
# search_letter("100 лет в обед")

#6
# def gcd(a, b):
#   while b:
#       a, b = b, a % b
#   print(f"Наибольший общий делитель равен {a}")


# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# gcd(num1, num2)

#7
# def guess_the_number():
#     random_num = random.randrange(1,11)
#     number_user = int(input("добро пожаловать в игру 'Угадай число'\n"
#                             "Какое число от 1-10 загаданно?: "))
    
#     while number_user > 10 or number_user <= 0:
#         print("ошибка, введите корректное значение")
#         number_user = int(input("Какое число от 1-10 загаданно?: "))
    
#     if number_user == random_num:
#         print(f"Ты выйграл")        
#     else:
#         print(f"ты проебал! Я загадал число {random_num}")
        
#     game_over = int(input("1 - играть заного\n2 - вернуть в меню\n"))
#     if game_over == 1:
#         guess_the_number()
#     elif game_over == 2:
#         mainMenu()
#     else:
#         game_over = int(input("1 - играть заного\n2 - вернуть в меню\n"))
    

# def rock_paper_scissors():
#     print("Добро пожаловать в игру камень, ножницы, бумага ")
    
#     rd = random.randrange(1,4)
#     ansver_user = int(input("1 - бумага\n2 - камень\n3 - ножницы\n"))
    
#     while ansver_user > 3 or ansver_user <= 0:
#         print("ошибка, введите корректное значение")
#         ansver_user = int(input("1 - бумага\n2 - камень\n3 - ножницы\n"))
    
#     if (ansver_user == 1 and rd == 3) or (ansver_user == 2 and rd == 1) or (ansver_user == 3 and rd == 2):
#         print("Ты проиграл")
#     elif (ansver_user == 1 and rd == 1) or (ansver_user == 2 and rd == 2) or (ansver_user == 3 and rd == 3):
#         print("Ничья")
#     else:
#         print("Ты выйграл")
        
#     game_over = int(input("1 - играть заного\n2 - вернуть в меню\n"))
    
#     if game_over == 1:
#         rock_paper_scissors()
#     elif game_over == 2:
#         mainMenu()
#     else:
#         game_over = int(input("1 - играть заного\n2 - вернуть в меню\n"))
        
        
# def mainMenu():
#     game = int(input("выберете игру!\n"
#                      "1 - камень, ножницы, бумага\n"
#                      "2 - угадай число\n"))
    
#     if game == 1:
#         rock_paper_scissors()
#     elif game == 2:
#         guess_the_number()
#     else:
#         print("неверный код игры")
#         mainMenu()
        
# mainMenu()