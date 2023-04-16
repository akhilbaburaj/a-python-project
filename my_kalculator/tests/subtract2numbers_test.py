import kalc.calc as my_calc


def test_sub_int():
    my_calc.subtract2numbers(12, 3)


def test_sub_float():
    my_calc.subtract2numbers(9.5, 6.5)


def test_sub_neg():
    my_calc.subtract2numbers(-3, -8)