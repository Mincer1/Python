# прицел
# for row in range(20):
#     for col in range(50):
#         if col == 25:
#             print("|", end = "")
#         elif row == 9:
#             print("-", end = "")
#         else:
#             print(' ', end = "")
#     print()



# Врата
# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print("-", end = "")
#         elif col == 0 or col == 29:
#             print("|", end = "")
#         else:
#             print(" ", end = "")
#     print()

#Трасса
# for row in range(20):
#     for col in range(50):
#         if col == 25:
#             print("|", end = "")
#         # elif row == 9:
#         #     print("-", end = "")
#         elif col == row + 30:
#             print("\\", end = "")
#         elif col == -row + 20:
#             print("/", end = "")
#         else:
#             print(' ', end = "")
#     print()

# matrix = 5
# for row in range(matrix, 0, -1):
#     for col in range(matrix):
#         if row > col+1:
#             print(0, end =" ")
#         elif row < col+1:
#             print(2, end = " ")
#         else:
#             print(1, end = " ")
#     print()

# matrix = 5
# for row in range(matrix+1):
#     for col in range(row, matrix+1, 1):
#         print(col, end = "\t")
#     print()