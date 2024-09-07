# GetScrambled ![python](https://img.shields.io/badge/python->=3.9_<3.13-blue)

---

## Description

GetScrambled is a simple library that allows you to scramble a image. No key is needed to unscramble the image, because the key is stored in the image itself (steganography and least significant bit). The image is scrambled by shuffling blocks of pixels. The size of the blocks can be set by the user.

The library uses pillow for image manipulation.

## Example

```python
from getscrambled.encode import encode
from PIL import Image

# Encode
image = Image.open("tests/data/baboon.png")
scrambled_image = encode(image, block_size=16)
scrambled_image.save("tests/artifacts/baboon_scrambled.png")

# Decode
from getscrambled.decode import decode
decoded_image = decode(scrambled_image)
decoded_image.save("tests/artifacts/baboon_decoded.png")
```
### Original and scrambled image
<img src="https://github.com/Starmania/getscrambled/blob/main/tests/data/baboon.png?raw=true" alt="baboon" style="width: 45%;"> <img src="https://github.com/Starmania/getscrambled/blob/main/tests/data/baboon_scrambled.png?raw=true" alt="baboon_scrambled" style="width: 45%;">

## Installation

```bash
pip install getscrambled
```

## Development and testing

```bash
git clone https://github.com/Starmania/getscrambled
cd getscrambled
poetry install
poetry run pytest
```

## Disclaimer ![warning](https://img.shields.io/badge/-warning-red)

This library is not meant to be used for security purposes nor to encrypt data. It will just make harder to see the original image. You could check that I never use the word "encrypt" in this repository.

## Todo

- [ ] More tests
