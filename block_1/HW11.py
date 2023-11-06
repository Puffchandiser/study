# # act = input()
# book = []
# for i in range(int(input())):
#     kontakt = input("Введите имя контакта ")
#     tele = int(input("Введите номер телефона "))
#     spisok = {}
#     spisok["kontakt"] = kontakt
#     spisok["tele"] = tele
#     print(spisok)
#     book.append(spisok)
# print(book)

book_phones = {"Федя": "7777777777", "Семен": "55554545555", "Алексей": "55554444444444444478"}
act = int(input())
if act == 1:
    name = input("Введите имя ")
    if name in book_phones:
        print(f"{name}: {book_phones[name]}")
    else:
        for key in book_phones:
            print(f"{key}: {book_phones[key]}")
elif act == 2 or act == 3:
    name = input("Введите имя ")
    phone = input("Телефон: ")
    if name != "" and phone != "":
        book_phones[name] = phone
        for key in book_phones:
            print(f"{key}: {book_phones[key]}")
elif act == 4:
    for key in book_phones:
        print(f"{key}: {book_phones[key]}")
    name = input("Введите имя, которое хотите удалить ")
    if name in book_phones:
        question = input(f"Вы точно хотите удалить этот контакт?: {name}\n ")
        if question == "да":
            check_name = book_phones.pop(name)
            print("Вот новый список контактов:")
            for key in book_phones:
                print(f"{key}: {book_phones[key]}")
        else:
            print("Удаление отменено")
    else:
        print("Ошибка! Заполните поля 'имя' и(или) 'номер телефона'")

# a = {}
# a["Василий"] = 123
# print(a)
# c = input("Введите настоящий номер контакта ")
# a["Василий"] = c
# print(a)
# for i in a:
#     print(f"{i}: {a[i]}")
#
# Действия должны выбираться вводом соответствующих номеров: 1 — показать, 2 — добавить, 3 — изменить, 4 — удалить.
