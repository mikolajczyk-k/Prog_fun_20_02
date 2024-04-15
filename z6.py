

def zadanie6(x, y):
    print("_____ZADANIE6_____")

    def safeFunction(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                return None
        return wrapper
    
    @safeFunction
    def divideNumbers(x, y):
        return x / y
    
    return print(divideNumbers(x,y))
