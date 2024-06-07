from datetime import datetime


entries = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(entries, state='EXECUTED'):
    """
    Фильтрует список словарей по заданному состоянию (state).
    """

    filtered_entries = [entry for entry in entries if entry.get('state') == state]
    return filtered_entries


# entries = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]

filtered_by_default = filter_by_state(entries)
filtered_by_canceled = filter_by_state(entries, 'CANCELED')


def sort_by_date(entries, order='descending'):
    """
    Сортирует список словарей по дате (ключ 'date').
    """

    for entry in entries:
        entry['date'] = datetime.strptime(entry['date'], '%Y-%m-%dT%H:%M:%S.%f')

    # Сортировка списка
    sorted_entries = sorted(entries, key=lambda x: x['date'], reverse=order == 'descending')

    # Преобразование объекта datetime обратно в строку
    for entry in sorted_entries:
        entry['date'] = entry['date'].strftime('%Y-%m-%dT%H:%M:%S.%f')

    return sorted_entries


entries = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

sorted_entries_desc = sort_by_date(entries)
sorted_entries_asc = sort_by_date(entries, 'ascending')

if __name__ == "__main__":
    print('Выход функции со статусом по умолчанию EXECUTED:')
    print(filtered_by_default)
    print('Выход функции, если вторым аргументом передано CANCELED:')
    print(filtered_by_canceled)
    print('Сортировка по убыванию:')
    print(sorted_entries_desc)
    print('Сортировка по возрастанию:')
    print(sorted_entries_asc)
