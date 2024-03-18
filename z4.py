import timeit

def startTiming():
    return timeit.default_timer()

def zadanie4():
    print("_____ZADANIE4_____")
    start = startTiming()

    return print("The elapsed time is: ", str(timeit.default_timer()-start))