# or - это "или", and - "и"
# if условие1 and условие2 то:
#   блок инструкий выполняется когда и первое, и второе значение возвращает true(верны)

# if условие1 or условие2 то:
#     блок инструкций выполняется когда первое или второе значение возвращает true (верно)

# a = 10
# b = 0
# if a and (b or (a and b)):
#     print("сработало")

# a = 5
# b = 5
# c = 3
# if a > b > c:
#     if a > b:
#         print(a)
#     else:
#         print(b)
# else:
#     if b > c:
#         print(c)

# a = 5
# b = 5
# c = 3
# if not a > b > c:
#     if a > b:
#         print(a)
#     else:
#         print(b)
# else:
#     if b > c:
#         print(c)

# a = "привет"
# b = "привет"
# if b in a:
#     print("эта буква есть в слове")

# x = 20
# if not not not not  x:
#     print("вывело")
