num_to_word_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

num_to_word_teens_dict = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

def get_num_of_digits(n):
    if n == 0:
        return 1
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def number_to_words(n):
    # ---- HANDLE INVALID INPUTS ----
    if n is None or not isinstance(n, int) or n < 0 or n > 9999:
        return None
    
    # ---- HANDLE VALID INPUTS ----
    out = ""
    while n > 10:
        num_of_digits = get_num_of_digits(n)
        print(num_of_digits)
        if num_of_digits == 2 and n < 20:
            out += num_to_word_teens_dict[n]
            return out
        if num_of_digits == 2 and n in num_to_word_dict.keys():
            out += num_to_word_dict[n]
            return out
        n //= 10
    if n <= 10:
        out += num_to_word_dict[n]
    
    return out

print(number_to_words(13))