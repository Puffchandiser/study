# def my_first_recursion(a):
#     a += 1
#     print(a)
#     if a == 997:
#         print("Рекурсия остановилась ")
#         return
#     return my_first_recursion(a)
# my_first_recursion(a=0)

def my_first_recursion(a, count):
    a += 1
    print(a)
    if a == 997:
        count += 1
        print("Рекурсия остановилась первый раз")
        while count < 4:
            return my_first_recursion(a, count)
            print("Цикл рекурсии окончен")
        return
    return my_first_recursion(a, count)
my_first_recursion(a=0, count=0)