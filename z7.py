def zadanie7(func1, func2, lista):
    print("_____ZADANIE 6_____")
    wynik_func1 = map(func1, lista)
    wynik_func2 = map(func2, lista)

    print("Pierwsza funkcja: "+str(list(wynik_func1)))
    print("Druga funkcja: "+str(list(wynik_func2)))

def zadanie72(functions, lista):
    print("LISTA FUNKCJI: ")
    i=1
    for f in functions:
        print("Funkcja "+str(i)+" :")
        print(list(map(f, lista)))
        i+=1
        

