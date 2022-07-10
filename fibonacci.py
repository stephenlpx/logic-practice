

def isFibo (valueToCheck, previousValue, currentValue):
    if currentValue > valueToCheck:
        return 0
    elif valueToCheck == currentValue:
        return 1
    else:
        return isFibo(valueToCheck,  currentValue, currentValue + previousValue)





valueToCheck = int(input(">"))

out_ = isFibo(valueToCheck, 0, 1)
print(1 if out_ else 0)