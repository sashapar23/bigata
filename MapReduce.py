import csv
import os

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def iter_group(queue):
    buf = []
    prev_key = None

    for val in queue:
        cur_key, cur_val = val
        #print cur_key, cur_val
        if cur_key == prev_key or prev_key is None:
            buf.append(cur_val)
        else:
            yield prev_key, buf
            buf = []
            buf.append(cur_val)
        prev_key = cur_key

    if buf:
        yield cur_key, buf

class MapReduce:
    def __init__(self):
        self.queue = []

    def send(self, a,b):
        self.queue.append((a,b))

    def count(self):
        return len(self.queue)

    def __iter__(self):
        return iter_group(sorted(self.queue))

#Корневая рабочая директория
path = "/Users/sg/Desktop/MapReduce" + "/"

#Получаем отсортированный список всех txt в директории
file_list = os.listdir(path)
file_list = [x for x in file_list if x[len(x)-3:len(x)] == "csv"]
file_list = sorted(file_list)

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
                string += row + " "
        except:
            print(count)
    x = MapReduce()
    for word in string.split():
        x.send(word, 1)

    maxcount = 0
    for word, ones in x:
        if maxcount < sum(ones):
            maxcount = sum(ones)
            maxword = word
    print(hvalue, user, maxword, maxcount)
    data = []
    data.append(hvalue)
    data.append(int(maxword) * maxcount)
    datadata.append(data)

i = 0
j = 1
summ = 0
globalresult = []
hresult = []
while i < len(datadata) - 1:
    if datadata[i][0] == datadata[i+1][0]:
        summ += datadata[i][1]
        i += 1
        j += 1
        if i == len(datadata) - 2:
            summ += datadata[i+1][1]
            j += 1
            hresult.append(datadata[i][0])
            hresult.append(summ / j)
            globalresult.append(hresult)
    else:
        hresult.append(datadata[i][0])
        hresult.append(summ / j)
        globalresult.append(hresult)
        summ = 0
        j = 1
        i += 1
        hresult = []

globalresult.sort(key = lambda x: x[1], reverse = True)

for i in range(len(globalresult)):
    print(globalresult[i][0], globalresult[i][1])









