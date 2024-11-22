filter_param = {'state' : 'EXECUTED'}
def filter_by_state(proced_list: list[dict[str, any]], state: str = 'EXECUTED') -> any:
    """Функция принимает на вход список словарей с операциями и возвращает список с нужными параметрами"""
    return [t for t in proced_list if t.get("state") == state]

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

def sort_by_date(proced_list: list[dict[str, any]], reverse_list: bool = True) -> list[dict[str, any]]:
    for operation in proced_list:
        for key, value in operation.items():
            sorted_list = sorted(proced_list, key=lambda x: x['date'])
    return sorted_list

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
