from colorama import init

init()
from colorama import Fore, Back, Style

print(Fore.BLACK + 'some red text')
print(Back.CYAN + 'and with a blue background')
print(Style.BRIGHT + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
