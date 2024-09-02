# pylint: disable=E0401, E0611, W0621, C0116, C0115, C0114
import PIL.Image
import pytest

from scrambling.shared import expand_image


@pytest.fixture
def get_image_100():
    return PIL.Image.new("RGB", (100, 100))


@pytest.fixture
def get_image_64():
    return PIL.Image.new("RGB", (64, 64))


@pytest.fixture
def get_image_64_100():
    return PIL.Image.new("RGB", (64, 100))


@pytest.fixture
def get_image_20():
    return PIL.Image.new("RGB", (20, 20))


def test_expand_image_100(get_image_100):
    expanded_image = expand_image(get_image_100, 64)
    assert expanded_image.size == (128, 128)


def test_expand_image_64(get_image_64):
    expanded_image = expand_image(get_image_64, 64)
    assert expanded_image.size == (64, 64)


def test_expand_image_64_100(get_image_64_100):
    expanded_image = expand_image(get_image_64_100, 64)
    assert expanded_image.size == (64, 128)


def test_expand_image_20(get_image_20):
    expanded_image = expand_image(get_image_20, 64)
    assert expanded_image.size == (64, 64)
