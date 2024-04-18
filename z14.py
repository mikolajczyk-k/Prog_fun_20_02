def countUniqueElements(lst):
    unique = set()
    result = 0
    for i in lst:
        if i not in unique:
            unique.add(i)
            result +=1

    return result
    

def zadanie14(lst):
    print("_____ZADANIE14_____")

    return print(countUniqueElements(lst))