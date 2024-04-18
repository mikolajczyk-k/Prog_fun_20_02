def sumOfSquaresOfOdds(numList):
    result = 0
    for n in numList:
        if n%2 ==1:
            result += n**2
    return result


def zadanie20(numList):
    print("_____ZADANIE20_____")

    return print (sumOfSquaresOfOdds(numList))