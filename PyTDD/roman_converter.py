arab_roman_dict = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I",
}

roman_shorter_dict = {
    "IIII": "IV",
    "VIIII": "IX",
    "XXXX": "XL",
    "LXXXX": "XC",
    "CCCC": "CD",
    "DCCCC": "CM",
}

def roman_converter(num):
    # ----- HANLDE INVALID INPUTS -----
    if num == None:
        return None
    
    if not isinstance(num, int):
        return None
    
    if num < 1 or num >= 4000:
        return None
    
    # ----- HANDLE VALID INPUTS -----
    roman = ""
    for key in arab_roman_dict.keys():
        while num >= key:
            roman += arab_roman_dict[key]
            num -= key
    
    # ----- HANDLE ROMAN SHORTENING -----
    for c in range(0, len(roman) - 4):
        if roman[c:c+5] in roman_shorter_dict:
            roman = roman[:c] + roman_shorter_dict[roman[c:c+5]] + roman[c+5:]
    for c in range(0, len(roman) - 3):
        if roman[c:c+4] in roman_shorter_dict:
            roman = roman[:c] + roman_shorter_dict[roman[c:c+4]] + roman[c+4:]

    return roman

def main():
    print(roman_converter(39))

if __name__ == "__main__":
    main()

