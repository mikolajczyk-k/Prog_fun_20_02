from itertools import product

def zadanie1():
    print("_____ZADANIE1_____")
    firstList = ['A', 'B']
    secondList = ['C', 'D']

    productOfLists = product(firstList, secondList)
    return print(list(productOfLists))