import greeting, menu, all_read, create

FILENAME = "notes.csv"

greeting.greeting()
flag = True

while flag:
    num = menu.menu()
    if num == "1":
        all_read.read_notes(FILENAME)
    elif num == "2":
        create.create_note(FILENAME)
    elif num == "0":
        print("\nДо встречи!\n")
        flag = False
    else:
        print("\nВведено неверное значение\n")