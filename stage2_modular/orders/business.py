# ORDERS - BUSINESS: the rules about orders and prices.
# Everything about books is asked to the catalog's business layer.
# Orders never touches the catalog's persistence.

from catalog import business as catalog
from errors import InvalidData, NotFound
from orders import persistence

FREE_SHIPPING_FROM = 5000  # cents
SHIPPING_PRICE = 499  # cents


def calculate_shipping(subtotal_cents):
    # TODO step 2: move the code from the old business.py here
    raise NotImplementedError("TODO step 2")


def place_order(book_id, quantity):
    # TODO step 2: move the code from the old business.py here, but everything about the book
    #   goes through the catalog: catalog.get_price() and catalog.take_stock()
    raise NotImplementedError("TODO step 2")


def get_order(order_id):
    # TODO step 2: move the code from the old business.py here
    raise NotImplementedError("TODO step 2")
