def zadanie9(lst, func):
    print("_____ZADANIE9_____")

    result = []
    for item in lst:
        if isinstance(item, tuple):
            for i in item:
                result.append(func(i,2))
    return print(result)