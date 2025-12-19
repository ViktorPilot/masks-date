def filter_by_state(list_of_dict: list[dict[str, str | int]], state: str) -> list[dict[str, str | int]]:
    """Функция, возвращающая список словарей с заданным статусом"""
    return [dict_from_list for dict_from_list in list_of_dict if dict_from_list.get("state") == state]


#def sort_by_date(list_of_dict_):






if __name__ == "__main__":
    list_of_dict_ = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    # filter_by_state(list_of_dict_, state="EXECUTED")
    # sort_by_date(list_of_dict_, type_sort="")



#[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]