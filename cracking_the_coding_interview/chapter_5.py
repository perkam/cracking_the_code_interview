def get_mask(i: int, j: int) -> int:
    # all 1s before i eg: 111000000
    left_submask = -1 << (j + 1)
    # all 1s after j eg:  000000111
    right_sumbask = (1 << i) - 1
    return left_submask | right_sumbask


def insertion(n: int, m: int, i: int, j: int):
    mask = get_mask(i, j)
    empty_n = n & mask
    shifted_m = m << i
    return empty_n | shifted_m
