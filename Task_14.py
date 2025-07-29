# nums_list = []

# N = int(input('Кол-во чисел в списке: '))

# for _ in range(N):

#  num = int(input('Очередное число: '))

#  nums_list.append(num)


# maximum = max(nums_list)

# minimum = min(nums_list)


# print('Максимальное число в списке:', maximum)

# print('Минимальное число в списке:', minimum)

#2
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

#3
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
