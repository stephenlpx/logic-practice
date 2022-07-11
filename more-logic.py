import re

num = "121 21212"
#removes the spaces in a string!!!!
new_num = re.sub(" ", "", num)
print(new_num)
print("")
print("")


def add_odd(number):
    #not sure about the last digit situation
    sum = 0
    for index in range(0, len(number), 2):
        sum += int(number[index])
    return sum



def multiply_evens(number):
    new_str = ""
    for index in range(1, len(num), 2):
        new_str += new_num[index]
        int_value = int(new_str) * 2
    return int_value



def add_multiplication_value(new_value):
    sum = 0
    new_value = str(multiply_evens(new_num))
    for index in range(len(new_value)):
        sum += int(new_value[index])
    return sum




print(add_odd(new_num))
print(multiply_evens(new_num))
print(add_multiplication_value(multiply_evens(new_num)))
