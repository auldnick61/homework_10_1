def filter_by_state(entries, state='EXECUTED'):
    """
    Фильтрует список словарей по заданному состоянию (state).
    Параметры:
        entries (list): Список словарей для фильтрации.
        state (str): Состояние, по которому следует произвести фильтрацию.
                     Значение по умолчанию - 'EXECUTED'.
    Возвращает:
        list: Новый список, содержащий только те словари, у которых ключ state
              содержит указанное значение.
    """

    filtered_entries = [entry for entry in entries if entry.get('state') == state]
    return filtered_entries


entries = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_by_default = filter_by_state(entries)
filtered_by_canceled = filter_by_state(entries, 'CANCELED')


if __name__ == "__main__":
    print('Выход функции со статусом по умолчанию EXECUTED:')
    print(filtered_by_default)
    print('Выход функции, если вторым аргументом передано CANCELED:')
    print(filtered_by_canceled)
