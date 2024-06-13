import unittest
from src.widget import mask_account_info, format_date


class TestWidget(unittest.TestCase):
    def test_mask_account_info_account_valid(self) -> None:
        """Проверка маскировки валидного номера счета."""
        info = "Счет 73654108430135874302"
        expected = "Счет ****74302"
        self.assertEqual(mask_account_info(info), expected)

    def test_mask_account_info_card_valid(self) -> None:
        """Проверка маскировки валидного номера карты."""
        info = "Visa Platinum 8990922113665229"
        expected = "Visa Platinum 8990 92** **** 5229"
        self.assertEqual(mask_account_info(info), expected)

    def test_mask_account_info_invalid(self) -> None:
        """Проверка возвращения ошибки при неверном формате номера."""
        info = "Wrong Info 123456"
        expected = "Неверный формат номера карты"
        self.assertEqual(mask_account_info(info), expected)

    def test_format_date_valid(self) -> None:
        """Проверка корректного приведения строки с датой к формату ДД.ММ.ГГГГ."""
        date_string = "2018-07-11T02:26:18.671407"
        expected = "11.07.2018"
        self.assertEqual(format_date(date_string), expected)


if __name__ == "__main__":
    unittest.main()
