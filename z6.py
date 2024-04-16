def mapNested(lst, func):
    for i, item in enumerate(lst):
        if isinstance(item, list):
            mapNested(item, func)
        else:
            lst[i] = func(item)

def zadanie6(lst):
    print("_____ZADANIE6_____")

    def squareNum(x):
        return x**2
    
    mapNested(lst, squareNum)
    

    return print(lst)
