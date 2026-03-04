

_ROMAN_PAIRS: list[tuple[int, str]] = [
    (1000, "M"),
    (500, "D"),
    (100, "C"),
    (50, "L"),
    (10, "X"),
    (5, "V"),
    (1, "I"),
]

_ROMAN_VALUES: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(arabic: int) -> str:
    # BUG: no 4/9/40/90/400/900 subtractive pairs
    result: list[str] = []
    n = arabic
    for value, numeral in _ROMAN_PAIRS:
        while n >= value:
            result.append(numeral)
            n -= value
    return "".join(result)


def from_roman(roman: str) -> int:
    # BUG: always additive
    return sum(_ROMAN_VALUES[ch] for ch in roman)
