# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: move the code from the old persistence.py here
    raise NotImplementedError("TODO step 1")


def find_book(book_id):
    # TODO step 1: move the code from the old persistence.py here
    raise NotImplementedError("TODO step 1")


def all_books():
    # TODO step 1: move the code from the old persistence.py here
    raise NotImplementedError("TODO step 1")


def update_stock(book_id, new_stock):
    # TODO step 1: move the code from the old persistence.py here
    raise NotImplementedError("TODO step 1")
