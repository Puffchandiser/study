# # (venv) PS C:\Users\User\PycharmProjects\study> dir
#
# #  Каталог: C:\Users\User\PycharmProjects\study
# #
# #
# # d-----      Ср 14.06.23     21:51                venv
# # -a----      Ср 14.06.23     21:52            544 main.py
#
#
# # (venv) PS C:\Users\User\PycharmProjects\study> cd block_1
# # (venv) PS C:\Users\User\PycharmProjects\study\block_1> cd ..
# # (venv) PS C:\Users\User\PycharmProjects\study> cd block_1
# # (venv) PS C:\Users\User\PycharmProjects\study\block_1> python HW1.py
#
a = "1 привет, это 'чудо'"
b = "2 пока"
# Срезы - название переменной + [start:stop:step]
c = a[0]
c1 = a[0:1]
c11 = a[:1]
c2 = b[-6]
c3 = a[2:8]
c4 = a[:]
c5 = a[::-1]
# print(c)
# print(c1)
# print(c2)
# print(c3)
print(c4)
print(c5)

# a = "Привет, меня зовут Александр"
# a1 = "Мне 26 лет"
# name = a[19:]
# age = a1[4:6]
# print(name, age)

# методы строк
a = "привет "
b = a.upper()
b1 = a.lower()
x = a.count("П")
x1 = a.replace("п","А")
x2 = len(a)
print(b)
print(x2)