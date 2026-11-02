# PRESENTATION LAYER: receives requests and returns (status code, body).
# It only calls the business layer and turns its errors into status codes.

import business
from business import InvalidData, NotEnoughStock, NotFound, ShopError

STATUS_CODES = {InvalidData: 400, NotFound: 404, NotEnoughStock: 409}


class ShopAPI:
    def add_book(self, request):
        try:
            return 201, business.add_book(request.get("title"), request.get("price_cents"), request.get("stock"))
        except ShopError as error:
            return STATUS_CODES[type(error)], {"error": str(error)}

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            return 201, business.place_order(request.get("book_id"), request.get("quantity"))
        except ShopError as error:
            return STATUS_CODES[type(error)], {"error": str(error)}

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except ShopError as error:
            return STATUS_CODES[type(error)], {"error": str(error)}
