def zadanie8(lista, listaSlow):
    print("_____ZADANIE 8_____")
    print("Lista kwadratow: ")

    listaKwadratow = [x**2 for x in lista]
    print(str(list(listaKwadratow)))

    print("Slowa: "+str(list(listaSlow)))
    listaDlugosci = [len(x) for x in listaSlow]
    print("Dlugosci slow: "+str(list(listaDlugosci)))
