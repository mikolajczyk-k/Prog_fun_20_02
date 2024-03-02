def zadanie10(n, file_path):
    print("_____ZADANIE10_____")    
    print("Ciag fibonacciego: ")
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a+b
    
    print(str(list(fib(n))))


    print("Plik tekstowy: ")
    def liniaPoLinii(filename):
        with open (filename ,'r') as file:
            for line in file:
                yield line.strip()

    for line in liniaPoLinii(file_path):
        print(line)
