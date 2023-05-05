import math

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

from utils import parse_file


def expected_value(n):
    return (1 - 1 / n) ** (1 - n)


def variance(n):
    p = (1 - 1 / n) ** (n - 1)
    return (1 - p) / (p ** 2)


directory = "."
n_values = [5, 50, 100, 500, 1000]
experimental_expected_value = dict()
experimental_variance = dict()
for n in n_values:
    filename = f"scenario2_n={n}"
    _, data = parse_file(filename)
    results = np.array(list(data.keys()))
    frequency = np.array(list(data.values()))
    experimental_expected_value[n] = np.average(results, weights=frequency)
    experimental_variance[n] = np.average((results - experimental_expected_value[n]) ** 2, weights=frequency)

table = tabulate({'n': n_values,
                  'E[L_n]': [experimental_expected_value[n] for n in n_values],
                  '(1 - 1 / n) ** (1 - n)': [expected_value(n) for n in n_values]},
                 headers='keys',
                 tablefmt='fancy_grid')

with open('expected_value.txt', 'w') as f:
    f.write(table + '\n')
    f.write(f"e = {math.e}")

table = tabulate({'n': n_values,
                  'Var[L_n]': [experimental_variance[n] for n in n_values],
                  '(1 - p)/p ** 2 for p = (1 - 1 / n) ** (n - 1)': [variance(n) for n in n_values]},
                 headers='keys',
                 tablefmt='fancy_grid')

with open('variance.txt', 'w') as f:
    f.write(table + '\n')
    f.write(f"e*(e - 1) = {math.e * (math.e - 1)}")


plt.rcParams.update({'font.size': 14})
plt.figure()
plt.xlabel('n')
plt.scatter(*zip(*experimental_expected_value.items()), color='blue', label=r'$E[L_{n}]$')
x_axis = np.linspace(1, 1000, 500)
y_axis = [expected_value(x) for x in x_axis]
plt.plot(x_axis, y_axis, color='red', label=r'$(1-\frac{1}{n})^{1-n}$')
# plt.plot(x_axis, [math.e] * len(x_axis), color='green', label=r'$e^{x}$')
plt.legend(loc='lower right')
plt.savefig('expected_value.png')

