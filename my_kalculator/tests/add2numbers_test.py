import kalc.calc as my_calc


def test_add_int():
    my_calc.add2numbers(2, 3)


def test_add_float():
    my_calc.add2numbers(2.5, 6.5)


def test_add_neg():
    my_calc.add2numbers(-3, -8)