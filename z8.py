from collections import Counter

def zadanie8(lst):
    print("_____ZADANIE8_____")

    counter = Counter(lst)

    maxCount = max(counter.values())
    for item in lst:
        if counter[item] == maxCount:
            return print(item)
        