# Take input string and turn into array
# Take array and turn into array of arrays of 5 values
# iterate each one of those outer arrays and perform the calculation specified
# output the correct value
# Make this a class so its easier to test!

def get_position(indicator, array):
    return int(array[indicator])


def get_value(indicator, array):
    return array[get_position(indicator, array)]


def add(operator1, operator2):
    print("adding " + str(operator1 + " to " + str(operator2)))
    return int(operator1) + int(operator2)


def multiply(operator1, operator2):
    print("multiplying " + str(operator1 + " by " + str(operator2)))
    return int(operator1) * int(operator2)


def run_program(input_string):
    commands_array = str.split(input_string, ",")
    position = 0
    print("starting")
    while position < len(commands_array) - 3:
        calculated_figure = 0
        print(position)
        print(commands_array)
        if commands_array[position] == "99":
            print("found exit command")
            break
        elif commands_array[position] == "1":
            calculated_figure = add(get_value(int(position) + 1, commands_array),
                                    get_value(int(position) + 2, commands_array))
            print("putting " + str(calculated_figure) + " into position " + str(commands_array[int(position) + 3]))
            commands_array[get_position(int(position) + 3, commands_array)] = str(calculated_figure)
        elif commands_array[position] == "2":
            calculated_figure = multiply(get_value(int(position) + 1, commands_array),
                                         get_value(int(position) + 2, commands_array))
            print("putting " + str(calculated_figure) + " into position " + str(commands_array[int(position) + 3]))
            commands_array[get_position(position + 3, commands_array)] = str(calculated_figure)
        print("going round")
        position = position + 4

    print("done")
    return commands_array


def test1():
    print(run_program('1,0,0,0,99'))
    print('test 1 should say')
    print('[2,0,0,0,99]')


def test2():
    print(run_program('2,3,0,3,99'))
    print('test 2 should say')
    print('[2,3,0,6,99]')


def test3():
    print(run_program('2,4,4,5,99,0'))
    print('test 3 should say')
    print('[2,4,4,5,99,9801]')


def test4():
    print(run_program('1,1,1,4,99,5,6,0,99'))
    print('test 4should say')
    print('[30,1,1,4,2,5,6,0,99]')


def task():
    commands_array = run_program(
        '1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0')
    print("position 0 contains: " + commands_array[0])


# test1()
# test2()
# test3()
# test4()
task()
