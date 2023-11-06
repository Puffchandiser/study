# Циклы:
# a = 21
# while a > 10:
#     print(a)
#     a = a - 1
#     if a == 15:
#         print("Это число было в условии")
#     # a += 1
#     print("Цикл работает")
# print("Цикл прошел")

# a = 0
# while a < 101:
#     print(a)
#     if a == 30:
#         print("ЧИСЛО ЗАМЕЧЕНО")
#         break
#     if a == 50:
#         print("ЧИСЛО ЗАМЕЧЕНО")
#         continue
#     if a == 70:
#         print("ЧИСЛО ЗАМЕЧЕНО")
#         continue
#     a = a + 1
a = 1
while True:
    print(a)
    b = input("Введите действие ")
    if b == "off":
        print("ДО СВИДАНИЯ")
        break
    a = a + 5
    if a > 100:
        break
    if a > 80:
        print("СКОРО КОНЕЦ ЦИКЛА")
