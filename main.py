# Adjacency List Graph


class LGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        self.adj_list[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=1):
        self.adj_list[vertex1][vertex2] = weight

    def bfs(self):
        queue = [list(self.adj_list.keys())[0]]
        visited = set()
        while len(queue) != 0:
            vertex = queue.pop(0)
            visited.add(vertex)
            yield vertex
            for av in self.adj_list[vertex]:
                if av not in visited:
                    queue.append(av)

    def dfs(self):
        stack = [list(self.adj_list.keys())[0]]
        visited = set()
        while len(stack) != 0:
            vertex = stack.pop()
            visited.add(vertex)
            yield vertex
            for av in self.adj_list[vertex]:
                if av not in visited:
                    stack.append(av)


g1 = LGraph()
g1.add_vertex("a")
g1.add_vertex("b")
g1.add_vertex("c")
g1.add_vertex("d")
g1.add_vertex("e")
g1.add_vertex("f")
g1.add_vertex("g")

g1.add_edge("a", "b")
g1.add_edge("b", "a")
g1.add_edge("a", "c")

g1.add_edge("b", "d")
g1.add_edge("b", "e")

g1.add_edge("c", "f")
g1.add_edge("c", "g")


# for v in g1.bfs():
#     print(v)
