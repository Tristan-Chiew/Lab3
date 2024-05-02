import Lab2
print("test lab2")

def test_calc_min_max_temperature():
    result = []
    input = [64, 34, 25, 12, 22, 11, 90]
    test = (11,90)

    result = Lab2.calc_min_max_temperature(input)

    assert (result == test)

def test_calc_average():
    result = []
    input = [10, 2 ,3]
    test = (5.0)

    result = Lab2.calc_average(input)

    assert (result == test)

def test_calc_median_temperature():
    result = []
    input = [10, 2 ,3]
    test = (3.0)

    result = Lab2.calc_median_temperature(input)

    assert (result == test)

