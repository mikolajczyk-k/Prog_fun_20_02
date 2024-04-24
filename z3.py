def zadanie3(dict):
    print("_____ZADANIE3_____")

    filteredDict = {key: value for key, value in dict.items() if isinstance(value, int) and value % 2 == 0}
    return print(filteredDict)