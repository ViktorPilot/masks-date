import pytest

from src import processing


@pytest.fixture
def filter_by_state_positive():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_by_state_positive_executed(filter_by_state_positive):
    assert processing.filter_by_state(filter_by_state_positive) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]


def test_filter_by_state_positive_canceled(filter_by_state_positive):
    assert processing.filter_by_state(filter_by_state_positive, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]


@pytest.fixture
def filter_by_state_not_executed():
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_filter_by_state_not_executed(filter_by_state_not_executed):
    assert processing.filter_by_state(filter_by_state_not_executed) == []


@pytest.fixture
def filter_by_state_not_canceled():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_filter_by_state_not_canceled(filter_by_state_not_canceled):
    assert processing.filter_by_state(filter_by_state_not_canceled, state="CANCELED") == []


@pytest.mark.parametrize("list_of_dict, result",
                         [([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                            {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}],
                           [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}])])
def test_filter_by_state_not_state_executed(list_of_dict, result):
    assert processing.filter_by_state(list_of_dict) == result


@pytest.mark.parametrize("list_of_dict, result",
                         [([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                            {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}],
                           [{"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}])])
def test_filter_by_state_not_state_canceled(list_of_dict, result):
    assert processing.filter_by_state(list_of_dict, state="CANCELED") == result


@pytest.fixture
def sort_by_date_positive():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_positive_reduce(sort_by_date_positive):
    assert processing.sort_by_date(sort_by_date_positive) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_positive_increase(sort_by_date_positive):
    assert processing.sort_by_date(sort_by_date_positive, type_sort=False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def sort_by_date_equal_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T01:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
    ]


def test_sort_by_date_equal_date_reduce(sort_by_date_equal_date):
    assert processing.sort_by_date(sort_by_date_equal_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T01:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
    ]


def test_sort_by_date_equal_date_increase(sort_by_date_equal_date):
    assert processing.sort_by_date(sort_by_date_equal_date, type_sort=False) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T01:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
    ]


@pytest.mark.parametrize("list_of_dict", [[{"id": 41428829, "state": "EXECUTED", "date": "2019-13-03T18:35:29.512364"},
                                           {"id": 939719570, "state": "EXECUTED",
                                            "date": "2018-06-31T02:08:58.425572"}],
                                          [{"id": 41428829, "state": "EXECUTED", "date": "2019-12-03T18:35:29.512364"},
                                           {"id": 939719570, "state": "EXECUTED",
                                            "date": "2018-06-32T02:08:58.425572"}]])
def test_sort_by_date_failed_date(list_of_dict):
    with pytest.raises(ValueError):
        processing.sort_by_date(list_of_dict)
