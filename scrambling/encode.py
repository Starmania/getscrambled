import itertools
import math

import PIL
import PIL.Image
import numpy as np
import stegano

from .exceptions import ImageFormatError
from .constants import BLOCK_SIZE as BS
from .constants import BACKGROUND_COLOR as BC


def _get_max_size(size, block_size):
    return (math.ceil(size[0] / block_size) * block_size,
            math.ceil(size[1] / block_size) * block_size)


def create_block_grid(width: int, height: int, block_size: int = BS) -> list[tuple[int, int]]:
    """Create a grid of blocks positions.

    Order: left to right (1), top to bottom (0)

    Args:
        width (int)
        height (int)
        block_size (int, optional): Defaults to BS.

    Returns:
        list[tuple[int, int]]: A list of tuples with the positions of the blocks
    """
    blocks_zipped = itertools.product(
        range(math.ceil(width / block_size)),
        range(math.ceil(height / block_size))
    )
    return sorted(blocks_zipped)


def expand_image(image: PIL.Image.Image, block_size=BS, color=BC) -> PIL.Image.Image:
    """Resize the canvas of the image to be a multiple of the block size.

    This function does not modify the existing pixels,
    it just adds white pixels to the right and bottom of the image.


    Args:
        image (PIL.Image.Image): The image to be expanded.
        block_size (int, optional): The size of the blocks. Defaults to BLOCK_SIZE.
        color (int, optional): The color of the added pixels. Defaults to BC (white).
    """
    max_size = _get_max_size(image.size, block_size)
    expanded_image = PIL.Image.new(image.mode, max_size, color=color)
    expanded_image.paste(image, (0, 0))
    return expanded_image


def add_data_image(image, blocks):
    if isinstance(image, str):
        image = PIL.Image.open(image)

    if image.format != "PNG":
        raise ImageFormatError(image)

    # Minimise the size of the variable "blocks"
    blocks = tuple((int(x), int(y)) for x, y in blocks)

    return stegano.lsb.hide(image, blocks)


def encode_block(image, block_size=BS):
    """Create a new image with an random arrangement of the blocks of the original image

    Args:
        image (_type_): _description_
        block_size (_type_, optional): _description_. Defaults to BS.

    Raises:
        ImageFormatError: _description_
    """
    if isinstance(image, str):
        image = PIL.Image.open(image)

    if image.format != "PNG":
        raise ImageFormatError(image)

    max_size = _get_max_size(image.size, block_size)
    encoded_image = PIL.Image.new(image.mode, max_size, color=BC)

    if image.size != max_size:
        extended_image = expand_image(image, block_size)
        extended_image.filename = image.filename
    else:
        extended_image = image

    # Generate blocks positions
    blocks = create_block_grid(*image.size, block_size)

    # Shuffle blocks
    np.random.shuffle(blocks)

    for (x, y) in blocks:
        block = image.crop((x * block_size, y * block_size,
                            x * block_size + block_size, y * block_size + block_size))
        encoded_image.paste(block, (x * block_size, y * block_size))

    blocks.insert(0, image.size)  # So we can recover the original image size

    return blocks, encoded_image
