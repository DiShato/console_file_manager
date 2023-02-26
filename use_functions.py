"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import json


def choice_1(cash, cash_deposit=0):
    '''
    :param cash_deposit: сумма пополнения
    :return: сумма с учетом пополнения
    '''
    try:
        cash = float(cash)
        cash_deposit = float(cash_deposit)
    except:
        print('Ошибка! Введено не число! Повторите попытку!')
    else:
        cash_new = cash + cash_deposit
        f = open('cash.txt', 'a')
        f.write(str(cash_deposit) + ',')
        f.close()
        return cash_new


def choice_2(cash, sum_shop=0, name_shop='покупка'):
    '''
    :param cash: сумма на счете
    :param sum_shop: сумма покупки
    :param name_shop: наименование покупки
    :return:
    '''
    try:
        cash = float(cash)
        sum_shop = float(sum_shop)
    except:
        print('Ошибка! Введено не число! Повторите попытку!')
    else:
        if cash >= sum_shop:
            cash -= sum_shop
        elif cash < sum_shop:
            print('денег не хватает!')

        f = open('history_shop.txt', 'a')
        f.write('покупка {} : {}руб, '.format(name_shop, sum_shop))
        f.close()

    return cash


def shoping():
    # если нет файлов с историейпокупок и остатка, то создаем
    if 'cash.txt' not in os.listdir():
        os.path.exists('cash.txt')
        f = open('cash.txt', 'w')
        f.write(str(0) + ',')
        f.close()
    if 'history_shop.json' not in os.listdir():
        os.path.exists('history_shop.json')

    while True:
        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход\n')

        choice = input('Выберите пункт меню')
        if choice == '1':
            cash = choice_1(cash=list(open('cash.txt', 'r'))[0].split(',')[-2],
                            cash_deposit=input('введите сумму пополнения'))

        elif choice == '2':
            cash = choice_2(cash=list(open('cash.txt', 'r'))[0].split(',')[-2],
                            sum_shop=input('Введите сумму покупки'),
                            name_shop=input('Введите наименование покупки'))

        elif choice == '3':
            print(list(open('history_shop.txt', 'r')))

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
