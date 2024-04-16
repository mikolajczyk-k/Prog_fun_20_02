def flattenList(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flattenList(item))
        else: 
            flat.append(item)
    return flat

    
            


def zadanie7(lst):
    print("_____ZADANIE7_____")

    flattenList(lst)

    return print(flattenList(lst))