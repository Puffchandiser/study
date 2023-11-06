# def example():
#     a = 5
#     return a
# example()
#
# b = 1000 + example()
#
# a = int(input())
# b = int(input())
# y = 10
#
# def plus(a, b):
#     # global y
#     c = a + b + y
#     # y += c
#     return c
# print(y)
#
# print(plus(a, b))

a = ["Артем", "Денис", "Владимир", "Степан", "Алексей", "Дмитрий"]
x = ["Alex", "Sam", 'Bob', "Jackob"]
b = input()
# def name(*args):
# def name(*j):
#     print("функция заработала")
#     # print(j)
#     if b in j or b in x:
#         print("Имя найдено")
#     else:
#         print("Такого имени в списке нет")
# c = name("Артем", "Денис", "Владимир", "Степан", "Алексей", "Дмитрий")
# def slot(**kwargs):
# def slot(b, x, **kwargs):
#     print(kwargs)
# slot(b, x, name="Василий", age=48, city="Moscow")
a1 = "Первая переменная"
a2 = "Вторая переменная"
def words(a1,a2):
    print(a1)
    print(a2)
    print("\n\n")
words(a1,a2)
words(a2,a1)
words(a1=a1, a2=a2)
words(a2=a2,a1=a1)