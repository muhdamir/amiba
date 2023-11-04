class EntryNotFoundError(Exception):
    """
    Raise this exception when entry of given id is not available
    """

    def __init__(self, id: int) -> None:
        message = f"Entry not found for id: {id}"
        super().__init__(message)
