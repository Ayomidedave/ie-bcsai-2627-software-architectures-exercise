# Bookworm online bookshop.
# Everything is in one class: input checks, business rules and data storage.
# It works... but nobody wants to touch it.


def create_app():
    return Shop()


class Shop:
    def __init__(self):
        self.books = []
        self.orders = []

    def add_book(self, request):
        title = request.get("title")
        price = request.get("price_cents")
        stock = request.get("stock")
        if type(title) != str or title == "":
            return 400, {"error": "title is required"}
        if type(price) != int or price <= 0:
            return 400, {"error": "price must be a positive integer"}
        if type(stock) != int or stock < 0:
            return 400, {"error": "stock cannot be negative"}
        book = {"id": len(self.books) + 1, "title": title, "price_cents": price, "stock": stock}
        self.books.append(book)
        print("Added book " + title)
        return 201, book

    def list_books(self):
        return 200, self.books

    def place_order(self, request):
        book_id = request.get("book_id")
        quantity = request.get("quantity")
        if type(book_id) != int or type(quantity) != int or quantity < 1:
            return 400, {"error": "book_id and a positive quantity are required"}

        book = None
        for b in self.books:
            if b["id"] == book_id:
                book = b
        if book == None:
            return 404, {"error": "book not found"}
        if book["stock"] < quantity:
            return 409, {"error": "not enough stock"}

        subtotal = book["price_cents"] * quantity
        if subtotal >= 5000:
            shipping = 0
        else:
            shipping = 499

        book["stock"] = book["stock"] - quantity
        order = {
            "id": len(self.orders) + 1,
            "book_id": book_id,
            "quantity": quantity,
            "subtotal_cents": subtotal,
            "shipping_cents": shipping,
            "total_cents": subtotal + shipping,
        }
        self.orders.append(order)
        print("Order placed for " + book["title"])
        return 201, order

    def get_order(self, order_id):
        for o in self.orders:
            if o["id"] == order_id:
                return 200, o
        return 404, {"error": "order not found"}
