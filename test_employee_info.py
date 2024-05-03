import employee_info

def test_average_salary():
    result = []
    test = (60166.666666666664)

    result = employee_info.calculate_average_salary()
    assert (result == test)
test_average_salary()

def test_get_employees_by_age_range():
    result = []
    test = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}]
    input = 24
    next_input = 30

    result = employee_info.get_employees_by_age_range(input,next_input)
    assert (result == test)


def test_employees_by_dept():
    result = []
    test = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    input = "Sales"

    result = employee_info.get_employees_by_dept(input)
    assert (result == test)