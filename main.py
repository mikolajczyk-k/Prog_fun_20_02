from z1 import *
from z2 import zadanie2
from z3 import zadanie3
from z4 import zadanie4
from z5 import zadanie5
from z6 import zadanie6
from z7 import *
from z8 import zadanie8
from z9 import zadanie9
from z10 import zadanie10

if __name__ == "__main__":
    zadanie1()
    zadanie2()
    zadanie3()

    array = [10, 3, 4, 2, 8, 13]

    def doKwadratu(x):
        return x**2
    
    zadanie4(doKwadratu, array)
    lista = [3, 4, 6, 9, 10, 33, 56]
    zadanie5(lista, 5, 6)

    slowa = ["ananas", "cytryna", "Michal", "Adam", "Troja", "Atlantyda"]
    zadanie6(slowa, array)

    def dodajPiec(x):
        return x+5
    zadanie7(doKwadratu, dodajPiec, lista)

    listaFun =[doKwadratu, dodajPiec]
    zadanie72(listaFun, lista)

    listaod1do10 = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]

    zadanie8(listaod1do10, slowa)

    zadanie9(lista)

    file_path = 'loremipsum.txt'

    zadanie10(100, file_path)


