
_ROMAN_PAIRS: list[tuple[int, str]] = [
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

_ROMAN_VALUES: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(arabic: int) -> str:

    result: list[str] = []
    n = arabic
    for value, numeral in _ROMAN_PAIRS:
        while n >= value:
            result.append(numeral)
            n -= value
    return "".join(result)


def from_roman(roman: str) -> int:
    total = 0
    for i, ch in enumerate(roman):
        v = _ROMAN_VALUES[ch]
        if i + 1 < len(roman) and v < _ROMAN_VALUES[roman[i + 1]]:
            total -= v
        else:
            total += v
    return total
