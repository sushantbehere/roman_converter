def to_roman(arabic: int) -> str:
    roman_map: list[tuple[int,str]] = [ # pair numerals to letters
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
        (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    conversion: str = ""
    for num, roman in roman_map:
        if arabic >= num:
            return roman + to_roman(arabic - num) #recursive
    return conversion

def from_roman(roman: str) -> int:
    arabic_map: list[tuple[str, int]] = [ # pair letters to numerals
        ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),
        ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
        ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
    ]
    return 0
