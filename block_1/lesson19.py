# k = 125
# k1 = 5
# for i in range(k1, k + 1):
# #     print(i)
# while True:
#     print(k1)
#     k1 = k1 + 1
#     if k1 == 125:
#         break

# p = 100
# p1 = 0
# while True:
#     print(p)
#     p = p - 1
#     if p < p1:
#         break

# даны натуральные числа a и b. Используя только операции + и - нужно вывести остаток а на b нацело и дробную часть.

a = int(input())
b = int(input())
count = 0
ostatok = count * b
while a >= b:
    a = a - b
    count += 1
print(count, a)

# if ostatok != a:
#         print(a - ostatok)
