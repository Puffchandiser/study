a = input("Сколько человек будет? ")
book = []
for i in range(int(a)):
    people = {}
    name = input("Введите имя ")
    age = int(input("Введите возраст "))
    people["name"] = name
    people["age"] = age
    print("Вы точно хотите добавить", name, "с возрастом", age, "?")
    ask = input()
    if ask == "да":
        book.append(people)
        print(book)
    else:
        print("ошибка")
# example = [{"name": "Дмитрий", "age": 38}, {"name": "Виктор", "age": 41}]
# people["key"] = "value"

# a = []
# for i in range(10):
#     a.append(i)
# print(a)
