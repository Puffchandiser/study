# def summa():
#     a = int(input("Введите первое число "))
#     b = int(input("Введите второе число "))
#     c = a + b
#     print(c)
# summa()
# def raznost():
#     pass
# raznost()
# def delenie():
#     print("Заработала функция деления ")
# delenie()
# def umnojenie():
#     print("Фунцкия умножения")
#     delenie()
# f = umnojenie()
# print(f)
# def eto_funkcia(f):
#     f = f + 100
#     return f
# c = 20
# b = eto_funkcia(c)
# print(b)

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = input("Впишите действие ")
def slojenie(a,b):
    x = a + b
    return x
def raznost(a,b):
    x = a - b
    return x
def umnojenie(a,b):
    x = a * b
    return x
def delenie(a,b):
    x = a / b
    return x
if c == "+":
    otvet = slojenie(a, b)
    print(otvet)
elif c == "*":
    otvet = umnojenie(a, b)
    print(otvet)
elif c == "-":
    otvet = raznost(a, b)
    print(otvet)
elif c == "/" or ":":
    if b == 0:
        print("Делить на ноль нельзя!!!")
    else:
        otvet = delenie(int(a), int(b))
        print(otvet)


