import csv
import random
from xml.dom import minidom 

with open('books.csv', encoding='cp1251') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    books = list(reader)

#1
count = 0
for i in books:
    if len(i[1]) > 30:
        count += 1
print('Строк "Название" длиннее 30:', count)

#2
avtor = input('Введите автора: ')
countavt1 = 0
for i in books:
    price = float(i[7])
    if avtor == i[3] or avtor == i[4]:
        if price < 150:
            countavt1 += 1
if countavt1 == 0:
    print('Ничего не найдено')
else:
    print('Количество книг автора', avtor, 'с ценой меньше 150:', countavt1)

#3
nepustavtor = [i for i in books if i[3] != ' ' or i[4] != ' ']
randavtor = random.sample(nepustavtor, 20)
with open('avtors.txt', 'w', encoding='utf-8') as answer:
    for j, i in enumerate(randavtor, start = 1):
        year = i[6][6:10]
        answer.write(f'{j}. {i[3]}. {i[1]} - {year} год.\n')
print('Файл avtors.txt создан')

#4
xmpl = minidom.parse('currency.xml')
slovar = {}
for val in xmpl.getElementsByTagName('Valute'):
    name = val.getElementsByTagName('Name')[0].firstChild.data
    value = val.getElementsByTagName('Value')[0].firstChild.data
    slovar[name] = value
print(slovar)

#Доп1
tags = []
for i in books:
    for tag in i[12].split('#'):
        tag = tag.strip()
        if tag not in tags and tag != ' ':
            tags.append(tag)
for i in tags:
    print(i)

#Доп2
popular = {}
for i in books:
    name = i[1]
    popular[name] = popular.get(name, 0) + int(i[8])
revpopular = []
for name in popular:
    revpopular.append([popular[name], name])
revpopular.sort(reverse = True)
print('20 самых популярных книг:')
print()
for i in range(20):
    print(f' {i + 1}. {revpopular[i][1]} - кол-во: {revpopular[i][0]}шт.')