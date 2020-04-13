from itertools import zip_longest
from typing import List

from cracking_the_coding_interview.linked_list import (
    DoublyLinkedList,
    LinkedList,
    LinkedListNode,
)


def remove_dups(linked_list: DoublyLinkedList):
    if linked_list.head is None:
        return
    existing_nodes = set()
    for node in linked_list:
        if node not in existing_nodes:
            existing_nodes.add(node)
        else:
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
    return linked_list


def remove_dups_followup(linked_list: DoublyLinkedList):
    first_idx = linked_list.head
    if first_idx.next is not None:
        second_idx = first_idx.next
    while first_idx.next is not None:
        if second_idx == first_idx:
            if second_idx.prev is not None:
                second_idx.prev.next = second_idx.next
            if second_idx.next is not None:
                second_idx.next.prev = second_idx.prev
        if second_idx.next is not None:
            second_idx = second_idx.next
        else:
            first_idx = first_idx.next
            second_idx = first_idx.next
    return linked_list


def kth_to_last(linked_list: LinkedList, k: int):
    counter = 1
    current = linked_list.head
    while current.next is not None:
        counter += 1
        current = current.next

    counter = counter - k
    node = linked_list.head
    while counter != 0:
        node = node.next
        counter -= 1

    return node


def kth_to_last_recursive(linked_list: LinkedList, k: int):
    def find_node(node: LinkedListNode):
        if node.next is None:
            if k == 1:
                return 1, node
            else:
                return 1, None
        nodes_ahead_count, found_node = find_node(node.next)
        if nodes_ahead_count + 1 == k:
            found_node = node
        return nodes_ahead_count + 1, found_node

    count, found_node = find_node(linked_list.head)
    if found_node is None:
        raise ValueError(
            "k(" + str(k) + ") is bigger than list length(" + str(count) + ")"
        )
    else:
        return found_node


def delete_middle_node(node: LinkedListNode):
    if node.next is not None:
        node.value = node.next.value
        node.next = node.next.next


def sum_lists(first: LinkedList, second: LinkedList) -> LinkedList:
    reminder = 0
    summed_list = LinkedList()
    for a, b in zip_longest(first, second, fillvalue=LinkedListNode(0)):
        sum = a.value + b.value + reminder
        summed_list.add(sum % 10)
        reminder = sum // 10
    return summed_list


def sum_lists_reversed(first: LinkedList, second: LinkedList) -> LinkedList:
    summed_list = LinkedList()

    def sum_nodes(a: LinkedListNode, b: LinkedListNode):
        if a.next is None and b.next is None:
            sum = a.value + b.value
            summed_list.add_to_beginning(sum % 10)
            return sum // 10
        elif a.next is None and b.next is not None:
            reminder = sum_nodes(LinkedListNode(0), b.next)
        elif a.next is not None and b.next is None:
            reminder = sum_nodes(a.next, LinkedListNode(0))
        else:
            reminder = sum_nodes(a.next, b.next)
        sum = a.value + b.value + reminder
        summed_list.add_to_beginning(sum % 10)
        return sum // 10

    reminder = sum_nodes(first.head, second.head)
    if reminder != 0:
        summed_list.add_to_beginning(reminder)
    return LinkedList(summed_list)


def palindrome(linked_list: LinkedList) -> bool:
    n = len(linked_list)
    if n == 0:
        return True
    checked_elements = []
    i = 1
    node = linked_list.head
    while node is not None:
        if i <= n // 2:
            checked_elements.append(node.value)

        if i == n // 2 + 1 and n % 2 != 0:
            node = node.next
            i += 1
            continue

        if i >= n // 2 + 1:
            if node.value != checked_elements.pop():
                return False
        node = node.next
        i += 1
    return True


def recursive_palindrome(linked_list: LinkedList) -> bool:
    queue: List[LinkedListNode] = []

    def palindrome_helper(node, queue: List):
        if node is None:
            return queue
        queue.append(node.value)
        palindrome_helper(node.next, queue)
        if queue.pop(0) != node.value:
            return False
        if len(queue) == 0:
            return True

    return palindrome_helper(linked_list.head, queue)
