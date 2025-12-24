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
