import json

import PIL
import PIL.Image
import stegano

from .exceptions import ImageFormatError
from .constants import BLOCK_SIZE as BS
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

    data = stegano.lsb.reveal(image)
    blocks_bad = json.loads(data)
    blocks = [(blocks_bad[i], blocks_bad[i + 1])
              for i in range(0, len(blocks_bad), 2)]

    return blocks


def decode_block(image, blocks: list[tuple[int, int]], block_size: int = BS):
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

    encoded_image = arrange_blocks(image, block_size, blocks, decoding=True)

    cropped_image = encoded_image.crop(
        (0, 0, original_size[0], original_size[1]))

    return cropped_image