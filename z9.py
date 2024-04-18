
def zipWithIndex(lst):
    indexList= []

    for i in range(len(lst)):
        indexList.append(i)
    
    return list(zip(indexList, lst))

def zadanie9(lst):
    print("_____ZADANIE9_____")

    return print(zipWithIndex(lst))