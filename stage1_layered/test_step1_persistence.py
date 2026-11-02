# STEP 1: the persistence layer stores and finds books and orders. Nothing else.
# Fails at the start. Passes when the functions in persistence.py are done.

import pytest

import persistence


@pytest.fixture(autouse=True)
def empty_storage():
    persistence.reset()


def test_save_and_find_a_book():
    book = persistence.save_book("Dune", 1500, 10)

    assert book == {"id": 1, "title": "Dune", "price_cents": 1500, "stock": 10}
    assert persistence.find_book(1) == book


def test_find_a_missing_book_returns_none():
    assert persistence.find_book(99) is None


def test_all_books():
    persistence.save_book("Dune", 1500, 10)
    persistence.save_book("Emma", 900, 3)

    assert [book["title"] for book in persistence.all_books()] == ["Dune", "Emma"]


def test_update_stock():
    book = persistence.save_book("Dune", 1500, 10)

    persistence.update_stock(book["id"], 4)

    assert persistence.find_book(book["id"])["stock"] == 4


def test_save_and_find_an_order():
    order = persistence.save_order({"book_id": 1, "quantity": 2})

    assert order["id"] == 1
    assert persistence.find_order(1) == order


def test_find_a_missing_order_returns_none():
    assert persistence.find_order(99) is None


def test_persistence_does_not_import_other_layers():
    from pathlib import Path

    code = (Path(__file__).parent / "persistence.py").read_text()
    imports = [line for line in code.splitlines() if line.startswith(("import ", "from "))]

    assert not any("business" in line or "presentation" in line for line in imports)
