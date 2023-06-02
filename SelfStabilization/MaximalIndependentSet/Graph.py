from Vertex import Vertex


class Graph:
    def __init__(self, size: int):
        self.vertices: list[Vertex] = [Vertex(i) for i in range(1, size+1)]

    def add_edge(self, a:int, b:int):
        self.vertices[a-1].add_neighbour(self.vertices[b-1])
        self.vertices[b-1].add_neighbour(self.vertices[a-1])

    def _in_safe_configuration(self) -> bool:
        return all(list(map(lambda v: v.is_independent or v.is_dominated, self.vertices)))

    def simulation(self) -> list[Vertex]:
        while not self._in_safe_configuration():
            for v in self.vertices:
                v.simulate_round()

        return list(map(lambda x: x.index, filter(lambda u: u.is_independent == True, self.vertices)))

    def print(self):
        print("=======================")
        print("Graph:")
        for v in self.vertices:
            v.print()
        print("=======================")

