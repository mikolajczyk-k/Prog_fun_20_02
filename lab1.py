import timeit

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
from z11 import zadanie11
from z12 import zadanie12
from z13 import zadanie13
from z14 import zadanie14
from z15 import zadanie15
from z16 import zadanie16
from z17 import zadanie17
from z18 import zadanie18
from z19 import zadanie19
from z20 import zadanie20
if __name__ == "__main__":

    wordList = ["USA", "Anglia", "Paryż", "Barcelona", "Azja", "Malezja"]
    numList = [1, 3, -3, 4, 6, 16, -20, 80]
    letterTuple = ("a", "a", "c", "z", "c", "d", "c")
    plantDictionary = {
        "flower": "Dandelion",
        "tree": "Maple",
        "root": "Ginger"
    }

    zadanie1(3)
    zadanie2(5)
    zadanie3(numList)
    zadanie4()
    zadanie5(numList)

    numList = zadanie6(numList) # przekształcenie listy w liste kwadratow
    numList = [4, 6, 16, -20, 80] #przeksztalcenie do wartosci poczatkowych, aby ulatwic sprawdzanie wiarygodnosci wynikow

    zadanie7(wordList)
    zadanie8(numList)
    zadanie9()
    zadanie10(10)
    zadanie11(wordList)
    zadanie12(10)
    zadanie13(-6)
    zadanie14(8, -2)
    zadanie15(3, 2)
    zadanie16(2)
    zadanie17(100.24)
    zadanie18(3)
    zadanie19(letterTuple)
    zadanie20(plantDictionary)








