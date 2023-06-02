class Vertex:
    def __init__(self, index: int) -> None:
        self.index = index
        self.neighbours: list = list()
        self.is_in_set = False

    def add_neighbour(self, neighbour) -> None:
        self.neighbours.append(neighbour)

    def _has_neighbours_in_set(self) -> bool:
        return any(list(map(lambda u: u.is_in_set, self.neighbours)))

    @property
    def is_independent(self):
        return self.is_in_set and not self._has_neighbours_in_set()

    @property
    def is_dominated(self):
        return not self.is_in_set and self._has_neighbours_in_set()

    def simulate_round(self) -> None:
        # make vertex independent
        if not self.is_in_set and not self._has_neighbours_in_set():
            self.is_in_set = True

        # make vertex dominated
        if self.is_in_set and self._has_neighbours_in_set():
            self.is_in_set = False

    def print(self) -> None:
        print(self.index, ":", list(map(lambda u: u.index, self.neighbours)))
