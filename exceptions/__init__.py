class BombException(Exception):
    pass


class BombParseException(BombException):
    pass


class BombRuntimeException(BombException):
    pass


class BombIllegalDefinitionException(BombRuntimeException):
    pass

