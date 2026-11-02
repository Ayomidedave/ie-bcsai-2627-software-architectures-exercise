# STEP 1: the catalog domain, with its own three layers.
#     catalog/presentation.py -> catalog/business.py -> catalog/persistence.py
# Fails at the start. Passes when the three files in catalog/ are done.

import pytest

from catalog import business, persistence, presentation
from errors import NotEnoughStock, NotFound
from layer_rules import check_layers


@pytest.fixture(autouse=True)
def empty_catalog():
    persistence.reset()


def test_catalog_respects_its_layers():
    check_layers("catalog")


def test_persistence_saves_and_finds_books():
    book = persistence.save_book("Dune", 1500, 10)

    assert persistence.find_book(book["id"]) == book
    assert persistence.find_book(99) is None


def test_business_gives_the_price():
    book = business.add_book("Dune", 1500, 10)

    assert business.get_price(book["id"]) == 1500


def test_business_takes_stock():
    book = business.add_book("Dune", 1500, 10)

    business.take_stock(book["id"], 3)

    assert persistence.find_book(book["id"])["stock"] == 7


def test_business_refuses_to_take_more_stock_than_there_is():
    book = business.add_book("Dune", 1500, 2)

    with pytest.raises(NotEnoughStock):
        business.take_stock(book["id"], 5)


def test_business_raises_not_found_for_unknown_books():
    with pytest.raises(NotFound):
        business.get_price(99)


def test_presentation_answers_with_status_codes():
    assert presentation.add_book({"title": "Dune", "price_cents": 1500, "stock": 10})[0] == 201
    assert presentation.add_book({"title": "", "price_cents": 1500, "stock": 10})[0] == 400
    assert presentation.list_books()[0] == 200
