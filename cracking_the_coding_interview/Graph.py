from typing import Dict


class Node(object):
    def __init__(self, label=""):
        self.neighbours = []
        # reverse neighbours are nodes that have edge going from them to this node
        self.reverse_neighbours = []
        self.visited_source = False
        self.visited_target = False
        self.path = [self]
        self.label = label

    def __str__(self):
        return self.label

    def __repr__(self):
        return str(self)


class Graph(object):
    def __init__(self, graph_string: str):
        self.nodes: Dict[int, Node] = {}
        for line in graph_string.splitlines():
            f = int(line.split("->")[0])
            s = int(line.split("->")[1])
            f_node = self.nodes.setdefault(f, Node(str(f)))
            s_node = self.nodes.setdefault(s, Node(str(s)))
            f_node.neighbours.append(s_node)
            s_node.reverse_neighbours.append(f_node)

    def get_node(self, i):
        return self.nodes[i]
