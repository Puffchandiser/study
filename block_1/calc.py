from colorama import init
init()
from colorama import Fore, Back, Style
print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, "0", Style.RESET_ALL)
print(Back.YELLOW, end="")
print(Style.BRIGHT, end="")
a = int(input(Fore.BLACK + "Первое число "))
# c = input("Действие ")
# b = int(input("Второе число "))
while True:
    c = input("Действие ")
    b = int(input("Число "))
    if c == "+":
        n = a + b
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, n, Style.RESET_ALL)
        a = n
    if c == "//":
        n = a//b
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, n, Style.RESET_ALL)
    elif c == "%":
        d = b/100 * a
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, n, Style.RESET_ALL)
        n = a // b
    elif c == "-":
        d = a - b
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, n, Style.RESET_ALL)
    elif c == "*":
        d = a * b
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, n, Style.RESET_ALL)
    elif c == "/":
        if b == 0:
            print(Back.LIGHTWHITE_EX, Fore.RED, Style.NORMAL, "ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ!",Style.RESET_ALL)
        else:
            d = int(a) / int(b)
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, int(n), Style.RESET_ALL)
    elif c == "^":
        d = a ** b
        print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT, n, Style.RESET_ALL)
    # else:
    #     print(Back.LIGHTWHITE_EX, Fore.RED, Style.NORMAL, "ВЫ ВВЕЛИ НЕКОРРЕКТНЫЙ СИМВОЛ",Style.RESET_ALL)