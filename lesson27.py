import datetime
def count_time(func):
    def wraper(*args, **kwargs):
        start = datetime.datetime.now()
        x = func(*args, **kwargs)
        finish = datetime.datetime.now()
        time_passed = finish - start
        print(time_passed)
        return x
    return wraper
#
# @count_time
# def func():
#     wwod = input("Введите любой символ ")
#     print(wwod)
# otvet = func()

# Дано натуральное число x, вычисли (1**1) - (2**2) + (3**3) - (4**4) + (...) + (x**x)
@count_time
def progressia():
    x = int(input())
    count = 0
    for i in range(1, x + 1):
        if i % 2 == 0:
            count -= (i ** i)
        else:
            count += (i ** i)
    print(count)
    return x
x = progressia()
@count_time
def progressia_bez_iks():
    count = 0
    for i in range(1, int(x) + 1):
        if i % 2 == 0:
            count -= (i ** i)
        else:
            count += (i ** i)
    print(count)
    print(x)
otvet = progressia_bez_iks()

