
def zadanie2(x):
    print("_____ZADANIE2_____")
    print("Multiplier: 4")

    def multiplyBy4(x):
        return x*4

    def make_Multiplier(x):
        return multiplyBy4(x)
    
    return print(make_Multiplier(x))