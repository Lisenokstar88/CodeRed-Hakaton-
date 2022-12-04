import Pandas as pd
import xlrd
import os
from openpyxl import load_workbook
from win32com import client
excel_data = pd.read_excel()
workbook = load_workbook ('D:\Рабочий стол\Новая папка\Заявка (Ответы).xlsx')
book = xlrd.open_workbook('черновик квитанции')
tablica = xlrd.open_workbook('Заявка (Ответы)')
polychatel = book.find('Введите имя получателя')
otpravitel = book.find('Введите имя')
chislo = book.find('Введите дату')
number = book.find('Введите номер')
summ = book.find('Введите сумму ₽')
cells = sheet['K2: K5000']
cell = sheet ['K']
for i in cells:
    if cell[i] == ('Оплата в банке'):
        book.replace('Введите имя получателя', (tablica.sheet['B', i], tablica.sheet['C', i], tablica.sheet['D', i]))
        book.save('квитанция 1')
# if polychatel == 'Введите имя получателя':
