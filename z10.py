def zadanie10(limit):
    print("_____ZADANIE10_____")

    if limit <=0 or not isinstance(limit, int):
        return print("The number must be positive and of type int.")

    def evenNumbersGenerator(limit):
        a=2
        for _ in range(limit):
            yield a
            a+=2
    return print(list(evenNumbersGenerator(limit)))