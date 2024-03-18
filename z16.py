def zadanie16(x):
    print("_____ZADANIE16______")

    def powTwo(x):
        return x**2
    def multiplyBy4(x):
        return x*4
    
    def compose(*funcs):
        def inner(arg):
            for f in reversed(funcs):
                arg = f(arg)
            return arg
        return inner

    composed = compose(powTwo, multiplyBy4) 
    return print(composed(x))