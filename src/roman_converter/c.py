def to_roman(arabic: int) -> str:
    roman_map: list[tuple[int,str]] = \
        [(1000,"M"),(500,"D"),(100,"C"),(50,"L"),(10,"X"),(5,"V"),(1,"I")] # pair numerals to letters
    conversion: str = ""
    for num, roman in roman_map:
        count = arabic // num
        if count >= 1:
            conversion += roman * count # repeats roman count times
            arabic -= num * count
    return conversion

def from_roman(roman: str) -> int:
    arabic_map: list[tuple[str, int]] = [
        ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),
        ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
        ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
    ]
    return 0
