def zadanie3(i):
    print("_____ZADANIE2_____")

    def fibonacci():
        a, b, = 0, 1
        while True:
            yield a
            a, b = b, a + b\
        
    gen = fibonacci()
    gen.next()

    for _ in range(i):
        print(gen.next())