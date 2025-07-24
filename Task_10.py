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

#3
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
         
#8
