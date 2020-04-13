from typing import Any


def pprint_tree(node, file=None, _prefix="", _last=True):
    if node is None:
        return
    print(_prefix, "`- " if _last else "|- ", node.value, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)


class TreeNode(object):
    def __init__(self, value: Any, left: Any = None, right: Any = None):
        self.value = value
        self.left_child = left
        self.right_child = right
        self.children = []
        if left is not None:
            self.children.append(left)
        if right is not None:
            self.children.append(right)


# This funtcion is here just to test
def preOrder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrder(node.left_child)
    preOrder(node.right_child)


# function to return the index of
# close parenthesis
def findIndex(Str, si, ei):
    if si > ei:
        return -1

    # Inbuilt stack
    s = []
    for i in range(si, ei + 1):

        # if open parenthesis, push it
        if Str[i] == "(":
            s.append(Str[i])

            # if close parenthesis
        elif Str[i] == ")":
            if s[-1] == "(":
                s.pop(-1)

                # if stack is empty, this is
                # the required index
                if len(s) == 0:
                    return i
                    # if not found return -1
    return -1


# function to conStruct tree from String
def treeFromString(Str, si, ei):
    # Base case
    if si > ei:
        return None

    # new root
    root = TreeNode(ord(Str[si]) - ord("0"))
    index = -1

    # if next char is '(' find the
    # index of its complement ')'
    if si + 1 <= ei and Str[si + 1] == "(":
        index = findIndex(Str, si + 1, ei)

        # if index found
    if index != -1:
        # call for left subtree
        root.left_child = treeFromString(Str, si + 2, index - 1)

        # call for right subtree
        root.right_child = treeFromString(Str, index + 2, ei - 1)
    return root


class BinaryTree(object):
    def __init__(self, root):
        self.root = root
