from colorama import init
init()
from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# a = "123"
# a1 = "привет 123"
# a2 = "привет"
# print(a.isdigit())
# print(a1.isdigit())
# print(a2.isdigit())
print(Back.YELLOW, end="")
print(Style.BRIGHT, end="")
a = input(Fore.BLACK + "Введи первое число ")
b = input("Введи второе число ")
c = str(input("Введи математическое действие "))
print(Style.RESET_ALL)
if c == "+":
    d = a + b
    if a.isalpha() or b.isalpha():
        print(Fore.BLACK, Back.RED, "ОШИБКА!!!", Style.RESET_ALL)
    print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, d, Style.RESET_ALL)
elif c == "//":
    d = a//b
    print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, d, Style.RESET_ALL)
elif c == "%":
    d = b/100 * a
    print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, d, Style.RESET_ALL)
elif c == "-":
    d = a - b
    print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, d, Style.RESET_ALL)
elif c == "*":
    d = a * b
    print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, d, Style.RESET_ALL)
elif c == "/":
    if b == 0:
        print(Back.LIGHTWHITE_EX, Fore.RED, Style.NORMAL, "ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ!",Style.RESET_ALL)
    else:
        d = a / b
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, d, Style.RESET_ALL)
elif c == "^":
    d = a ** b
    print(d)
else:
    print(Back.LIGHTWHITE_EX, Fore.RED, Style.NORMAL, "ВЫ ВВЕЛИ НЕКОРРЕКТНЫЙ СИМВОЛ",Style.RESET_ALL)



