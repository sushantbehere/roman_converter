from importlib import import_module
from pathlib import Path
from types import ModuleType

import pytest

IMPL_DIR = Path(__file__).parent.parent.parent / "src/roman_converter"

def discover_implementations() -> list[ModuleType]:
    return [
        import_module(f"roman_converter.{path.stem}")
        for path in sorted(IMPL_DIR.glob("*.py"))
        if path.is_file() and not path.name.startswith("_")
    ]

@pytest.fixture(params=discover_implementations(), ids=lambda m: m.__name__)
def impl(request: pytest.FixtureRequest) -> ModuleType:
    return request.param
