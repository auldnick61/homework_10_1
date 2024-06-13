import unittest
from src.processing import filter_by_state, sort_by_date


class TestProcessing(unittest.TestCase):

    def setUp(self) -> None:
        self.entries = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]

    def test_filter_by_state_default(self) -> None:
        """Тестирование фильтрации по состоянию 'EXECUTED'."""
        expected = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
        self.assertEqual(filter_by_state(self.entries), expected)

    def test_filter_by_state_canceled(self) -> None:
        """Тестирование фильтрации по состоянию 'CANCELED'."""
        expected = [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
        self.assertEqual(filter_by_state(self.entries, "CANCELED"), expected)

    def test_sort_by_date_descending(self) -> None:
        """Тестирование сортировки по дате по убыванию."""
        expected = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
        sorted_entries = sort_by_date(self.entries)
        self.assertEqual(sorted_entries, expected)

    def test_sort_by_date_ascending(self) -> None:
        """Тестирование сортировки по дате по возрастанию."""
        expected = [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
        sorted_entries = sort_by_date(self.entries, "ascending")
        self.assertEqual(sorted_entries, expected)


if __name__ == "__main__":
    unittest.main()
