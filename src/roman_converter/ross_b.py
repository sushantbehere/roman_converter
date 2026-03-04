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
    arabic_map:dict[str,int] = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    conversion:int = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and arabic_map[roman[i]] < arabic_map[roman[i + 1]]:
            conversion -= arabic_map[roman[i]]
        else:
            conversion += arabic_map[roman[i]]
    return conversion