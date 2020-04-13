from cracking_the_coding_interview.chapter_4 import (
    check_balance,
    create_binary_search_tree,
    list_of_depths,
    list_of_depths_bfs,
    search_path,
    validate_bst,
)
from cracking_the_coding_interview.Graph import Graph
from cracking_the_coding_interview.Tree import BinaryTree, pprint_tree, treeFromString


def test_search_path():
    graph_string = (
        "1->2\n"
        "1->3\n"
        "3->4\n"
        "4->1\n"
        "3->5\n"
        "5->6\n"
        "6->7\n"
        "4->7\n"
        "6->8\n"
        "8->9\n"
        "9->7\n"
        "9->4\n"
    )
    graph = Graph(graph_string)
    assert str(search_path(graph.get_node(1), graph.get_node(8))) == "[1, 3, 5, 6, 8]"
    graph = Graph("1->1")
    assert str(search_path(graph.get_node(1), graph.get_node(1))) == "[1]"
    graph = Graph("1->2")
    assert str(search_path(graph.get_node(1), graph.get_node(2))) == "[1, 2]"
    graph = Graph("1->2")
    assert search_path(graph.get_node(2), graph.get_node(1)) == []

    b_tree = create_binary_search_tree([1, 3, 4, 6, 8, 10, 11])
    print("\n")
    pprint_tree(b_tree.root)

    b_tree = create_binary_search_tree([1, 3, 4, 6])
    print("\n")
    pprint_tree(b_tree.root)

    tree = create_binary_search_tree([1, 3, 4, 6, 8, 10, 11])
    lists = list_of_depths(tree)
    assert [x.value.value for x in lists[0]] == [6]
    assert [x.value.value for x in lists[1]] == [3, 10]
    assert [x.value.value for x in lists[2]] == [1, 4, 8, 11]

    lists = list_of_depths_bfs(tree)
    assert [x.value.value for x in lists[0]] == [6]
    assert [x.value.value for x in lists[1]] == [3, 10]
    assert [x.value.value for x in lists[2]] == [1, 4, 8, 11]

    tree = BinaryTree(
        treeFromString(
            "4(2(3)(1))(6(5(3(1)(2))(4)))", 0, len("4(2(3)(1))(6(5(3(1)(2))(4)))") - 1
        )
    )
    assert check_balance(tree.root) is False
    tree = create_binary_search_tree([1, 3, 4, 6, 8, 10, 11])
    assert check_balance(tree.root) is True

    tree = BinaryTree(
        treeFromString(
            "4(2(3)(1))(6(5(3(1)(2))(4)))", 0, len("4(2(3)(1))(6(5(3(1)(2))(4)))") - 1
        )
    )
    assert validate_bst(tree.root) is False
    # tree = create_binary_search_tree([1, 3, 4, 6, 8, 10, 11])
    # assert validate_bst(tree.root) is True
