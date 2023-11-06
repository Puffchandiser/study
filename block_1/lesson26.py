a, b = input(), input()


def my_first_decorator(func):
    def wraper():
        print("обертка заработала")
        d = func()
        otvet = d.upper()
        return otvet

    return wraper


@my_first_decorator
def summa():
    a, b = input(), input()
    c = a + b
    return c


d = summa()
print(d)

# Дано натуральное число x,  1 * 2  + 2*3 + 3*4 + .... + (x-1 * x) x = 5, ответ 40, x = 3, ответ 8
x = int(input())
progressia = 0
for i in range(1, x + 1):
    # 1*1 + 1*2 + 2*3 + 3*4 = 1 + 2 + 6 +12
    progressia = (i - 1) * i + progressia
    progressia += (i - 1) * i
print(progressia)
