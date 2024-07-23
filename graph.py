class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))


g = Graph()

g.add_node(0, 1)
g.add_node(0, 4)
g.add_node(1, 2)
g.add_node(1, 3)
g.add_node(1, 4)
g.add_node(2, 3)
g.add_node(3, 4)

g.print_graph()
