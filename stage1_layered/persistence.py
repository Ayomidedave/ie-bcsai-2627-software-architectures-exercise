# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: create the book dict with the next id, store it in `books` and return it
    raise NotImplementedError("TODO step 1")


def find_book(book_id):
    # TODO step 1: return the book, or None if it does not exist
    raise NotImplementedError("TODO step 1")


def all_books():
    # TODO step 1: return a list with all the books
    raise NotImplementedError("TODO step 1")


def update_stock(book_id, new_stock):
    # TODO step 1: change the stock of the book
    raise NotImplementedError("TODO step 1")


def save_order(order):
    # TODO step 1: give the order the next id, store it in `orders` and return it
    raise NotImplementedError("TODO step 1")


def find_order(order_id):
    # TODO step 1: return the order, or None if it does not exist
    raise NotImplementedError("TODO step 1")
