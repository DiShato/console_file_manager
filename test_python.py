#  тесты для встроенных функций filter, map, sorted
#  также для функций из библиотеки math: pi, sqrt, pow, hypot


# filter
def test_filter_none_list():
    assert list(filter(None, [-1, 0, 1, 1.111])) == [-1, 1, 1.111]
    assert list(filter(None, ['b'])) == ['b']
    assert list(filter(None, [None])) == []
    assert list(filter(None, [True])) == [True]
    assert list(filter(None, [False])) == []

    bools = ['bool', 0, None, True, False, 1, 1 - 1, 2 % 2]
    out = []
    for i in bools:
        if bool(i) == True:
            out.append(i)
    assert list(filter(None, bools)) ==  out

# map
def test_map():
    assert list(map(len, ['1','22','333'])) == [1, 2, 3]
    assert list(map(str, [1, 2, 3, ])) == ['1', '2', '3', ]
    assert list(map(abs, [-2, 6, -4.3, 0, 2*4,-7//5])) == [2, 6, 4.3, 0, 8, 2]
    assert list(map(lambda num: num ** 2, [2, 4])) == [4, 16]
    assert list(map(lambda x: x[:2], ['22-02-2023', '21-02-2023' ])) == ['22','21']

# map
def test_sorted():
    assert sorted(['1', '22', '333']) == ['1', '22', '333']
    assert sorted(['1', '22', '333'], reverse=False) == ['1', '22', '333']
    assert sorted([1, 2.2 ], reverse=False) == [1, 2.2]
    assert sorted([1, 22], reverse=True) == [22, 1]
    assert sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}) ==  [1, 2, 3, 4, 5]
    assert sorted("Hello Andrey !".split(), key=str.lower) == ['!', 'Andrey', 'Hello']


from math import pi, sqrt, pow, hypot
# pi
def test_pi():
    assert pi == 3.141592653589793
    assert pi/3.141592653589793 == 1

# sqrt
def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(1) == 1
    assert sqrt(0) == 0
    assert sqrt(25) == 5

# pow
def test_pow():
    assert pow(1,10) == 1
    assert pow(10, 2) == 100
    assert pow(5, 0) == 1
    assert pow(0, 10) == 0

# hypot
def test_hypot():
    assert hypot(4, 3)==  sqrt(4*4+3*3) == 5
    assert hypot(1, 1) == sqrt(1 * 1 + 1 * 1)
    assert hypot(2, 0) == sqrt(2 * 2 + 0 * 0) == 2

