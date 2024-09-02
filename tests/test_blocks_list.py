from getscrambled.encode import create_block_grid


def test_create_block_grid_simple():
    block_size = 16
    width, height = 32, 32
    assert_result = [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert create_block_grid(width, height, block_size) == assert_result


def test_create_block_grid_not_multiple():
    block_size = 16
    width, height = 33, 33
    assert_result = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1),
                     (1, 2), (2, 0), (2, 1), (2, 2)]
    assert create_block_grid(width, height, block_size) == assert_result


def test_create_block_grid_not_multiple_2():
    block_size = 16
    width, height = 33, 32
    assert_result = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    assert create_block_grid(width, height, block_size) == assert_result
