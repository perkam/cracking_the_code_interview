from typing import Dict, List, Sequence

from bitarray import bitarray


def all_unique_with_hash_table(seq: Sequence) -> bool:
    if len(seq) > 127:
        return False
    elements_counter = {}
    for element in seq:
        if element not in elements_counter:
            elements_counter[element] = True
        else:
            return False
    return True


def all_unique_letters_without_hash_table(sentence: str) -> bool:
    bit_array = bitarray(127)
    bit_array.setall(False)
    for element in sentence:
        if bit_array[ord(element) - ord("a")]:
            return False
        else:
            bit_array[ord(element) - ord("a")] = True
    return True


def count_letters(string: str) -> Dict:
    counter: Dict = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


def check_permutations(a: str, b: str) -> bool:
    elements_counter = count_letters(a)
    for letter in b:
        elements_counter[letter] = elements_counter.get(letter, 0) - 1
        if elements_counter[letter] < 0:
            return False
    return True


def urlify(url: str, letters_count: int) -> str:
    clean_url = []
    whitespace_flag = False
    copied_letters_count = 0
    for letter in url:
        if copied_letters_count == letters_count:
            break
        if letter == " ":
            if whitespace_flag is False:
                clean_url.append("%20")
                whitespace_flag = True
                copied_letters_count += 1
        else:
            whitespace_flag = False
            clean_url.append(letter)
            copied_letters_count += 1
    return "".join(clean_url)


def palindrome_permutation(string: List[str]) -> bool:
    if len(string) == 0:
        return True
    string = sorted([x.lower() for x in string if not x.isspace()])

    counter = 0
    odds_count = 0
    current_char = string[0]

    for char in string:
        if char == current_char:
            counter += 1
        else:
            if counter % 2 != 0:
                odds_count += 1
            counter = 1
            current_char = char
    if counter % 2 != 0:
        odds_count += 1
    return odds_count <= 1
