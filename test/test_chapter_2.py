from cracking_the_coding_interview.chapter_2 import (
    delete_middle_node,
    kth_to_last,
    kth_to_last_recursive,
    palindrome,
    recursive_palindrome,
    remove_dups,
    remove_dups_followup,
    sum_lists,
)
from cracking_the_coding_interview.linked_list import DoublyLinkedList, LinkedList


def test_remove_dups():
    assert remove_dups(
        DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8])
    ) == DoublyLinkedList([1, 2, 3, 4, 5, 8])
    assert remove_dups_followup(
        DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8])
    ) == DoublyLinkedList([1, 2, 3, 4, 5, 8])

    assert (
        kth_to_last(DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8]), 2).value
        == 4
    )
    assert (
        kth_to_last(DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8]), 1).value
        == 8
    )
    assert (
        kth_to_last(DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8]), 5).value
        == 5
    )

    assert (
        kth_to_last_recursive(
            DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8]), 2
        ).value
        == 4
    )
    assert (
        kth_to_last_recursive(
            DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8]), 1
        ).value
        == 8
    )
    assert (
        kth_to_last_recursive(
            DoublyLinkedList([1, 2, 3, 2, 4, 3, 1, 3, 5, 4, 4, 4, 8]), 5
        ).value
        == 5
    )

    li = DoublyLinkedList([7, 1, 6])
    delete_middle_node(li.head.next)
    assert li == DoublyLinkedList([7, 6])

    assert sum_lists(
        DoublyLinkedList([7, 1, 6]), DoublyLinkedList([5, 9, 2])
    ) == DoublyLinkedList([2, 1, 9])
    assert sum_lists(
        DoublyLinkedList([1, 1, 1, 1]), DoublyLinkedList([2, 2])
    ) == DoublyLinkedList([3, 3, 1, 1])

    # assert sum_lists_reversed(DoublyLinkedList([7, 1, 6]), DoublyLinkedList([5, 9, 2])) == DoublyLinkedList([1, 3, 0, 8])
    # assert sum_lists_reversed(DoublyLinkedList([1, 1, 1, 1]), DoublyLinkedList([2, 2])) == DoublyLinkedList([1, 1, 3, 3])

    assert palindrome(LinkedList([1, 2, 3, 2, 1])) is True
    assert palindrome(LinkedList([1, 2, 2])) is False
    assert palindrome(LinkedList([1, 2, 2, 1])) is True

    assert recursive_palindrome(LinkedList([1, 2, 3, 2, 1])) is True
    assert recursive_palindrome(LinkedList([1, 2, 2])) is False
    assert recursive_palindrome(LinkedList([1, 2, 2, 1])) is True
