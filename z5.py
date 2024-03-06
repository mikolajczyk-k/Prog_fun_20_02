
def squareList(list):
    print("_____ZADANIE5_____")
    sqrList = []
    for x in list:
        s = lambda x: x**2
        sqrList.append(s(x))

    return print(str(sqrList))