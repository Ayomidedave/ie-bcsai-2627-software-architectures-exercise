# CATALOG - BUSINESS: the rules about books and stock.
# This is also the only part of the catalog that other domains may use.

from catalog import persistence
from errors import InvalidData, NotEnoughStock, NotFound


def add_book(title, price_cents, stock):
    # TODO step 1: move the code from the old business.py here
    raise NotImplementedError("TODO step 1")


def list_books():
    # TODO step 1: move the code from the old business.py here
    raise NotImplementedError("TODO step 1")


def get_price(book_id):
    # TODO step 1: new function. Return the price of the book, or raise NotFound
    raise NotImplementedError("TODO step 1")


def take_stock(book_id, quantity):
    # TODO step 1: new function. The stock check and update that were in place_order:
    #   raise NotFound or NotEnoughStock, otherwise subtract quantity from the stock
    raise NotImplementedError("TODO step 1")
