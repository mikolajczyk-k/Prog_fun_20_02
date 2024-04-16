def removeduplicates(lst):
    unique = set()
    result =[]
    for item in lst:
        if item not in unique:
            unique.add(item)
            result.append(item)
    return result



def zadanie4(lst):
    print("_____ZADANIE4_____")

    return print(removeduplicates(lst))