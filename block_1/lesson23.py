# в последовательности натуральных чисел опредлить минимальное число, оканчивающееся на 4.
# Программа получает количество чисел, затем сами числа. В последовательности всегда есть число, оканчивающееся на 4.
# Кол-во чисел не больше 1000. Введенные числа не превышают 30.000. Программа должно вывести минимальное число.
# n = int(input())
# listik = []
# max_count_n = 1000
# max_amount_numbers = 30000
# last_number = 4
# if n <= max_count_n:
#     for i in range(n):
#         numbers = int(input())
#         if numbers % 10 == last_number and numbers <= max_amount_numbers:
#             listik.append(numbers)
#     a = min(listik)
# else:
#     a = []
# print(a)

n = int(input())
max_count_n = 1000
max_amount_numbers = 30000
last_number = 4
otvet = max_amount_numbers
if n <= max_count_n:
    for i in range(n):
        numbers = int(input())
        if numbers % 10 == last_number and numbers <= otvet:
            otvet = numbers
print(otvet)