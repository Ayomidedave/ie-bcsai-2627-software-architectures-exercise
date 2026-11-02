# SHOP BEHAVIOUR TESTS: they check WHAT the shop does, seen from the outside,
# not HOW the code is organised inside.
# This exact file is copied into every stage. It passes from the start and must
# keep passing after every change: if it goes red, the refactoring broke the shop.
#
# Rules of the shop:
#   - subtotal = price x quantity
#   - shipping is free from 5000 cents (50 euros), otherwise 499 cents
#   - placing an order takes the books out of stock
#   - an order is rejected if the book does not exist (404) or there is not enough stock (409)

import pytest

from app import create_app


@pytest.fixture
def shop():
    return create_app()


def add_dune(shop, price=1500, stock=10):
    status, book = shop.add_book({"title": "Dune", "price_cents": price, "stock": stock})
    assert status == 201
    return book


def stock_of(shop, book_id):
    status, books = shop.list_books()
    for book in books:
        if book["id"] == book_id:
            return book["stock"]


def test_add_and_list_books(shop):
    book = add_dune(shop)

    assert book == {"id": 1, "title": "Dune", "price_cents": 1500, "stock": 10}
    assert shop.list_books() == (200, [book])


@pytest.mark.parametrize(
    "request_data",
    [
        {"title": "", "price_cents": 1500, "stock": 1},
        {"title": "Dune", "price_cents": 0, "stock": 1},
        {"title": "Dune", "price_cents": 1500, "stock": -1},
    ],
)
def test_invalid_book_is_rejected(shop, request_data):
    status, body = shop.add_book(request_data)

    assert status == 400


def test_small_order_pays_shipping(shop):
    book = add_dune(shop, price=1500)

    status, order = shop.place_order({"book_id": book["id"], "quantity": 2})

    assert status == 201
    assert order["subtotal_cents"] == 3000
    assert order["shipping_cents"] == 499
    assert order["total_cents"] == 3499


def test_order_of_50_euros_has_free_shipping(shop):
    book = add_dune(shop, price=2500)

    status, order = shop.place_order({"book_id": book["id"], "quantity": 2})

    assert order["shipping_cents"] == 0
    assert order["total_cents"] == 5000


def test_order_takes_books_out_of_stock(shop):
    book = add_dune(shop, stock=10)

    shop.place_order({"book_id": book["id"], "quantity": 3})

    assert stock_of(shop, book["id"]) == 7


def test_order_can_be_read_back(shop):
    book = add_dune(shop)
    status, order = shop.place_order({"book_id": book["id"], "quantity": 1})

    assert shop.get_order(order["id"]) == (200, order)


def test_unknown_book_gives_404(shop):
    status, body = shop.place_order({"book_id": 99, "quantity": 1})

    assert status == 404


def test_unknown_order_gives_404(shop):
    status, body = shop.get_order(99)

    assert status == 404


def test_not_enough_stock_gives_409_and_changes_nothing(shop):
    book = add_dune(shop, stock=2)

    status, body = shop.place_order({"book_id": book["id"], "quantity": 3})

    assert status == 409
    assert stock_of(shop, book["id"]) == 2


def test_invalid_quantity_gives_400(shop):
    book = add_dune(shop)

    status, body = shop.place_order({"book_id": book["id"], "quantity": 0})

    assert status == 400
