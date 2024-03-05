import functools

def zadanie8(lista):
    print("_____ZADANIE8_____")
    return print(str(functools.reduce(lambda a, b: a+b, lista)))