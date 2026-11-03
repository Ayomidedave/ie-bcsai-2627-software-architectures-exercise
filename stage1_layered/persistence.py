
books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    book_id = len(books) + 1

    book = {
        "id": book_id,
        "title": title,
        "price_cents": price_cents,
        "stock": stock
    }

    books[book_id] = book
    return book


def find_book(book_id):
    return books.get(book_id)


def all_books():
    return list(books.values())


def update_stock(book_id, new_stock):
    books[book_id]["stock"] = new_stock


def save_order(order):
    order_id = len(orders) + 1
    order["id"] = order_id
    orders[order_id] = order
    return order


def find_order(order_id):
    return orders.get(order_id)
