# BUSINESS LAYER: the rules of the shop.
# It uses the persistence layer to store and find data.
# It knows nothing about requests or status codes: when something is wrong it raises an error.

import persistence

FREE_SHIPPING_FROM = 5000  # cents
SHIPPING_PRICE = 499  # cents


class ShopError(Exception):
    pass


class InvalidData(ShopError):
    pass


class NotFound(ShopError):
    pass


class NotEnoughStock(ShopError):
    pass


def calculate_shipping(subtotal_cents):
    # TODO step 2: 0 from FREE_SHIPPING_FROM cents, otherwise SHIPPING_PRICE
    raise NotImplementedError("TODO step 2")


def add_book(title, price_cents, stock):
    # TODO step 2: check the data (raise InvalidData) and save the book with persistence.save_book
    raise NotImplementedError("TODO step 2")


def list_books():
    # TODO step 2: return all the books, using the persistence layer
    raise NotImplementedError("TODO step 2")


def place_order(book_id, quantity):
    # TODO step 2: move the order logic from presentation.py here.
    #   invalid book_id or quantity -> raise InvalidData
    #   book does not exist         -> raise NotFound
    #   not enough stock            -> raise NotEnoughStock
    #   otherwise: compute the price (use calculate_shipping), update the stock,
    #   save the order and return it (use the persistence layer)
    raise NotImplementedError("TODO step 2")


def get_order(order_id):
    # TODO step 2: return the order, or raise NotFound
    raise NotImplementedError("TODO step 2")
