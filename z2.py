from statistics import mean

def filterLongWords(wordList):
    avgLength = mean([len(i) for i in wordList])

    longWords = [i for i in wordList if len(i) > avgLength]

    return longWords

def zadanie2(wordList):
    print("_____ZADANIE2_____")
    return print(filterLongWords(wordList))


