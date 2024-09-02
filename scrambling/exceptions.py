"""Module for exceptions used in the scrambling package.
"""
import PIL.Image


class ImageFormatError(ValueError):
    """Exception raised when an image is not in PNG format.
    """

    def __init__(self, image: PIL.Image.Image):
        self.image = image

    def __str__(self):
        return f"Image ({self.image}) format must be PNG, not {self.image.format}"
