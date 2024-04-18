def splitList(lst, *lengths):
    

    subs = []
    start = 0
    for length in lengths:
        end = start + length
        subs.append(lst[start:end])
        start = end
    return subs

    

def zadanie13(lst, *lengths):
    print("_____ZADANIE13_____")

    return print(splitList(lst, *lengths))