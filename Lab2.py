print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    variable = input("Enter some numbers separated by commas (e.g 5,67,32): ")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def get_user_input():
    lists = input("Enter floats separated by commas: ")
    float_list = lists.split(",")
    Nout = []
    for num in float_list:
       Nout.append(float(num))
    return Nout

def calc_average(input):
    temps = input
    temp_list = [float(temp) for temp in temps]
    return sum(temp_list) / len(temp_list)

def sort_temperature():
    temps = input("Enter temps separated by commas: ")
    temp_list = [float(temp) for temp in temps.split(",")]
    return sorted(temp_list)

def calc_median_temperature(input):
    temps = input
    temp_list = [float(temp) for temp in temps]
    sorted_temps = sorted(temp_list)
    total = len(sorted_temps)
    if total % 2 == 0:
        return (sorted_temps[total // 2 - 1] + sorted_temps[total // 2]) / 2
    else:
        return sorted_temps[total // 2]

def calc_min_max_temperature(input):
    temps = input
    temp_list = [int(temp) for temp in temps]
    return min(temp_list), max(temp_list)

if __name__ == "__main__":
    main()
