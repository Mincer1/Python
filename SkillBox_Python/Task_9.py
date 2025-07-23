#1
# pirates = 0
# for i in range(1, 10+1):
#     print(f"{i} пират")
#     karamba = input("Какой девис?: ")
#     if karamba.lower() == "карамба":
#         pirates += 1
# print(pirates)    

#2
# text = input("Введите текс: ")
# count_text = 0
# for symbol in text:
#     count_text += 1
#     if symbol == '*':
#         print(f"символ '*' стоит на позиции  {count_text}")
#         break

#3
# count_row = 5#int(input("Введите количество рядов: "))
# count_seats = 7#int(input("Введите количество сиденей в ряде: "))
# distance = 3#int(input("Введите кол-во меров между рядами: "))
# for row in range(count_row):
#     print("=" * count_seats, "*" * distance, "=" * count_seats)
    
    
#4

# north_south = 8
# west_east = 10

# while True:
#     comand = input("куда движимся?: ")
#     if comand == "w" and north_south < 15:
#         north_south += 1
#     elif comand == "s" and north_south > 0:
#         north_south -= 1
#     elif comand == "d" and west_east < 20:
#         west_east += 1
#     elif comand == "a" and west_east > 0:
#         west_east -= 1
#     else:
#         break
        
#     print(f"марсоход находится на позиции: {north_south},{west_east}")


#5
# text = input("Введите текст: ")
# big_symvol = 0
# count_symvol = 0
# for symvol in text:
#     if symvol == " ":
#         big_symvol = count_symvol if count_symvol > big_symvol else big_symvol
#         count_symvol = 0
#     else:
#         count_symvol += 1

# big_symvol = count_symvol if count_symvol > big_symvol else big_symvol
# print(f"самое длинное слово: {big_symvol}")
        
#6
# sum_milk = 0
# for i in range(1,10+1):
#     comand = input(f"стоило №{i} занято?:b-yes a-no :  ")
#     if comand == "b":
#         sum_milk += i * 2
# print(f"за сегодня {sum_milk}л молока")
        
        
#7
# code = "shacnidw"#input("Введите шифр: ")
# decoder = ""
# part_two = ""
# flag = True
# for symvol in code:
#     if flag:
#         decoder += symvol
#         flag = False
#     else:
#         part_two = symvol + part_two
#         flag = True 
             
# print(f"расшифровка: {decoder + part_two}")

#8
# word = input("Введите палиндром: ")
# palindrom = ""

# for symvol in word:
#     palindrom = symvol + palindrom
    
# if word == palindrom:
#     print("Да, это полиндром!")
# else:
#     print("Нет, это не палиндром")