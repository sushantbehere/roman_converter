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
    arabic_map: dict[str, int] = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    i:int = 0
    conversion:int = 0

    while i < len(roman):
        if i + 1 < len(roman) and arabic_map[roman[i]] < arabic_map[roman[i + 1]]:
            conversion += arabic_map[roman[i + 1]] - arabic_map[roman[i]]
            i += 2
        else:
            conversion += arabic_map[roman[i]]
            i += 1

    return conversion
