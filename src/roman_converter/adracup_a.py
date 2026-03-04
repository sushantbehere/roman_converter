def to_roman(arabic: int) -> str:
    """
    Roman Numerals that are valid: I, V, X, L, C, D, M including lowercase of them
    Can only have certain order (I-III, then IV, Cannot have VV, IIII)
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    Range for roman numerals is 1 - 3999 so I - MMMCMXCIX respectively
    """
    result = ""
    Map_roman = [
        (1000,"M"), (900,"CM"), (500, "D"), (100, "C"), (90,"XC"), (50,"L"), (10, "X"), (9, "IX"), (5,"V"), (1,"I")
    ]
    for number, string in Map_roman:
        if arabic >= number:
            return string + to_roman(arabic - number)

    return result

def from_roman(roman: str) -> int:
    # Map_integer = dict([
    #     ("I", 1), ("V", 5), ("X",10),("L",50),("C",100),("D",500),("M",1000)
    # ])
    Map_integer: dict[str, int] = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    result = 0
    for i in range(len(roman)):
        current = Map_integer[roman[i]]

        if i + 1 < len(roman) and current < Map_integer[roman[i+1]]:
            result -= current
        else:
            result += current

    return result