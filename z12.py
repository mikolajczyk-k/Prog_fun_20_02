def rotateList(lst, steps=0):
    length = len(lst)
    steps = steps % length
    return lst[-steps:] + lst[:-steps]


def zadanie12(lst, steps=0):
    print("_____ZADANIE12_____")

    return print(rotateList(lst, steps))