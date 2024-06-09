from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(entries: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по заданному состоянию (state).
    """
    filtered_entries = [entry for entry in entries if entry.get("state") == state]

    return filtered_entries


def sort_by_date(entries: List[Dict[str, Any]], order: str = "descending") -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате (ключ 'date').
    """

    sorted_entries = sorted(
        entries, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=order == "descending"
    )

    return sorted_entries


if __name__ == "__main__":

    entries = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    filtered_by_default = filter_by_state(entries)
    filtered_by_canceled = filter_by_state(entries, "CANCELED")
    sorted_entries_desc = sort_by_date(entries)
    sorted_entries_asc = sort_by_date(entries, "ascending")

    print("Выход функции со статусом по умолчанию EXECUTED:")
    print(filtered_by_default)
    print("Выход функции, если вторым аргументом передано CANCELED:")
    print(filtered_by_canceled)
    print("Сортировка по убыванию:")
    print(sorted_entries_desc)
    print("Сортировка по возрастанию:")
    print(sorted_entries_asc)
