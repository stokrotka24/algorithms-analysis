import matplotlib.pyplot as plt

from utils import parse_file


def make_histogram(filename: str):
    title, data = parse_file(filename)
    plt.figure()
    plt.title(title)
    plt.xlabel('slot')
    plt.ylabel('no. occurrences')
    plt.bar(data.keys(), data.values())
    plt.savefig(filename)


make_histogram("scenario2")
make_histogram("scenario3_n=2")
make_histogram("scenario3_n=half_u")
make_histogram("scenario3_n=u")
