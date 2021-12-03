import csv
import os
import shutil

#Функция для нахождения n-го вхождения в строку
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#Корневая рабочая директория
path = "/Users/sg/Desktop/bigdata2/"

#Получаем отсортированный список всех csv в директории
file_list = os.listdir(path)
file_list = [x for x in file_list if x[len(x)-3:len(x)] == "csv"]
file_list = sorted(file_list)

#идем по каждому csv файлу и форматируем его
os.mkdir(path + "txt")
datadata = []
for file in file_list:
    hvalue = file[find_nth(file, ".", 1)+1:find_nth(file, ".", 2)]
    user = file[find_nth(file, ".", 2)+1:find_nth(file, ".", 3)]
    string = ""
    with open(path + file, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ";"
        file_reader = csv.reader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        try:
            for row in file_reader:
                if count == 0:
                    count += 1
                    continue
                count += 1
                row = row[2]
                row = row.split()
                row = ''.join(row)
                row = row[:row.find(".")-len(row)]
                row = row[:-3] + "000"
                string += row + " "
        except:
            print(count)

        #формируем выходной txt файл
        nametxt = file[:-4] + ".txt"
        txt = open(path + "txt" + "/" + nametxt, "w", encoding='utf-16-le')
        txt.write('\ufeff')
        txt.write(string)

#Раскладываем полученные txt по директориям
path = path + "txt/"
file_list = os.listdir(path)
os.mkdir(path + "format/")
for file in file_list:
    os.mkdir(path + "format/" + file[:-4])
    shutil.move(path + file, path + "format/" + file[:-4])

