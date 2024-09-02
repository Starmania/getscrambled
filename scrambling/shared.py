import itertools
import math
import typing

import PIL
import PIL.Image

from .constants import BLOCK_SIZE as BS
from .constants import BACKGROUND_COLOR as BC

if typing.TYPE_CHECKING:
    Image = PIL.Image.Image


def _get_max_size(size: tuple[int, int], block_size: int):
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


def expand_image(image: "Image", block_size: int = BS, color=BC) -> "Image":
    """Resize the canvas of the image to be a multiple of the block size.

    This function does not modify the existing pixels,
    it just adds white pixels to the right and bottom of the image.


    Args:
        image (Image): The image to be expanded.
        block_size (int, optional): The size of the blocks. Defaults to BLOCK_SIZE.
        color (int, optional): The color of the added pixels. Defaults to BC (white).
    """
    max_size = _get_max_size(image.size, block_size)
    expanded_image = PIL.Image.new(image.mode, max_size, color=color)
    expanded_image.paste(image, (0, 0))
    return expanded_image


def arrange_blocks(image: "Image", block_size: int, blocks, decoding=False):
    """Create a new image with the blocks arranged in the positions given by the list "blocks"

    This function could encode or decode an image.

    Args:
        image (Image): The original image
        block_size (int)
        blocks (list[tuple[int, int]]): The positions of the blocks

    Returns:
        Image: The new image with the blocks arranged
    """
    original_blocks = create_block_grid(*image.size, block_size)

    max_size = _get_max_size(image.size, block_size)
    encoded_image = PIL.Image.new(image.mode, max_size, color=BC)

    if image.size != max_size:
        extended_image = expand_image(image, block_size)
        extended_image.filename = image.filename
    else:
        extended_image = image

    generator = zip(blocks, original_blocks) if decoding else zip(
        original_blocks, blocks)

    for (x, y), (ox, oy) in generator:
        block = image.crop((x * block_size, y * block_size,
                            x * block_size + block_size, y * block_size + block_size))
        encoded_image.paste(block, (ox * block_size, oy * block_size))
    return encoded_image
