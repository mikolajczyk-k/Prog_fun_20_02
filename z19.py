def zadanie19(tup):
    print("_____ZADANIE19_____")
    print("Znajdywanie powtarzajacych sie wartosci w tuplach za pomoca dictionary (zwaracane sa elementy i ich indeksy)")

    def findRepetitionsInTuple(tup):
        repeatedElements = {}
        for i, item in enumerate(tup):
            if item in repeatedElements:
                repeatedElements[item].append(i)
            else:
                repeatedElements[item] = [i]

        results = []

        for item, indexes in repeatedElements.items():
            if len(indexes) > 1:
                results.append((item, indexes))
        return results
    
    return print(findRepetitionsInTuple(tup))

        
