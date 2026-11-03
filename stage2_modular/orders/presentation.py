# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request):
    try:
        order = business.place_order(
            request.get("book_id"),
            request.get("quantity")
        )
        return 201, order

    except ShopError as error:
        return error_response(error)


def get_order(order_id):
    try:
        return 200, business.get_order(order_id)

    except ShopError as error:
        return error_response(error)