from z1 import zadanie1
from z2 import zadanie2
from z3 import zadanie3
from z4 import zadanie4
from z5 import zadanie5
from z6 import zadanie6
from z7 import zadanie7
from z8 import zadanie8
from z9 import zadanie9
from z10 import zadanie10

if __name__ == "__main__":
    numList= [3, 5, 6, 8, 2, -15, 16, 32]
    word = "BahamaS"

    dateDict = {
        "year": 1968,
        "month": "January",
        "day": 17
    }

    carDict = {
        "brand": "Ford",
        "year": 2002,
        "color": "blue"
    }

    repList = [True, False, True, 2, 2, 2, 0.5 , 0.5, True]

    tpList = [(2,2,2), (1,1,1), (0.5,0.5,5)]

    zadanie1(numList)
    zadanie2(word)
    zadanie3(dateDict)
    zadanie4(2,4)
    zadanie5(numList, 3)
    zadanie6(numList, abs)
    zadanie7(dateDict, carDict)
    zadanie8(repList)
    zadanie9(tpList, pow)
    zadanie10(numList)

