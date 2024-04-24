from collections import defaultdict

def combineValues(v1, v2):
    if isinstance(v1, int) and isinstance(v2, int):
        return v1+v2
    elif isinstance(v1, str) and isinstance(v2, str):
        return v1+v2
    elif isinstance(v1, list) and isinstance(v2, list):
        return v1+v2
    
    else:
        raise ValueError("Mismatched or missing values")


def zadanie7(*dicts):
    print("_____ZADANIE7_____")

    combined = defaultdict(lambda: None)

    for dictionary in dicts:
        for key, value in dictionary.items():
            if combined[key] is None:
                combined[key] = value
            else:
                combined[key] = combineValues(combined[key], value)

    return print(dict(combined))



