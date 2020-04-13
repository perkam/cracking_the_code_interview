from random import randint
from typing import Any


class LinkedListNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __eq__(self, other):
        if not isinstance(other, LinkedListNode):
            return False
        return self.value == other.value

    def __ne__(self, other):
        if not isinstance(other, LinkedListNode):
            return True
        return self.value != other.value

    def __str__(self) -> str:
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

    def __add__(self, other):
        return self.value + other.value


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a.value != b.value:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __str__(self) -> str:
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __repr__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self) -> int:
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value: Any) -> LinkedListNode:
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value: Any) -> LinkedListNode:
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values: Any):
        for v in values:
            self.add(v)

    def generate(self, n: int, min_value: int, max_value: int):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


class DoublyLinkedList(LinkedList):
    def add(self, value: Any):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value, None, self.tail)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self
