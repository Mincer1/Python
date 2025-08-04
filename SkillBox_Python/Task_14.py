#1.1
# numbers_list = [3,7,5]

# while True:

#  number = int(input('Новое число: '))

#  numbers_list.append(number)

#  print('Текущий список чисел:', numbers_list)

#  for i in numbers_list:

#    print(i ** 2, i ** 3, i ** 4)

#  print()

#1.2
# numbers = []
# for i in range(101):
#     numbers.append(i)
# print(numbers)

#1.3
# count_id = int(input("сколько сотрудников?: "))
# employee_id = []

# for _ in range(count_id):
#     id = int(input("id сотрудника: "))
#     employee_id.append(id)

# search_id = int(input("Какой id ищем?: "))

# if search_id in employee_id:
#     print("Сотрудник работает!")
# else:
#     print("не работает")

#2.1
# nums_list = []

# N = int(input('Кол-во чисел в списке: '))

# for _ in range(N):

#  num = int(input('Очередное число: '))

#  nums_list.append(num)


# maximum = max(nums_list)

# minimum = min(nums_list)


# print('Максимальное число в списке:', maximum)

# print('Минимальное число в списке:', minimum)

#2.2
# summa_index = 0
# num_list = []
# count_num = int(input("Введите кол-во чисел в списке: "))

# for num in range(count_num):
#     num_list.append(int(input(f"Введите {num + 1} число: ")))
    
# delitel = int(input("Введите делитеть: "))

# for i, number in enumerate(num_list):
#     if number % delitel == 0:
#         print(f"Индекс числа {number}: {i}")
#         summa_index += i
        
# print(f"Сумма индексов {summa_index}")

#2.3
# count_dog = int(input("Сколько собак учавствуют в бегах?: "))
# dogs = []
# for i in range(count_dog):
#     dogs.append(int(input(f"Введите сколько очков у {i + 1} собаки: ")))

# print(dogs)

# max_index = 0
# min_index = 0

# for i, scors in enumerate(dogs):
#     if max(dogs) == scors:
#         max_index = i
#     elif min(dogs) == scors:
#         min_index = i

# dogs[max_index], dogs[min_index] = dogs[min_index], dogs[max_index]
# print(dogs)

#3.1
# words = input("Введите список: ")
# words_list = list(words)
# count_simvol = 0

# for i, simvol in enumerate(words_list):
#     if simvol == ":" :
#         words_list[i] = ";"
#         count_simvol +=1

# for i in words_list:
#     print(i, end ="")
# print(f"Кол-во замен: {count_simvol}")

#3.2
# text_list = list(input("Введите текст: "))
# num_str = int(input("Введите номер строки: "))

# print(f"Слева символ {text_list[num_str - 2]}\nCправа смивол: {text_list[num_str]}")

# if text_list.count(text_list[num_str-1]) > 1:
#     print("Есть как минимму еще один такой же символ")
# else:
#     print("Таких же символов больше нет")

#3.3
# words_list = []
# count_list = [0,0,0]
# for i in range (3):
#     words_list.append(input(f"Введите {i+1} слово: "))
    
# text = input("Введите слово из текста: ")
# while text != "конец":
#     for i, sym in enumerate(words_list):
#         if text == sym:
#             count_list[i] += 1
    
#     text = input("Введите слово из текста: ")
    
# print(f"Подсчет слов в тексе:\n")

# for i, words in enumerate(words_list):
#     print(f"{words}: {count_list[i]}")