from functools import partial

def zadanie17(x):
    print("_____ZADANIE17_____")

    add5 = partial(lambda x: x+5)
    return print(add5(x))
