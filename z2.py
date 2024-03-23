from itertools import combinations

def zadanie2():
    print("_____ZADANIE2_____")

    listObj = ['A', 'B', 'C', 1, 2, 3, True, False]

    def possiblePairs(listObj):
        combinationsList = list(combinations(listObj,2))
        return combinationsList
    
    return print(possiblePairs(listObj))