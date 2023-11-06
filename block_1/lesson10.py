# a, b   a <= b  5 10
a = int(input("Введи число 1 "))
b = int(input("Введи число 2 "))
cnt = 0
while a <= b:
    print(a)
    a += 1

# # x = 5 то ответ - 1+2+3+4+5 или 1+2+3+x
# x = int(input("Введи число "))
# cnt = 0
# cnt_sum = 0
# while cnt <= x:
#     print(cnt, cnt_sum)
#     cnt += 1
#     cnt_sum = cnt_sum + cnt
