from cracking_the_coding_interview.chapter_1 import (
    all_unique_letters_without_hash_table,
    all_unique_with_hash_table,
    check_permutations,
    compress,
    one_way,
    palindrome_permutation,
    urlify,
)


def test_chapter_1():
    assert all_unique_with_hash_table("abcdf") is True
    assert all_unique_with_hash_table("") is True
    assert all_unique_with_hash_table("avvs") is False

    assert all_unique_letters_without_hash_table("abcdf") is True
    assert all_unique_letters_without_hash_table("") is True
    assert all_unique_letters_without_hash_table("avvs") is False

    assert check_permutations("abs", "bsa") is True
    assert check_permutations("abc", "abca") is False
    assert check_permutations("abs", "abc") is False

    assert urlify("John smith", 10) == "John%20smith"
    assert urlify("abcds", 5) == "abcds"
    assert urlify("", 0) == ""
    assert urlify("dsadsa       aaa        ", 11) == "dsadsa%20aaa%20"
    assert urlify("aa  ", 2) == "aa"
    assert urlify("dsadsa       aaa        ", 10) == "dsadsa%20aaa"

    assert palindrome_permutation(list("Tact coa")) is True
    assert palindrome_permutation(list("")) is True
    assert palindrome_permutation(list("a")) is True
    assert palindrome_permutation(list("a11")) is True
    assert palindrome_permutation(list("abb c")) is False
    assert palindrome_permutation(list("abbc")) is False

    assert one_way("", "a") is True
    assert one_way("a", "") is True
    assert one_way("ab", "") is False
    assert one_way("ab", "b") is True
    assert one_way("abcsds", "abcdds") is True
    assert one_way("abb", "abbxd") is False
    assert one_way("bb", "abbew") is False
    assert one_way("abcd", "xbcd") is True

    assert compress("aaabcccccaaa") == "a3b1c5a3"
    assert compress("") == ""
    assert compress("a") == "a"
    assert compress("aa") == "aa"
    assert compress("abcd") == "abcd"
    assert compress("aabbbqqpppzz") == "a2b3q2p3z2"
