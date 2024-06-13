import pytest
from src.widget import mask_account_info, format_date
from typing import List, Tuple


@pytest.fixture
def account_info() -> List[Tuple[str, str]]:
    return [
        ("Счет 73654108430135874302", "Счет ****74302"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Wrong Info 123456", "Неверный формат номера карты")
    ]


@pytest.fixture
def date_info() -> List[Tuple[str, str]]:
    return [
        ("2018-07-11T02:26:18.671407", "11.07.2018")
    ]


@pytest.mark.parametrize("input_value,expected", [
    ("Счет 73654108430135874302", "Счет ****74302"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Wrong Info 123456", "Неверный формат номера карты")
])
def test_mask_account_info(input_value: str, expected: str) -> None:
    assert mask_account_info(input_value) == expected


@pytest.mark.parametrize("input_value, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018")
])
def test_format_date(input_value: str, expected: str) -> None:
    assert format_date(input_value) == expected
