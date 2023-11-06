#1991/10/31 и 1991/10/11
# a = str(input("Введите год/месяц/день рождения "))
# b = str(input("Введите год/месяц/день рождения "))
# a1 = a[0:4]
# b1 = b[0:4]
# a2 = a[6:7]
# b2 = b[6:7]
# a3 = a[9:10]
# b3 = b[9:10]
# if a1 > b1:
#     print("второй человек старше")
# elif a1 < b1:
#     print("первый человек старше")
# elif a1 == b1 and a2 > b2:
#     print("второй человек старше")
# elif a1 == b1 and a2 < b2:
#     print("первый человек старше")
# elif a1 == b1 and a2 == b2 and a3 > b3:
#     print("первый человек старше")
# elif a1 == b1 and a2 == b2 and a3 < b3:
#     print("второй человек старше")
# else:
#     print("вы ввели неверные данные")
text = 'Введите любое слово: '
text += '\nИли введите exit для выхода: '

active = True
while active:
    message = input(text)
    if message == 'exit':
        active = False
    else:
        print(message)
