def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, возвращающая список словарей с заданным статусом"""
    return [dict_from_list for dict_from_list in list_of_dict if dict_from_list.get("state") == state]


def sort_by_date(list_of_dict: list[dict], type_sort: bool = True) -> list[dict]:
    """Функция, возвращающая список словарей отсортированных по дате"""
    for one_dict in list_of_dict:
        if int(one_dict.get("date", "")[5:7]) > 12 or int(one_dict.get("date", "")[8:10]) > 31:
            raise ValueError("Неправильный ввод значений даты")
    return sorted(list_of_dict, key=lambda list_date: list_date.get("date", "")[:10], reverse=type_sort)


if __name__ == "__main__":
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )

    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-31T01:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
