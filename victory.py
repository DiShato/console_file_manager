from datetime import datetime
import random

def  play_victory():
    count_random_writers = 5
    right_answer = 0
    wrong_answer = 0
    new_game = 'yes'

    dictionary_of_writers = {'А.С. Пушкин': '06.06.1799',
                             'М.Ю. Лермонтов': '15.10.1814',
                             'А.П. Чехов': '15.06.1904',
                             'Л.Н. Толстой': '09.09.1828',
                             'М.А. Булгаков': '15.05.1940',
                             'Н.В, Гоголь' : '20.03.1852',
                             'А.А. Блок' : '23.11.1880',
                             'И.С. Тургенев' : '09.11.1818',
                             'И.А. Бунин' : '22.10.1870',
                             'В.П. Некрасов' : '17.06.1911'
                             }



    while new_game == 'yes':

        dictionary_of_writers_new = {}



        # отбираем (count_random_writers) несколько случайных писателей из словаря
        random_writers = random.sample(list(dictionary_of_writers.keys()), count_random_writers)

        for i in range(count_random_writers):
            dictionary_of_writers_new[random_writers[i]] = dictionary_of_writers.get(random_writers[i])



        year_ = None



        # проходим по случайному списку писателей и проводим викторину
        for i in range(len(list(dictionary_of_writers_new.keys()))):

            name_writers = list(dictionary_of_writers_new.keys())[i]
            birthday_writers = list(dictionary_of_writers_new.values())[i]

            while year_ != str(birthday_writers):

                year_ = input('введите год рождения в формате dd.mm.yyyy {}: '.format(name_writers))

                if year_ == str(birthday_writers):
                    right_answer += 1

                    #if year_ == list(dictionary_of_writers_new.values())[-1]:
                     #   break
                else:
                    wrong_answer += 1
                    dt = datetime.strptime(birthday_writers, '%m.%d.%Y')
                    print('правильный ответ :', dt.strftime('%B %d, %Y'))



        # результаты викторины
        print('количество правильных ответов : ', right_answer)
        print('количество ошибок : ', wrong_answer)
        print('процент правильных ответов : ', right_answer * 100 / (right_answer + wrong_answer))
        print('процент неправильных ответов : ', wrong_answer * 100 / (right_answer + wrong_answer))

        new_game = input('начать игру сначала? ввести yes/no : ')
