# Creates the shop, starting with no books and no orders.

import persistence
from presentation import ShopAPI


def create_app():
    persistence.reset()
    return ShopAPI()
