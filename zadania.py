from main import *

doZad4 = 5.3

def roundFun(number):
    return round(number)

def powNumber(number):
    return pow(number, 2)

def intNumber(number):
    return int(number)

def chrNumber(number):

    intNum = intNumber(number)

    return chr(intNum)

def predefFun(number):

    print("_____PREDEFINED_FUNCITONS_____")
    print("str(number): "+str(number))
    print("round(number) "+str(roundFun(number)))
    print("pow(number, 2)"+str(powNumber(number)))
    print("int(number): " + str(intNumber(number)))
    print("chr(number): " + str(chrNumber(number)))
    return 0

def zadanie3():
    print("_____FUNKCJA ZE ZMIENNA GLOBALNA I FUNKCYCYJNA___")
    y = 3
    print("zmienna globalna x: "+str(x))

    print("zmienna funkcyjna y: "+str(y))

    return print("x+y="+str(x+y))

def zadanie4(x):
    print("_____FUNKCJA JAKO ARGUMENT___")
    return (x)

def zadanie5(lista):
    parzyste = []
    print("___PARZYSTE Z LISTY___")
    for num in lista:
        if num%2 == 0:
            parzyste.append(num)
    print(str(parzyste))

def zadanie5_2(b):
    return lambda a: a * b

















