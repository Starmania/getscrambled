from PIL import Image

from getscrambled.encode import encode
from getscrambled.decode import decode


def test_general_smoke():
    """Test the general functionality of the package.

    If this test passes, it means that the most basic functionality of the package is working.
    """
    image = Image.open("tests/data/baboon.png")
    scrambled_image = encode(image, block_size=16)
    scrambled_image.save("tests/artifacts/baboon_scrambled.png")

    decoded_image = decode(scrambled_image)
    decoded_image.save("tests/artifacts/baboon_decoded.png")
