from cracking_the_coding_interview.chapter_5 import insertion


def test_insertion():
    n = 0b10000000000
    m = 0b10011
    assert insertion(n, m, 2, 6) == 0b10001001100
