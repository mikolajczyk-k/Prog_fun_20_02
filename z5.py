

def zadanie5(lista, boka, bokb):
    even = []
    for x in lista:
        if x%2 ==0:
            even.append(x)
    
    print("_____ZADANIE 5 _____")
    print("Tablica: "+str(lista))
    print("Wynik: ")

    print(str(list(even)))

    print("Boki prostokatow: a = "+str(boka)+"b = "+str(bokb))

    x = lambda a, b : a*b

    print("Powierzchnia: ")
    print(x(boka, bokb))

    

