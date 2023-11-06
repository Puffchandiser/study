# def func():
#     print("функция работает")
# func()
# def func1():
#     x = 1 + 2
#     return x
# func1()

# otvet = ""
# a = input()
# b = input()
# def func2(a,b):
#     global otvet
#     otvet = a + " " + b
#     otvet = f"{a} {b}"
# otvet_iz_func2 = func2(a,b)
# print(otvet)

# C > f, f > c
# messure = input("Впишите меру измерения температуры из которой хотите перевести ")
# temperature = int(input("Введите значение "))
# def perevod():
#     if messure == "f":
#         otvet = temperature * 25 / 9 + 32
#     elif messure == "c":
#         otvet = 5 /9 * (temperature - 32)
#     else:
#         otvet = "Что-то пошло не так"
#     return otvet
# print(perevod())

temperature = input("Введите значение температуры со шкалой измерения ")
temperature_splited = temperature.split()
def perevod():
    if "c" in temperature_splited or "C" in temperature_splited:
        otvet = f' {int(temperature_splited[0]) * 9 / 5 + 32} F'
    elif "f" in temperature_splited or "F" in temperature_splited:
        otvet = f' {5 * (int(temperature_splited[0]) - 32) / 9} C'
    else:
        otvet = "Что-то пошло не так"
    return otvet
print(perevod())