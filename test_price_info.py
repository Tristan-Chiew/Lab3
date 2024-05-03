import price_info

def test_total_cost_shopping():
    result = []
    test = (46.75)

    result = price_info.total_cost_shopping()

    assert (result == test)
test_total_cost_shopping()

def test_cost_of_fruit():
    result = []
    test = (12.0, 10.0, "apple")

    result = price_info.cost_of_fruits("apple",10)

    assert (result == test)
test_cost_of_fruit()