from types import ModuleType
import pytest


@pytest.mark.parametrize(
    "arabic, roman",
    [
        (1, "I"),
        (3, "III"),
        (4, "IV"),        # catches “no subtractive”
        (9, "IX"),        # catches “no subtractive”
        (14, "XIV"),
        (40, "XL"),       # catches “no subtractive”
        (90, "XC"),       # catches “no subtractive”
        (400, "CD"),      # catches “no subtractive”
        (900, "CM"),      # catches “no subtractive”
        (1994, "MCMXCIV"),
        (2024, "MMXXIV"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_to_roman_selected_cases(impl: ModuleType, arabic: int, roman: str):
    assert impl.to_roman(arabic) == roman
