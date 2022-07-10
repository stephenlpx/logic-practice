
ErrorMessage = ""


def calc(value1, value2, calcOperator):
    operators = ["Add", "Subtract", "Divide", "Multiply"]

    if calcOperator not in operators:
        ErrorMessage = f"{calcOperator} does not exist"
        return ErrorMessage

    try:
        v1 = float(value1)
        v2 = float(value2)
    except ValueError:
        return "Numbers need to be numeric"


    if v2 == 0 and calcOperator == "Divide":
        ErrorMessage = "Cant divide by zero"
        return ErrorMessage


    return_value = 0

    if calcOperator == "Add":
        return_value = v1 + v2
    elif calcOperator == "Subtract":
        return_value = v1 - v2
    elif calcOperator == "Divide":
        return_value = v1 / v2
    elif calcOperator == "Multiply":
        return_value = v1 * v2

    return return_value


value1 = input(">")
value2 = input(">")
calcOperator = input(">")

result = calc(value1, value2, calcOperator)

if ErrorMessage != "":
    print(ErrorMessage.upper())
else:
    print(str(result) + '\n')