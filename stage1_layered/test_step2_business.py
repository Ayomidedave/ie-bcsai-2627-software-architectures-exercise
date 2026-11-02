# STEP 2: the business layer holds the rules of the shop.
# These tests call business.py directly: no requests, no status codes.
# Fails at the start. Passes when the functions in business.py are done.

from pathlib import Path

import pytest

import business
import persistence
from business import InvalidData, NotEnoughStock, NotFound


@pytest.fixture(autouse=True)
def empty_storage():
    persistence.reset()


@pytest.mark.parametrize("subtotal, shipping", [(1000, 499), (4999, 499), (5000, 0), (8000, 0)])
def test_shipping_rule(subtotal, shipping):
    assert business.calculate_shipping(subtotal) == shipping


def test_add_book_saves_it():
    book = business.add_book("Dune", 1500, 10)

    assert business.list_books() == [book]


def test_add_book_with_invalid_price_raises_invalid_data():
    with pytest.raises(InvalidData):
        business.add_book("Dune", 0, 10)


def test_place_order_computes_the_price_and_takes_stock():
    book = business.add_book("Dune", 1500, 10)

    order = business.place_order(book["id"], 2)

    assert order["total_cents"] == 3499
    assert persistence.find_book(book["id"])["stock"] == 8


def test_place_order_for_unknown_book_raises_not_found():
    with pytest.raises(NotFound):
        business.place_order(99, 1)


def test_place_order_without_enough_stock_raises_not_enough_stock():
    book = business.add_book("Dune", 1500, 1)

    with pytest.raises(NotEnoughStock):
        business.place_order(book["id"], 5)


def test_get_order():
    book = business.add_book("Dune", 1500, 10)
    order = business.place_order(book["id"], 1)

    assert business.get_order(order["id"]) == order


def test_business_does_not_import_presentation():
    code = (Path(__file__).parent / "business.py").read_text()
    imports = [line for line in code.splitlines() if line.startswith(("import ", "from "))]

    assert not any("presentation" in line for line in imports)
