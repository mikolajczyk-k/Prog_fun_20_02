def zadanie5(lst, maxLen):
    print("_____ZADANIE5_____")

    result = []
    start = 0

    while start < len(lst):
        result.append(lst[slice(start, start+maxLen)])
        start+=maxLen

    return print(result)

