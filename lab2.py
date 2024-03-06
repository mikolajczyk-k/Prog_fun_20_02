import timeit

from z1 import apply_Twice
from z2 import *
from z3 import filterEvenNumbers
from z4 import timeIt
from z5 import squareList
from z6 import zadanie6
from z7 import zadanie7
from z8 import zadanie8
if __name__ == "__main__":

    def powTwo(x):
        return x**2
    
    x= 5
    apply_Twice(powTwo, x)

    make_Multiplier(x)

    lista = [3, 5, 7, 6, 13, 15, 16, 230, 80]

    filterEvenNumbers(lista)

    now = timeit.timeit()

    timeIt(now)

    squareList(lista)

    zadanie6(lista)

    listaSlow = ["USA", "Anglia", "Paryż", "Barcelona", "Azja", "Malezja"]

    zadanie7(listaSlow)

    test = [1, 2, 3, 4, 5]

    zadanie8(test)

