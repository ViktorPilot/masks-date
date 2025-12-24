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
                                         [7000792289606361, "7000792289606362"]
                                         ])
def test_get_mask_card_not_int(card_number):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(card_number)

@pytest. mark.parametrize("count_number, result", [("12345678901234504305", "**4305"),
                                                   ("00000000000000000000", "**0000"),
                                                   ("99999999999999999999", "**9999"),
                                                   ])
def test_get_mask_account_positive(count_number, result):
    assert masks.get_mask_account(count_number) == result

@pytest.mark.parametrize("count_number", ["736541084",
                                          "7365410843013587430500000001"])
def test_get_mask_account_short_and_large(count_number):
    with pytest.raises(ValueError):
        masks.get_mask_account(count_number)

@pytest.mark.parametrize("count_number", ["abcdabcdabcdabcdabcd",
                                         "9999999.999999999999",
                                         "",
                                         [99999999999999999999, "abcdabcdabcdabcdabc"]
                                         ])
def test_get_mask_account_not_int(count_number):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(count_number)
