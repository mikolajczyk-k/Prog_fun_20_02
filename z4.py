import timeit


def timeIt(startTime):

    print("_____ZADANIE4_____")

    def calculateTime(startTime):
        return startTime - timeit.timeit()
    
    return print("Time elapsed: "+str(calculateTime(startTime)))