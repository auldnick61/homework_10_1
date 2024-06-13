### Функция filter_by_state
Описание: Эта функция принимает список словарей entries и строку state. Она фильтрует список, возвращая только те словари, чьё значение ключа "state" равно аргументу state. Аргумент state имеет значение по умолчанию "EXECUTED".

Примеры использования:
- filter_by_state(entries) вернёт список всех словарей со статусом "EXECUTED".
- filter_by_state(entries, "CANCELED") вернёт список всех словарей со статусом "CANCELED".

### Функция sort_by_date
Описание: Эта функция принимает список словарей entries и строку order. Она сортирует список словарей на основе даты, указанной в ключе "date". Дата должна быть в формате ISO 8601. Аргумент order может принимать значения "ascending" для сортировки по возрастанию или "descending" для сортировки по убыванию, которое является значением по умолчанию.

Примеры использования:
- sort_by_date(entries) вернёт список словарей, отсортированных по дате от новых к старым.
- sort_by_date(entries, "ascending") вернёт список словарей, отсортированных по дате от старых к новым.

### Пример работы с данной функцией
Предоставлен блок кода, который демонстрирует использование этих функций с предопределённым списком entries. В нём выполняется:
- Фильтрация элементов по умолчанию (state="EXECUTED").
- Фильтрация элементов по состоянию state="CANCELED".
- Сортировка элементов по дате в порядке убывания (order="descending").
- Сортировка элементов по дате в порядке возрастания (order="ascending").

Выходные данные демонстрируют результаты этих операций.


## Добавлены тесты проверки модулей: masks.py, widget.py, processing.py
Предоставлены блоки тестов: test_masks.py, test_widget.py, test_processing.py
- Проведено тестирование функций
- Проведен тест на покрытие кода тестами
- Проведена проверка кода тестов mypy, flake8, black