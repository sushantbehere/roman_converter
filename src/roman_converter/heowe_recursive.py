def to_roman(arabic: int) -> str:
    values = [
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
    if arabic <= 0:
        return ""
    for value, numeral in values:
        if arabic >= value:
            return numeral + to_roman(arabic - value)
    return ""


def from_roman(roman: str) -> int:
    values = [
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
    if not roman:
        return 0
    for arabic_val, roman_str in values:
        if roman.startswith(roman_str):
            return arabic_val + from_roman(roman[len(roman_str) :])
    return 0
