# STEP 2: the orders domain, with its own three layers.
#     orders/presentation.py -> orders/business.py -> orders/persistence.py
# Orders needs prices and stock: it asks catalog/business.py, never catalog/persistence.py.
# Fails at the start. Passes when the three files in orders/ are done.

import pytest

from catalog import business as catalog_business
from catalog import persistence as catalog_persistence
from layer_rules import check_layers, imports_in
from orders import business, persistence, presentation


@pytest.fixture(autouse=True)
def empty_shop():
    catalog_persistence.reset()
    persistence.reset()


def test_orders_respects_its_layers():
    check_layers("orders")


def test_orders_only_uses_the_catalog_business_layer():
    for file in ["orders/presentation.py", "orders/business.py", "orders/persistence.py"]:
        for line in imports_in(file):
            if "catalog" in line:
                assert "persistence" not in line and "presentation" not in line, f"{file}: {line}"


def test_catalog_does_not_use_orders():
    for file in ["catalog/presentation.py", "catalog/business.py", "catalog/persistence.py"]:
        assert not any("orders" in line for line in imports_in(file)), file


def test_persistence_saves_and_finds_orders():
    order = persistence.save_order({"book_id": 1, "quantity": 2})

    assert persistence.find_order(order["id"]) == order
    assert persistence.find_order(99) is None


@pytest.mark.parametrize("subtotal, shipping", [(4999, 499), (5000, 0)])
def test_business_shipping_rule(subtotal, shipping):
    assert business.calculate_shipping(subtotal) == shipping


def test_business_places_an_order_using_the_catalog():
    book = catalog_business.add_book("Dune", 1500, 10)

    order = business.place_order(book["id"], 2)

    assert order["total_cents"] == 3499
    assert catalog_persistence.find_book(book["id"])["stock"] == 8


def test_presentation_answers_with_status_codes():
    book = catalog_business.add_book("Dune", 1500, 1)

    assert presentation.place_order({"book_id": book["id"], "quantity": 1})[0] == 201
    assert presentation.place_order({"book_id": book["id"], "quantity": 1})[0] == 409
    assert presentation.place_order({"book_id": 99, "quantity": 1})[0] == 404
    assert presentation.get_order(1)[0] == 200
