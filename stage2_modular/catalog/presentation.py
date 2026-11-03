# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request):
    try:
        book = business.add_book(
            request.get("title"),
            request.get("price_cents"),
            request.get("stock")
        )
        return 201, book
    except ShopError as error:
        return error_response(error)


def list_books():
    return 200, business.list_books()