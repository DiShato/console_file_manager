from use_functions import choice_1, choice_2

def test_shoping_choice_1():
    assert choice_1(0, 0) == 0
    assert choice_1(0, 10) == 10
    assert choice_1(10, 100) == 110

def test_shoping_choice_2():
    assert list(choice_2(0, {}, 0, name_shop='')) == [0, {'': 0}]
    assert list(choice_2(100,{}, 10, name_shop='пряники') ) == [90, {'пряники': 10}]
    assert list(choice_2(90, {'пряники': 10}, 20, name_shop='зефирки')) == [70, {'пряники': 10, 'зефирки': 20}]