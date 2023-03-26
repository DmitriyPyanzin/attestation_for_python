import csv

def filtr_for_id(FILENAME):
    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            print(f"{row[0]}")
    id = input("\nВведите ID заметки: ")

    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        count = 0
        for row in file_reader:
            if id == row[0]:
                print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
                count += 1
        if count == 0:
            print(f"Такого ID {id} нет")

    input('\nНажмите enter\n')