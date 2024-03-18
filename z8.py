import functools

def zadanie8(numList):
    print("_____ZADANIE8_____")
    return print(functools.reduce(lambda a,b: a+b, numList)) #albo operator.add