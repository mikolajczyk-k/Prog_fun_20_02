
def zadanie3(list):
    print("_____ZADANIE3_____")

    def filterEvenNumbers(list):
        evenList = []
        for x in list:
            if x%2 == 0:
                evenList.append(x)

        return evenList
    return print(filterEvenNumbers(list))
    