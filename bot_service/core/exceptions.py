class InvalidExpenseError(Exception):
    """Error lanzado cuando el mensaje no es válido para agregar un gasto."""
    pass

class UserNotWhitelistedError(Exception):
    """Error lanzado cuando un usuario no está en la whitelist."""
    pass
