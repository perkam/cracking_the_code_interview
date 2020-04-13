from cracking_the_coding_interview.chapter_3 import StackOfPlates, StackWithMin


def test_min():
    stack = StackWithMin()
    stack.push(0)
    assert stack.is_empty() is False
    assert stack.min() == 0
    stack.push(1)
    assert stack.peek() == 1
    assert stack.min() == 0
    stack.push(-1)
    assert stack.min() == -1
    stack.push(1)
    assert stack.min() == -1
    assert stack.pop() == 1
    assert stack.pop() == -1
    assert stack.min() == 0
    assert stack.pop() == 1
    assert stack.pop() == 0


def test_stack_of_plates():
    stack = StackOfPlates(2)
    stack.push(0)
    assert stack.is_empty() is False
    stack.push(1)
    assert stack.peek() == 1
    stack.push(-1)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == -1
    assert stack.pop() == 1
    assert stack.pop() == 0
