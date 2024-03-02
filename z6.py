def zadanie6(slowa, liczby):

    print("_____ZADANIE 6______")
    slowaNaA = filter(lambda slowo: slowo[0].lower() == 'a', slowa)

    print("Slowa na A/a: "+str(list(slowaNaA)))

    kwadratyLiczb = map(lambda liczba: liczba**2, liczby)

    print("Kwadraty liczb: "+str(list(kwadratyLiczb)))
