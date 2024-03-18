def add(x):
    def inn(y):
        return x + y
    return inn


def zadanie15(x, y):
    print("_____ZADANIE15______")

    firstNumber = add(x)

    return print(firstNumber(y))