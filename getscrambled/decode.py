"""Module to decode the image

Example:
```python
from getscrambled import decode
import PIL.Image

img = PIL.Image.open("encoded_image.png")
blocks = decode.extract_data_image(img)

# This is required as stegano closes the image...
img = PIL.Image.open("encoded_image.png")
decoded_img = decode.decode_block(img, blocks)
```
"""
import json

import PIL
import PIL.Image
import stegano

from .exceptions import ImageFormatError
from .shared import arrange_blocks


def extract_data_image(image):
    """Extract the blocks information from the image

    Args:
        image (Image): The image to query from

    Returns:
        blocks (list[tuple[int, int]]): The positions of the blocks
    """
    if isinstance(image, str):
        image = PIL.Image.open(image)

    # This is required as stegano closes the image... For now
    image.close_ = image.close
    image.close = lambda: None

    data = stegano.lsb.reveal(image)
    image.close = image.close_
    del image.close_

    blocks_bad = json.loads(data)
    blocks = [(blocks_bad[i], blocks_bad[i + 1])
              for i in range(0, len(blocks_bad), 2)]

    return blocks


def decode_block(image, blocks: list[tuple[int, int]]):
    """Create a new image with the original blocks arrangement

    Args:
        image (Image): The image to be decoded
        block_size (int, optional). Defaults to BS.

    Raises:
        ImageFormatError: If the image is known to not be a PNG image
    """
    if isinstance(image, str):
        image = PIL.Image.open(image)

    if image.format not in ("PNG", None):
        raise ImageFormatError(image)

    original_size = blocks.pop(0)
    block_size = blocks.pop(0)[0]

    encoded_image = arrange_blocks(image, block_size, blocks, decoding=True)

    cropped_image = encoded_image.crop(
        (0, 0, original_size[0], original_size[1]))

    return cropped_image
