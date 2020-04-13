from typing import Any


class BigStack(object):
    def __init__(self, capacity: int, number_of_stacks: int):
        len_of_stack = capacity // number_of_stacks + number_of_stacks
        self.__capacity = len_of_stack * number_of_stacks * 2
        self.__stack = [None] * self.__capacity * 2

        self.__heads = [x * len_of_stack for x in range(number_of_stacks)]
        self.__tails = [x * len_of_stack for x in range(number_of_stacks)]
        self.__sizes = [0] * number_of_stacks
        self.__capacities = [len_of_stack] * number_of_stacks
        self.__last_stack = number_of_stacks - 1

    def pop(self, stack_index: int) -> Any:
        if self.__sizes[stack_index] == 0:
            raise IndexError("Pop from empty list")
        tail = self.__tails[stack_index]
        item = self.__stack[tail]
        if tail - 1 < 0:
            new_tail = self.__capacity - 1
        else:
            new_tail = tail - 1
        self.__tails[stack_index] = new_tail
        self.__sizes[stack_index] -= 1
        return item

    def push(self, item: Any, stack_index: int) -> Any:
        if self.__sizes[stack_index] == self.__capacities[stack_index]:
            self.__reallocate_stack(stack_index)
        self.__stack[self.__tails[stack_index]] = item
        self.__tails[stack_index] = (self.__tails[stack_index] + 1) % self.__capacity
        self.__sizes[stack_index] += 1

    def peek(self, stack_index: int) -> Any:
        return self.__stack[self.__tails[stack_index]]

    def is_empty(self, stack_index: int) -> bool:
        return self.__sizes[stack_index] == 0

    def __reallocate_stack(self, stack_index: int):
        if sum(self.__sizes) + self.__sizes[stack_index] >= self.__capacity:

            self.__stack.extend([None] * self.__capacity)
            self.__capacity *= 2
            for x in range(len(self.__heads)):
                self.__reallocate_stack(x)
        else:
            self.__capacities[stack_index] *= 2
            new_head = self.__tails[self.__last_stack]
            new_tail = (new_head + self.__capacities[stack_index]) % self.__capacity
            if new_tail < new_head:
                self.__stack[new_head:] = self.__stack[
                    self.__heads[stack_index] : len(self.__stack[new_head:])
                ]
                self.__stack[0:new_tail] = self.__stack[
                    len(self.__stack[new_head:]) : self.__tails[stack_index]
                ]
            else:
                self.__stack[new_head:new_tail] = self.__stack[
                    self.__heads[stack_index] : self.__tails[stack_index]
                ]
            self.__heads[stack_index] = new_head
            self.__tails[stack_index] = new_tail
            self.__last_stack = stack_index


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0


class StackWithMin(Stack):
    def __init__(self):
        super(StackWithMin, self).__init__()
        self.__mins = Stack()

    def push(self, item):
        if self.__mins.is_empty():
            self.__mins.push(item)
        elif item <= self.__mins.peek():
            self.__mins.push(item)
        super().push(item)

    def pop(self):
        item = super().pop()
        if item == self.__mins.peek():
            self.__mins.pop()
        return item

    def min(self):
        return self.__mins.peek()


class StackOfPlates(Stack):
    def __init__(self, capacity: int):
        super(StackOfPlates, self).__init__()
        self.__stacks = Stack()
        self.__curent_size = 0
        self.__capacity = capacity

    def push(self, item):
        if self.__curent_size == self.__capacity or self.__stacks.is_empty():
            self.__stacks.push(Stack())
            self.__curent_size = 0
        self.__stacks.peek().push(item)
        self.__curent_size += 1

    def peek(self):
        return self.__stacks.peek().peek()

    def pop(self):
        item = self.__stacks.peek().pop()
        self.__curent_size -= 1
        if self.__curent_size == 0:
            self.__stacks.pop()
        return item

    def is_empty(self):
        return self.__stacks.is_empty()
