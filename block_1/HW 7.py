from colorama import init

init()
from colorama import Fore, Back, Style

pin = (input("Придумайте PIN-код "))
# if len(pin) >= 8 and pin.isalpha() and pin.islower() == True or pin.isdigit() and len(pin) >= 8:
#     print(Fore.BLACK, Style.BRIGHT, Back.LIGHTGREEN_EX, "PIN слабый", Style.RESET_ALL)
# elif len(pin) >= 8 and pin.islower() == True and pin.isalnum():
#     print(Fore.BLACK, Style.BRIGHT, Back.LIGHTYELLOW_EX, "PIN средний", Style.RESET_ALL)
# elif len(pin) < 8:
#     print (Fore.RED, Style.DIM, Back.LIGHTCYAN_EX, "PIN ОЧЕНЬ СЛАБЫЙ", Style.RESET_ALL)
# else:print(Fore.BLACK, Style.BRIGHT, Back.LIGHTGREEN_EX, "PIN слабый", Style.RESET_ALL)
#     print(Fore.BLACK, Style.BRIGHT, Back.LIGHTRED_EX, "PIN хороший", Style.RESET_ALL)

# elif len(pin) >= 8 and pin.isupper() == False and pin.islower() == False and pin.isnumeric() == True:
#     print(Fore.BLACK, Style.BRIGHT, Back.LIGHTRED_EX, "PIN хороший", Style.RESET_ALL)
# else:
#     print(Fore.BLACK, Style.DIM, Back.LIGHTCYAN_EX, "PIN ОЧЕНЬ СЛАБЫЙ!!!", Style.RESET_ALL)

if len(pin) >= 8 and not pin.isupper() and not pin.islower() and not pin.isdigit() and not pin.isalpha():
    print(Fore.BLACK, Style.BRIGHT, Back.LIGHTRED_EX, "PIN хороший", Style.RESET_ALL)
elif len(pin) >= 8 and pin.islower() and not pin.isalpha():
    print(Fore.BLACK, Style.BRIGHT, Back.LIGHTYELLOW_EX, "PIN средний", Style.RESET_ALL)
elif len(pin) >= 8 and (pin.isalpha() or pin.isdigit()):
    print(Fore.BLACK, Style.BRIGHT, Back.LIGHTGREEN_EX, "PIN слабый", Style.RESET_ALL)
else:
    print(Fore.BLACK, Style.DIM, Back.LIGHTCYAN_EX, "PIN ОЧЕНЬ СЛАБЫЙ!!!", Style.RESET_ALL)
