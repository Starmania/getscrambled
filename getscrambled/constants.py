# pylint: disable=invalid-name
"""Constants for the getscrambled project.

    To edit theses constants at runtime, do this:

    ```python
    from getscrambled.constants import constants
    constants.BLOCK_SIZE = 64
    ```
"""


class Constants:
    """Constants for the project. Could be edited.
    """

    def __init__(self):
        self._block_size = 64
        self._bg_color = (255, 255, 255)

    @property
    def BLOCK_SIZE(self) -> int:
        """The size of the blocks in the image when encoding or decoding. Defaults to 64.
        """
        return self._block_size

    @BLOCK_SIZE.setter
    def BLOCK_SIZE(self, value: int):
        if not isinstance(value, int):
            raise TypeError("BLOCK_SIZE must be an integer.")
        if value < 1:
            raise ValueError("BLOCK_SIZE must be greater than 0.")
        self._block_size = value

    @property
    def BACKGROUND_COLOR(self) -> tuple[int, int, int]:
        """The color of the added pixels when expanding the image. Defaults to white.
        """
        return self._bg_color

    @BACKGROUND_COLOR.setter
    def BACKGROUND_COLOR(self, value: tuple[int, int, int]):
        if not isinstance(value, tuple):
            raise TypeError("BACKGROUND_COLOR must be a tuple.")
        if not len(value) == 3:
            raise ValueError("BACKGROUND_COLOR must have 3 values.")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("All values in BACKGROUND_COLOR must be integers.")
        self._bg_color = value


constants = Constants()
