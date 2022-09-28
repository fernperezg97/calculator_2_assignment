"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    my_string = input("type in your expression.")
    sliced = my_string.split(" ")
    first_num = int(sliced[1])
    second_num = int(sliced[2])
    if sliced[0] == "q":
        break
    elif sliced[0] == "pow":
        answer = power(first_num, second_num)
        print(answer)
    elif sliced[0] == "add":
        answer = add(first_num, second_num)
        print(answer)
    elif sliced[0] == "sub":
        answer = subtract(first_num, second_num)
        print(answer)
    elif sliced[0] == "mult":
        answer = multiply(first_num, second_num)
        print(answer)
    elif sliced[0] == "divide":
        answer = divide(first_num, second_num)
        print(answer)
    elif sliced[0] == "square":
        answer = square(first_num)
        print(answer)
    elif sliced[0] == "cube":
        answer = cube(first_num)
        print(answer)
    elif sliced[0] == "mod":
        answer = mod(first_num, second_num)
        print(answer)