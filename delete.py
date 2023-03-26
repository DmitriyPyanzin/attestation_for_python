import csv
import os

def delete_note(FILENAME):
    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            print(f"{row[0]}")
    id = input("\nВведите ID заметки, которую хотите удалить: ")

    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        count = 0
        for row in file_reader:
            if id == row[0]:
                count += 1
        if count == 0:
            print(f"Такого ID {id} нет")

    with open("tmp.csv", mode="w", encoding="utf_8") as new_file:
        with open(FILENAME, encoding="utf_8") as source:
            source_reader = csv.reader(source)
            for row in source_reader:
                if id != row[0][:row[0].find(";")]:
                    new_file.writelines(row)
                    new_file.write("\n")

    os.rename("notes.csv", "0.csv")
    os.rename("tmp.csv", "notes.csv")
    os.rename("0.csv", "tmp.csv")

    print(f"Заметка с {id} удалена")
    input("\nНажмите Enter\n")