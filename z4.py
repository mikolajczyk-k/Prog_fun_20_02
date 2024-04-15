
def zadanie4(numList):
    print("_____ZADANIE4_____")

    squaresGreaterThanTen = [num **2 for num in numList if (numSquared := num**2 and num > 10)]

    return print(squaresGreaterThanTen)