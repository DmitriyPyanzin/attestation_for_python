from datetime import datetime
import csv, os

def create_note(FILENAME):
    flag = True
    with open(FILENAME, encoding="utf_8") as file:
        list_id = []
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            list_id.append(row[0])
        while flag:
            id = input("Введите номер ID для новой заметки: ")
            for i in range(len(list_id)):
                if id in list_id:
                    print("Такой ID уже сущесвует, введите другой")
                    break
                else:
                    flag = False
                    break

    with open("tmp.csv", mode="w", encoding="utf_8") as new_file:
        with open(FILENAME, encoding="utf_8") as source:
            source_reader = csv.reader(source)
            count = 1
            now = datetime.now().strftime("%d-%m-%Y")
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note = {"ID": id, "Заголовок": title, "Тело": body, "Дата создания": now}
            for row in source_reader:
                if int(id) > int(row[0][:row[0].find(";")]):
                    new_file.writelines(row)
                    new_file.write("\n")
                elif count != 0 and int(id) < int(row[0][:row[0].find(";")]):
                    count = 0
                    parametrs = ["ID", "Заголовок", "Тело", "Дата создания"]
                    file_writer = csv.DictWriter(new_file, delimiter=";", lineterminator="\n", fieldnames=parametrs)
                    file_writer.writerow(note)
                    new_file.writelines(row)
                    new_file.write("\n")
                else:
                    new_file.writelines(row)
                    new_file.write("\n")
            if count == 1:
                parametrs = ["ID", "Заголовок", "Тело", "Дата создания"]
                file_writer = csv.DictWriter(new_file, delimiter=";", lineterminator="\n", fieldnames=parametrs)
                file_writer.writerow(note)


    os.rename("notes.csv", "0.csv")
    os.rename("tmp.csv", "notes.csv")
    os.rename("0.csv", "tmp.csv")

    print(f"Заметка {id} создана {now}.")
    input("\nНажмите Enter\n")