
# PRESENTATION LAYER: receives requests and returns status codes.

import business


class ShopAPI:

    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"),
                request.get("price_cents"),
                request.get("stock")
            )

            return 201, book

        except business.ShopError as error:
            return self.handle_error(error)

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(
                request.get("book_id"),
                request.get("quantity")
            )

            return 201, order

        except business.ShopError as error:
            return self.handle_error(error)

    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)

            return 200, order

        except business.ShopError as error:
            return self.handle_error(error)

    def handle_error(self, error):

        if isinstance(error, business.InvalidData):
            return 400, {"error": str(error)}

        if isinstance(error, business.NotFound):
            return 404, {"error": str(error)}

        if isinstance(error, business.NotEnoughStock):
            return 409, {"error": str(error)}
