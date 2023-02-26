from datetime import datetime
import random

dictionary_of_writers = {'А.С. Пушкин': '06.06.1799',
                         'М.Ю. Лермонтов': '15.10.1814',
                         'А.П. Чехов': '15.06.1904',
                         'Л.Н. Толстой': '09.09.1828',
                         'М.А. Булгаков': '15.05.1940',
                         'Н.В, Гоголь': '20.03.1852',
                         'А.А. Блок': '23.11.1880',
                         'И.С. Тургенев': '09.11.1818',
                         'И.А. Бунин': '22.10.1870',
                         'В.П. Некрасов': '17.06.1911'}


def play_victory(count_random_question=5, new_game='yes', dict_of_victory=dictionary_of_writers):
    '''

    :param count_random_question:  кол-во вопросов для викторины
    :param new_game: параметр запуска игры
    :param dict_of_victory: список вопросов и ответов для викторины
    :return:
    '''

    right_answer = 0
    wrong_answer = 0

    while new_game == 'yes':

        dict_of_victory_new = {}
        answer = None

        # отбираем (count_random_question несколько случайных писателей из словаря c помощью sample
        random_question = random.sample(list(dict_of_victory.keys()), count_random_question)

        # записываем в новый словарь отобранное кол-во пар вопрос-ответ
        for i in range(count_random_question):
            dict_of_victory_new[random_question[i]] = dict_of_victory.get(random_question[i])

        # проходим по вопросам словаря и проводим викторину
        for i in range(len(list(dict_of_victory_new.keys()))):

            dict_question = list(dict_of_victory_new.keys())[i]  # вопрос i
            the_answer_to_the_question = list(dict_of_victory_new.values())[i]  # ответ на вопрос i

            while answer != str(the_answer_to_the_question):

                answer = input('введите год рождения в формате dd.mm.yyyy {}: '.format(dict_question))
                try:
                    print(datetime.strptime(answer, '%d.%m.%Y'))  # проверка корректности записи даты
                except:
                    print('Введите дату в соответствии с форматом dd.mm.yyyy')
                else:
                    if answer == the_answer_to_the_question:
                        right_answer += 1
                    else:
                        wrong_answer += 1
                        print('правильный ответ :', the_answer_to_the_question)

        # результаты викторины
        print('количество правильных ответов : ', right_answer)
        print('количество ошибок : ', wrong_answer)
        print('процент правильных ответов : ', right_answer * 100 / (right_answer + wrong_answer))
        print('процент неправильных ответов : ', wrong_answer * 100 / (right_answer + wrong_answer))

        new_game = input('начать игру сначала? ввести yes/no : ')
