import unittest
from masks import mask_card_number, mask_account_number


class TestMaskCardNumber(unittest.TestCase):
    def test_mask_card_number_valid(self):
        """Тестирование с валидным номером карты"""
        self.assertEqual(mask_card_number(1234567890123456), '1234 56** **** 3456')

    def test_mask_card_number_invalid(self):
        """Тестирование с невалидным номером карты"""
        self.assertEqual(mask_card_number(12345), 'Неверный формат номера карты')


class TestMaskAccountNumber(unittest.TestCase):
    def test_mask_account_number_valid(self):
        """Тестирование с валидным номером счета"""
        self.assertEqual(mask_account_number('12345678901234567890'), '****67890')

    def test_mask_account_number_invalid(self):
        """Тестирование с невалидным номером счета"""
        self.assertEqual(mask_account_number('12345'), 'Неверный формат номера счета')


if __name__ == '__main__':
    unittest.main()