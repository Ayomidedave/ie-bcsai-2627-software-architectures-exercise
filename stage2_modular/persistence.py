# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    book = {"id": len(books) + 1, "title": title, "price_cents": price_cents, "stock": stock}
    books[book["id"]] = book
    return book


def find_book(book_id):
    return books.get(book_id)  # None if it does not exist


def all_books():
    return list(books.values())


def update_stock(book_id, new_stock):
    books[book_id]["stock"] = new_stock


def save_order(order):
    order["id"] = len(orders) + 1
    orders[order["id"]] = order
    return order


def find_order(order_id):
    return orders.get(order_id)  # None if it does not exist
