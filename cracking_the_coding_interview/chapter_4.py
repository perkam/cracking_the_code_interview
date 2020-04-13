from typing import List, Tuple

from cracking_the_coding_interview.Graph import Node
from cracking_the_coding_interview.linked_list import LinkedList
from cracking_the_coding_interview.Tree import BinaryTree, TreeNode


def search_path(source: Node, target: Node):
    source_queue = []
    target_queue = []
    source.visited_source = True
    target.visited_target = True
    source_queue.append(source)
    target_queue.append(target)
    while source_queue and target_queue:
        first = source_queue.pop(0)
        if first == target or first.visited_target is True:
            return first.path
        for neighbour in first.neighbours:
            if neighbour.visited_source is False:
                neighbour.path = first.path + neighbour.path
                neighbour.visited_source = True
                source_queue.append(neighbour)

        second = target_queue.pop(0)
        if second == source or second.visited_source is True:
            return second.path
        for neighbour in second.reverse_neighbours:
            if neighbour.visited_target is False:
                neighbour.path.extend(second.path)
                neighbour.visited_target = True
                target_queue.append(neighbour)
    return []


def create_binary_search_tree(elements: List) -> BinaryTree:
    def create_subtree(elements: List):
        if not elements:
            return None
        if len(elements) == 1:
            return TreeNode(elements[0])
        if len(elements) == 2:
            return TreeNode(elements[1], TreeNode(elements[0]))
        middle_index = (len(elements) - 1) // 2
        root = TreeNode(
            elements[middle_index],
            create_subtree(elements[:middle_index]),
            create_subtree(elements[middle_index + 1 :]),
        )
        return root

    return BinaryTree(create_subtree(elements))


def list_of_depths(tree: BinaryTree):
    def add_to_list(node: TreeNode, depth: int, lists: List[LinkedList]):
        if node is None:
            return
        if depth == len(lists):
            lists.append(LinkedList([node]))
        else:
            lists[depth].add(node)
        add_to_list(node.left_child, depth + 1, lists)
        add_to_list(node.right_child, depth + 1, lists)

    lists: List[LinkedList] = []
    add_to_list(tree.root, 0, lists)
    return lists


def list_of_depths_bfs(tree: BinaryTree):
    lists = []
    current = LinkedList()
    if tree.root is not None:
        current.add(tree.root)
    while len(current) != 0:
        lists.append(current)
        parents = current
        current = LinkedList(
            [child for parent in parents for child in parent.value.children]
        )
    return lists


def check_balance(root: TreeNode) -> bool:
    def check_height(root: TreeNode) -> int:
        if root is None:
            return -1
        else:
            left_height = check_height(root.left_child)
            right_height = check_height(root.right_child)
            if abs(left_height - right_height) > 1:
                raise ValueError("Unbalanced tree")
            else:
                return 1 + max(left_height, right_height)

    try:
        check_height(root)
        return True
    except ValueError:
        return False


def validate_bst(root: TreeNode) -> bool:
    def subtree_min_max(root: TreeNode) -> Tuple[int, int]:
        value = root.value
        if root.left_child is not None:
            left_min, left_max = subtree_min_max(root.left_child)
        else:
            left_min, left_max = value, value
        if root.right_child is not None:
            right_min, right_max = subtree_min_max(root.right_child)
        else:
            right_min, right_max = value, value
        if left_max >= value or right_min < value:
            raise ValueError("Subtree is not BST.")
        return (
            min(left_min, left_max, right_min, right_max, value),
            max(left_min, left_max, right_min, right_max, value),
        )

    if root is None:
        return True
    try:
        min_value, max_value = subtree_min_max(root)
        return min_value < root.value <= max_value
    except ValueError:
        return False
