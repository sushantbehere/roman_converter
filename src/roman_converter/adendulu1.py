ROMAN_MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

VALID_SUBTRACTIONS = {"IV", "IX", "XL", "XC", "CD", "CM"}


def to_roman(arabic: int) -> str:
    if not isinstance(arabic, int):
        raise ValueError("Non-integer")
    if arabic <= 0:
        raise ValueError("Must be positive")
    if arabic >= 4000:
        raise ValueError("Too large")

    result = ""
    for value, symbol in ROMAN_MAP:
        while arabic >= value:
            result += symbol
            arabic -= value
    return result


def from_roman(roman: str) -> int:
    if not roman:
        raise ValueError("Empty string")
    if roman != roman.upper():
        raise ValueError("Case violation")

    for c in roman:
        if c not in "IVXLCDM":
            raise ValueError("Invalid character")

    if "IIII" in roman or "XXXX" in roman or "CCCC" in roman or "MMMM" in roman:
        raise ValueError("Invalid repetition")
    if "VV" in roman or "LL" in roman or "DD" in roman:
        raise ValueError("Invalid repetition")

    total = 0
    i = 0
    values = {symbol: value for value, symbol in ROMAN_MAP}

    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in VALID_SUBTRACTIONS:
            total += values[roman[i:i+2]]
            i += 2
        else:
            if i + 1 < len(roman) and values[roman[i]] < values[roman[i+1]]:
                raise ValueError("Invalid subtraction")
            total += values[roman[i]]
            i += 1

    if total < 1 or total >= 4000:
        raise ValueError("Out of range")

    return total