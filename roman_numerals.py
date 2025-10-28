def to_roman(num):
    #create dictionary for roman numerals
    romans = {
        "M" : 1000,
        "CM" : 900,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "XL" : 40,
        "X" : 10,
        "IX": 9,
        "V" : 5,
        "IV": 4,
        "I" : 1
    }
    result = []
    while num > 0:
        for key, val in romans.items():
            if val <= num:
                num -= val
                result.append(key)
                break
    return ''.join(result)


# print(to_roman(5254))

