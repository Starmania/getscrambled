"""GetScrambled

GetScrambled is a simple library that allows you to scramble a image.
No key is needed to unscramble the image, because the key is stored in the image
itself (steganography and least significant bit). The image is scrambled
by shuffling blocks of pixels. The size of the blocks can be set by the user.


Example:

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

Disclaimer:

This library is not meant to be used for security purposes nor to encrypt data.
It will just make harder to see the original image.
"""
