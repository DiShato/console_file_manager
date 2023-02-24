from use_functions import choice_1, choice_2

def test_shoping_choice_1():
    assert choice_1(0, 0) == 0
    assert choice_1(0, 10) == 10
    assert choice_1(10, 100) == 110

def test_shoping_choice_2():
    assert choice_2(0, 0) == 0
    assert choice_2(100,10) == 90
    assert choice_2(90, 20) == 70