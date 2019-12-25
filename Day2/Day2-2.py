def get_position(indicator, array):
    return int(array[indicator])


def get_value(indicator, array):
    return array[get_position(indicator, array)]


def add(operator1, operator2):
    # print("adding " + str(operator1 + " to " + str(operator2)))
    return int(operator1) + int(operator2)


def multiply(operator1, operator2):
    # print("multiplying " + str(operator1 + " by " + str(operator2)))
    return int(operator1) * int(operator2)


def run_iteration(input_string):
    commands_array = str.split(input_string, ",")
    position = 0
    while position < len(commands_array) - 3:
        calculated_figure = 0
        if commands_array[position] == "99":
            break
        elif commands_array[position] == "1":
            calculated_figure = add(get_value(int(position) + 1, commands_array),
                                    get_value(int(position) + 2, commands_array))
            commands_array[get_position(int(position) + 3, commands_array)] = str(calculated_figure)
        elif commands_array[position] == "2":
            calculated_figure = multiply(get_value(int(position) + 1, commands_array),
                                         get_value(int(position) + 2, commands_array))
            commands_array[get_position(position + 3, commands_array)] = str(calculated_figure)
        position = position + 4
    return commands_array


def run_program():
    original_string = '3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0'
    for noun in range(0, 100):
        for verb in range(0, 100):
            # if run_iteration('0,' + str(noun) + ',' + str(verb) + ',' + original_string)[0] == "19690720":
            output = run_iteration('0,' + str(noun) + ',' + str(verb) + ',' + original_string)[0]
            if output == 19690720 or output == "19690720":
                print(noun)
                print(verb)


run_program()
