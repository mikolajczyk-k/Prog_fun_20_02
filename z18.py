


def zadanie18(limit):
    print("_____ZADANIE18_____")
    print("Na przykładzie generatora kwadratow liczb: ")

    if limit <0 or not isinstance(limit, int):
        return print("The number must not be neative and of type int.")

    def generateSquares():
        i=1
        while 1:
            yield i**2
            i+=1

    squareGenerator = generateSquares()
    squareList = []
    for _ in range(limit):
        squareList.append(next(squareGenerator))

    return print(squareList)