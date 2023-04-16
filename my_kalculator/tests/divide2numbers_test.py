import kalc.calc as my_calc


def test_div_int():
    my_calc.divide2numbers(2, 3)


def test_div_float():
    my_calc.divide2numbers(10.0, 0.5)


def test_div_neg():
    my_calc.divide2numbers(-3, -8)