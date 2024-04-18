def cumulativeSum(lst):
    cumulative = []
    total = 0 

    for item in lst:
        total+=item
        cumulative.append(total)

    return cumulative




def zadanie10(lst):
    print("_____ZADANIE10_____")

    return print(cumulativeSum(lst))