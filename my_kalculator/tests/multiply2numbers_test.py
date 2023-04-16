import kalc.calc as my_calc


def test_prd_int():
    my_calc.multiply2numbers(2, 3)


def test_prd_float():
    my_calc.multiply2numbers(10.0, 0.5)


def test_prd_neg():
    my_calc.multiply2numbers(-3, -8)