import csv
import os
from datetime import datetime

def redactor(FILENAME):
    with open(FILENAME, encoding="utf_8") as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            print(f"{row[0]}")
    id = input("\nВведите ID заметки, которую хотите редактировать: ")

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
                elif id == row[0][:row[0].find(";")]:
                    str = row[0][:row[0].find(";") + 1]
                    title = input("Введите новый заголовок заметки: ")
                    body = input("Введите новое тело заметки: ")
                    now = datetime.now().strftime("%d-%m-%Y")
                    str += title + ";" + body + ";" + now
                    new_file.writelines(str)
                    new_file.write("\n")

    os.rename("notes.csv", "0.csv")
    os.rename("tmp.csv", "notes.csv")
    os.rename("0.csv", "tmp.csv")

    print(f"Заметка {id} изменена")
    input("\nНажмите Enter\n")