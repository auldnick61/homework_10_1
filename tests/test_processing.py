import pytest
from typing import List, Dict
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_entries() -> List[Dict[str, str]]:
    return [
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_default(sample_entries: List[Dict[str, str]]) -> None:
    expected = [
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(sample_entries) == expected


def test_filter_by_state_canceled(sample_entries: List[Dict[str, str]]) -> None:
    expected = [
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(sample_entries, "CANCELED") == expected


def test_sort_by_date_descending(sample_entries: List[Dict[str, str]]) -> None:
    expected = [
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(sample_entries) == expected


def test_sort_by_date_ascending(sample_entries: List[Dict[str, str]]) -> None:
    expected = [
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(sample_entries, "ascending") == expected