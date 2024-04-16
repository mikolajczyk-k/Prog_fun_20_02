def recursiveSum(numList):
    result = 0
    for item in numList:
        if isinstance(item, list):
            result += recursiveSum(item)
        else:
            result += item

    return result

def zadanie3(numList):
    print("_____ZADANIE3_____")

    return print(recursiveSum(numList))