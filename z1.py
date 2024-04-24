def zadanie1(numList):
    print("_____ZADANIE1_____")

    if all(isinstance(x, int ) for x in numList):
        try:
            result = 0
            for item in numList:
                if item%2 == 0:
                    result+=item
            return print(result)

        except Exception as e:
            print(f"Error: {e}")
    else:
        return print("All values must be of type int")


    
