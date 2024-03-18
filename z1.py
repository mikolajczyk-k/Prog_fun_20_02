def zadanie1(x):
     
    print("_____ZADANIE1_____")
    def powTwo(x):
        return x**2
     
    def apply_Twice(func, x):
        func = powTwo
        
        return func(func(x))
    

    return print(apply_Twice(powTwo, x))



