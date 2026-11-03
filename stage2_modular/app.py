# Creates the shop, starting with no books and no orders.
#
# STARTING POINT: the shop still uses the layered code from stage 1
# (business.py, persistence.py, presentation.py).
# In step 3 you will build it from the catalog/ and orders/ domains instead.

# Creates the shop using the catalog and orders domains.

from catalog import persistence as catalog_persistence
from orders import persistence as orders_persistence
from catalog import presentation as catalog_presentation
from orders import presentation as orders_presentation


class ShopAPI:

    def add_book(self, request):
        return catalog_presentation.add_book(request)

    def list_books(self):
        return catalog_presentation.list_books()

    def place_order(self, request):
        return orders_presentation.place_order(request)

    def get_order(self, order_id):
        return orders_presentation.get_order(order_id)


def create_app():
    catalog_persistence.reset()
    orders_persistence.reset()
    return ShopAPI()