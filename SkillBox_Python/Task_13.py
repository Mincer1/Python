#1

#2
# def maximum_two (num1, num2):
#     max_num = max(num1,num2)
#     return max_num


# def maximum_three (num1, num2):
#     max_num = max(num1,num2)
#     return max_num

# num1 = 551
# num2 = 88
# num3 = 44

# print(f"Максимальное число из трех: {max(num1,num2,num3)}")

#3
# def polindrom (num):
#     num = int(str(num)[::-1])
#     return num

# n = 345
# k = 228
# print(f"Первое число наоборот: {polindrom(n)}\n"
#       f"Второе число наоборот: {polindrom(k)}\n"
#       f"сумма: { polindrom(n) + polindrom(k) }\n"
#       f"сумма наоборот { polindrom(polindrom(k) + polindrom(n)) }")

#4
# def count_numbers (num):
#     count_num = int(len(str(num)))
#     return count_num


# def change_number (num):
#     first_num = str(num)[:1] #находим первую цифру в числе
#     last_num = str(num) [int(len(str(num)))-1:] #находим последнюю цифру числе 
#     mid_num = str(num)[1:int(len(str(num))-1)] # находим промежут числа
#     new_num = last_num + mid_num + first_num # клеим новое число
#     return int(new_num)


# def main ():
#     num1 = int(input("введите число больше 3 цифр: "))
#     num2 = int(input("введите число больше 4 цифр: "))
#     if count_numbers(num1) == 3 and count_numbers(num2) == 4:
#         print(f"Число 1 :{change_number(num1)}\n"
#               f"Число 2 :{change_number(num2)}\n"
#               f"сумма чисел: { change_number(num1) + change_number(num2) }")
        
#     else:
#         print("Ошибка ввода")
#         main()


# main()

#5
amplituda = 1
stop = 0.1
add_amplitude = 0.084
count_colebal = 0
while amplituda > stop:
    amplituda -= add_amplitude
    add_amplitude -= add_amplitude * add_amplitude
    count_colebal += 1
print(f"колебаний: {count_colebal}")
#6