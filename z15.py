def customSort(wordList, func):

    return sorted(wordList, key=func)


def zadanie15(wordList):
    print("_____ZADANIE15_____")
    
    return print(customSort(wordList, func=lambda s: s[::-1])) # sortuje wlg odwroconych stringow alfabetycznie
