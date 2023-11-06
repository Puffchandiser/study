# a = "123"
# a1 = "привет 123"
# a2 = "привет"
# # print(a.isdigit())
# # print(a1.isdigit())
# # print(a2.isdigit())
#
# print(a.isalpha())
# print(a1.isalpha())
# print(a2.isalpha())

# pin = input("Введи четырехзначный PIN ")
# if pin.isalpha() and len(pin) >= 5:
#     print("PIN должен содержать только 4 цифры")
# else:
#     print("PIN is good")

pin = input("Введи четырехзначный PIN ")
if pin.isdigit() and len(pin) == 4:
    print("PIN is good")
else:
    print("PIN должен содержать только 4 цифры")