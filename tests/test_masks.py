import pytest
from src.masks import mask_card_number, mask_account_number


@pytest.mark.parametrize("input_value,expected", [
    (1234567890123456, '1234 56** **** 3456'),  # Валидный номер карты
    (12345, 'Неверный формат номера карты'),  # Невалидный номер карты
])
def test_mask_card_number(input_value: int, expected: str) -> None:
    assert mask_card_number(input_value) == expected


@pytest.mark.parametrize("input_value,expected", [
    ('12345678901234567890', '****67890'),  # Валидный номер счета
    ('12345', 'Неверный формат номера счета'),  # Невалидный номер счета
])
def test_mask_account_number(input_value: str, expected: str) -> None:
    assert mask_account_number(input_value) == expected
