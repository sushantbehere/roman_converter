from roman_converter.adendulu1 import ROMAN_MAP

def to_roman(arabic: int) -> str:
    if arabic <= 0 or arabic >= 4000:
        raise ValueError
    result = ""
    for value, symbol in ROMAN_MAP:
        while arabic >= value:
            result += symbol
            arabic -= value
    return result


def from_roman(roman: str) -> int:
    if not roman:
        return 0

    roman = roman.upper()

    values = dict(ROMAN_MAP)
    total = 0
    i = 0

    while i < len(roman):
        if i + 1 < len(roman) and values.get(roman[i], 0) < values.get(roman[i+1], 0):
            total += values[roman[i+1]] - values[roman[i]]
            i += 2
        else:
            total += values.get(roman[i], 0)
            i += 1

    return total