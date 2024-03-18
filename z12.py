from functools import partial


def zadanie12(x):

    print("_____ZADANIE12_____")
    def multiply (x, n):
        return x*n

    mult3 = partial(multiply,  n=3)

    return print(str(mult3(x)))
