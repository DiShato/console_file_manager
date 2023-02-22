import os
import shutil
import sys
from victory import *
from use_functions import *

while True:
    print()
    print('1. создать папку')
    print('2. удалить папку')
    print('3. копировать файл')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход')
    print()

    choice = input('Выберите пункт меню')

    if choice == '1':
        os.mkdir(input('введите наименование папки'))

    if choice == '2':
        os.rmdir(input('введите наименование папки'))

    if choice == '3':
        filename_ = input('введите наименование файла для копирования')
        filename_new = input('введите новое наименование файла для копирования')
        shutil.copy(filename_,filename_new)

    if choice == '4':
        print("Каталог:", os.listdir())

    if choice == '5':
        print("Каталог:", [x for x in os.listdir() if x[-3:] != '.py'])

    if choice == '6':
        print("Файлы .py:", [x for x in os.listdir() if x[-3:] == '.py'])

    if choice == '7':
        print(' OS is', sys.platform, '(', os.name, ')')

    if choice == '8':
        print('человек')

    if choice == '9':
        play_victory()

    if choice == '10':
        shoping()

    if choice == '11':
        break
