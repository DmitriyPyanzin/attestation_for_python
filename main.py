import greeting, menu, all_read, create, filtration_for_date, filtration_for_id, redactor

FILENAME = "notes.csv"

greeting.greeting()
flag = True

while flag:
    num = menu.menu()
    if num == "1":
        all_read.read_notes(FILENAME)
    elif num == "2":
        create.create_note(FILENAME)
    elif num == "3":
        filtration_for_date.filtr_for_date(FILENAME)
    elif num == "4":
        filtration_for_id.filtr_for_id(FILENAME)
    elif num == "5":
        redactor.redactor(FILENAME)
    elif num == "0":
        print("\nДо встречи!\n")
        flag = False
    else:
        print("\nВведено неверное значение\n")