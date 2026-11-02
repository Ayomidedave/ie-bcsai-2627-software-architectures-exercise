# Errors shared by all domains, and how presentation turns them into status codes.


class ShopError(Exception):
    pass


class InvalidData(ShopError):
    pass


class NotFound(ShopError):
    pass


class NotEnoughStock(ShopError):
    pass


STATUS_CODES = {InvalidData: 400, NotFound: 404, NotEnoughStock: 409}


def error_response(error):
    return STATUS_CODES[type(error)], {"error": str(error)}
