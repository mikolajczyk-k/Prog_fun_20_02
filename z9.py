import functools

def zadanie9(lista):
    print("_____ZADANIE 9_____")
    print("Najwieksza liczba z listy: ")
    print(functools.reduce(lambda a, b: a if a > b else b, lista))
    print("Srednia liczb z listy: ")
    print(functools.reduce(lambda a, b: a+b, lista)/len(lista) if lista else 0)