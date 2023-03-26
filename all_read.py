import csv

def read_notes(FILENAME):
    with open(FILENAME, encoding='utf_8') as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
    input("\nНажмите Enter\n")