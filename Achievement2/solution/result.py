import os

#функция нахождения n-го вхождения в строку
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#Рабочая директория
path = "/Users/sg/Desktop/bigdata2/txt/"

#Получаем массив нужных файлов
file_list = os.listdir(path)
file_list = [x for x in file_list if x[0:4] == "user"]
file_list = sorted(file_list)

#массив для сохранения результатов по каждому файлу
datadata=[]

#находим самое популярное значение скорости в каждом результате по h и user
for file in file_list:

    hvalue = file[find_nth(file, ".", 1) + 1:find_nth(file, ".", 2)]
    user = file[find_nth(file, ".", 2) + 1:find_nth(file, "f", 1)]
    reduce = open(path + file, 'r')
    string = str(reduce.read())
    reduce = string[4:].split()
    if len(reduce) % 2 != 0:
        reduce.pop(len(reduce)-1)

    maxcount = 0
    i = 1
    while i < len(reduce) - 1:
        if maxcount < int(reduce[i]):
            maxcount = int(reduce[i])
            maxword = int(reduce[i-1])
        i = i + 2

    data = []
    data.append(hvalue)
    data.append(maxword * maxcount)
    datadata.append(data)

#считаем среднее значение для каждого h
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

#сортируем в порядке убывания и выводим результаты
globalresult.sort(key = lambda x: x[1], reverse = True)

for i in range(len(globalresult)):
    print(globalresult[i][0], globalresult[i][1])



