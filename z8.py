def partitionList(lst):
    even = []
    odd = []
    def checkIfEven(x):
        if x%2 == 0:
            return True
        else: 
            return False

    for item in lst:
        if checkIfEven(item) == True:
            even.append(item)
        else:
            odd.append(item)
    
    result = [even,odd]

    return result




def zadanie8(lst):
    print("_____ZADANIE8_____")
    print("Dzielenie listy intow na parzyste i nieparzyste:")


    try:
        return print(partitionList(lst))

    except Exception as e:
        print("Error: "+str(e))
        return None