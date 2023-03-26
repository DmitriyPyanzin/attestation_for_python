import csv

def filtr_for_date(FILENAME):
    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            print(f"{row[3]}")
        date = input("\nВведите время создания заметок: ")

    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        count = 0
        for row in file_reader:
            if date == row[3]:
                print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
                count += 1
        if count == 0:
            print(f"\nТакой даты {date} нет")

    input('\nНажмите enter\n')