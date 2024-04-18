def checkAnagrams(*words):
    charList = list(words[0].lower())
    charList.sort()
    result = True
    for i in words:
        wordChars = list(i.lower())
        wordChars.sort()
        if wordChars != charList:
            result = False
            return result
        
        else: 
            continue

    return result



def zadanie19(*words):
    print("_____ZADANIE19_____")

    return print(checkAnagrams(*words))