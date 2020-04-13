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


def one_way(first: str, second: str) -> bool:
    if len(first) + len(second) == 1:
        return True
    if abs(len(first) - len(second)) > 1:
        return False

    def letter_removed(
        first_list: List[str], i: int, second_list: List[str], j: int
    ) -> bool:
        try:
            return first_list[i + 1 :] == second_list[j:]
        except IndexError:
            return False

    def letter_added(
        first_list: List[str], i: int, second_list: List[str], j: int
    ) -> bool:
        try:
            return first_list[i:] == second_list[j + 1 :]
        except IndexError:
            return False

    first_list = list(first)
    second_list = list(second)
    i = 0
    j = 0
    len_first = len(first_list)
    len_second = len(second_list)
    while i < len_first and j < len_second:
        if first_list[i] != second_list[j]:
            if letter_added(first_list, i, second_list, j):
                return True
            elif letter_removed(first_list, i, second_list, j):
                return True
            else:
                if i == len_first - 1 and j == len_second - 1:
                    return True
                else:
                    return first_list[i + 1 :] == second_list[i + 1 :]
        i += 1
        j += 1
    return True


def compress(string: str) -> str:
    if not string:
        return ""
    counter = 0
    i = 0
    counted_letter = string[i]
    counted_string = []
    while i < len(string):
        if string[i] == counted_letter:
            counter += 1
        else:
            counted_string.append(counted_letter)
            counted_string.append(str(counter))
            counted_letter = string[i]
            counter = 1
        i += 1
    counted_string.append(counted_letter)
    counted_string.append(str(counter))
    compressed_string = "".join(counted_string)
    return compressed_string if len(compressed_string) < len(string) else string


class Image(object):
    class Pixel(object):
        def __init__(self, r, g, b, a):
            self.r = r
            self.g = g
            self.b = b
            self.a = a

    def __init__(self, pixel_matrix: List[List[Pixel]]):
        self.image = pixel_matrix
        self.N = len(pixel_matrix)

    def __getitem__(self, key):
        return self.image[key]

    def __len__(self):
        return self.N


def rotate_image_in_place(image: Image, direction: str):
    if direction == "right":
        __rotate_right(image)
    if direction == "left":
        __rotate_left(image)
    else:
        raise ValueError("Incorrect direction: {}".format(direction))


def __rotate_right(image: Image):
    n = len(image)
    pixels_to_switch = n * n
    # f((x, y)) = (y, n - 1 - x)
    # y = (n - 1, 0)
    first_pixel_substitute = image[n - 1][0]
    substituted_pixels = 1
    x = 0
    y = 0
    while substituted_pixels < pixels_to_switch:
        current_pixel = image[x][y]
        next_x = y
        next_y = n - 1 - x
        image[next_x][next_y] = current_pixel
        substituted_pixels += 1
    image[0][0] = first_pixel_substitute


def __rotate_left(image: Image):
    n = len(image)
    pixels_to_switch = n * n
    # f((x, y)) = (y, n - 1 - x)
    # y = (n - 1, 0)
    first_pixel_substitute = image[n - 1][0]
    substituted_pixels = 1
    x = 0
    y = 0
    while substituted_pixels < pixels_to_switch:
        current_pixel = image[x][y]
        next_x = y
        next_y = n - 1 - x
        image[next_x][next_y] = current_pixel
        substituted_pixels += 1
    image[0][0] = first_pixel_substitute
