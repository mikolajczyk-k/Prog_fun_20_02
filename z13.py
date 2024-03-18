
def calculateFactorial(x):
    if (x==1 or x==0):
        return 1
    elif x < 0:
        return x*calculateFactorial(x+1)
    else: 
        return x*calculateFactorial(x-1)
    

def zadanie13(x):
    print("_____ZADANIE13_____")
    return print(calculateFactorial(x))