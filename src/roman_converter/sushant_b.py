
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
    def build(n: int, idx: int = 0) -> str:
        if n == 0:
            return ""
        value, numeral = _ROMAN_PAIRS[idx]
        if n >= value:
            return numeral + build(n - value, idx)
        return build(n, idx + 1)

    return build(arabic)


def from_roman(roman: str) -> int:
    total = 0
    i = 0
    while i < len(roman):
        v = _ROMAN_VALUES[roman[i]]
        if i + 1 < len(roman):
            v2 = _ROMAN_VALUES[roman[i + 1]]
            if v < v2:
                total += (v2 - v)
                i += 2
                continue
        total += v
        i += 1
    return total
