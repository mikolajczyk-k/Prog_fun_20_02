def zadanie3(n):
    print("_____ZADANIE3_____")

    if n < 0 or not isinstance(n, int):
        return print("The number be positive and of type int.")

    def fibonacci():
        a, b, = 0, 1
        while True:
            yield a
            a, b = b, a + b
        
    gen = fibonacci()
    
    fibList = []

    for _ in range(n):
        fibList.append(next(gen))

    return print(fibList)