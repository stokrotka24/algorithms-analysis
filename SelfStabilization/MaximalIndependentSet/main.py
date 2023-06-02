from Graph import Graph

def read_data(filename: str) -> Graph:
    with open(filename, "r") as f:
        lines = f.readlines()
    size = int(lines[0])
    g = Graph(size)

    for line in lines[1:]:
        a, b = list(map(lambda x: int(x), line.split()))
        g.add_edge(a, b)

    g.print()
    return g

if __name__ == "__main__":
    graph: Graph =read_data("example_data/data.txt")
    print("Maximal independent set:", graph.simulation())

    graph: Graph = read_data("example_data/data2.txt")
    print("Maximal independent set:", graph.simulation())