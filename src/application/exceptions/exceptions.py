class EntryNotFoundError(Exception):
    """
    Raise this exception when entry of given id is not available
    """

    def __init__(self, id: int) -> None:
        message = f"Entry not found for id: {id}"
        super().__init__(message)


class InputNotUnique(Exception):
    """
    Raise this exception when input is already exist in database
    """

    def __init__(self, input: str, message: str = "{} has already been taken") -> None:
        message = message.format(input)
        super().__init__(message)
