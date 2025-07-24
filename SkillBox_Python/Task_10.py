#1
# for row in range(6):
#     for col in range(0,6):
#         if col == 0:
#             print(row + col, end = "\t")
#         else:
#             print(row + col * 2, end = "\t")
#     print()

#2
# matrix= 6
# for row in range(1, matrix):
#     for col in range(row):
#         print(row, end = " ")
#     print()

#4
# number = int(input("Введите кол-во цифр: "))
# count_num = 0

# for i in range(number):
    
#     num = int(input("Введите число: "))
#     while num < 1:
#         num = int(input("Введите число больше 0: "))
#     proverka = 0
    
#     for x in range(1,100):
#         if num % x == 0:
#             proverka +=1
            
#     if proverka == 2:
#         count_num += 1
#         proverka = 0
            
# print(count_num)
         
#5
# number = input("Введите число: ")
# summ = 0
# count = 0
# for num in number:
#     summ += int(num)
#     count += 1
# print(f"сумм чисел = {summ}\nкол-во {count}")

#6
# height = int(input("Введите высоту треугольника: "))

# for row in range(height):
#     spaces = height - row - 1 #3
#     hashtags = 2 * row + 1 #1
#     line = ' ' * spaces + '#' * hashtags #   
#     print(line)

#7
# levels = int(input("Введите количество уровней пирамиды: "))
# odd_number = 1

# for line in range(levels):
#     spaces = levels - line - 1
#     print("   " * spaces, end="")

#     for number in range(line+1):
#         print(odd_number, end="    ")
#         odd_number += 2

#     print()
#8
# depth = int(input("Введите глубину ямы: "))

# for line in range(depth):

#     for left_number in range(depth, depth-line-1, -1):
#         print(left_number, end="")
#     point_count = 2 * (depth - line - 1)
#     print("." * point_count, end="")

#     for right_number in range(depth - line, depth+1):
#         print(right_number, end="")

#     print()