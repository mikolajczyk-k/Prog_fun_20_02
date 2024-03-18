def zadanie20(data):
    print("_____ZADANIE20_____")
    print("Wykrywa i zwraca czy dane wejsciowe to krotka, lista, czy dictionary i wypisuje dane")

    def recognizeDataType(data):
        match str(type(data)):
            case "<class 'list'>":
                print("A list was given. Data: ")
                print(list(data))

            case "<class 'tuple'>":
                print("A tuple was given. Data: ")
                print(tuple(data))

            case "<class 'dict'>":
                print("A tuple was given. Data: ")
                print(dict(data))
            case default:
                print("Unsupported data type. ")

    recognizeDataType(data)
