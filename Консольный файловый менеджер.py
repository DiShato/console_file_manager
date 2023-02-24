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
    print('11. сохранить содержимое рабочей директории в файл')
    print('12. выход')
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

        print("Каталог:", [x for x in os.listdir() if os.path.isdir(x)])

    if choice == '6':
        print("Файлы", [x for x in os.listdir() if os.path.isfile(x)])

    if choice == '7':
        print(' OS is', sys.platform, '(', os.name, ')')

    if choice == '8':
        print('человек')

    if choice == '9':
        play_victory()

    if choice == '10':
        shoping()

    if choice == '11':
        if 'listdir.txt' not in os.listdir():
            os.path.exists('listdir.txt')
        f = open('listdir.txt', 'w')
        f.write(' Каталог : ' + str([x for x in os.listdir() if os.path.isdir(x)]))
        f.write(' Файлы : ' + str([x for x in os.listdir() if os.path.isfile(x)]))
        f.close()

    if choice == '12':
        break
