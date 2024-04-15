from itertools import groupby


def zadanie7(numList):
    print("_____ZADANIE7_____")

    sortedNumbers = sorted(numList, key=lambda x: x%2)
    groupedNumbers = groupby(sortedNumbers, key=lambda x: x%2)

    for key, group in groupedNumbers:
        keyAndGroup = {key: list(group)}
        print(keyAndGroup)


