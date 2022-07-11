

def isFibo (valueToCheck, previousValue, currentValue):
    if valueToCheck == currentValue or valueToCheck == previousValue:
        return 1

    elif currentValue > valueToCheck:
        return 0

    else:
        return isFibo(valueToCheck,  currentValue, currentValue + previousValue)





valueToCheck = int(input(">"))

out_ = isFibo(valueToCheck, 0, 1)
print(1 if out_ else 0)