import pytest

from src import masks


@pytest.mark.parametrize("card_number, result", [("7000792289606361", "7000 79** **** 6361"),
                                                 ("9999999999999999", "9999 99** **** 9999"),
                                                 ("0000000000000000", "0000 00** **** 0000")])
def test_get_mask_card_positive(card_number, result):
    assert masks.get_mask_card_number(card_number) == result


@pytest.fixture
def short_number():
    return "700079228"


def test_get_mask_card_short_number(short_number):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(short_number)


@pytest.fixture
def large_number():
    return "7000792280000000001"


def test_get_mask_card_large_number(large_number):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(large_number)

@pytest.mark.parametrize("card_number", ["abcdabcdabcdabcd",
                                         "9999999.99999999",
                                         "",
                                         [9999999999999999, "abcdabcdabcdabcd"]
                                         ])
def test_get_mask_card_not_int(card_number):
    with pytest.raises(Exception):
        masks.get_mask_card_number(card_number)

