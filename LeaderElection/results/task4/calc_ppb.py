import math

import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate

from utils import parse_file

no_experiments = 1000
u = 1000
n_values = [2, int(u / 8), int(u / 4), int(u / 2), u]
round_length = math.ceil(math.log2(u))
ppb = dict()
for n in n_values:
    filename = f"scenario3_n={n}"
    title, data = parse_file(filename)
    success_in_one_round = 0
    for (k, v) in data.items():
        if k <= round_length:
            success_in_one_round += v

    ppb[n] = success_in_one_round / no_experiments

table = tabulate({'n': n_values,
                  'Pr[S_{L,n}]': [ppb[n] for n in n_values]},
                 headers='keys',
                 tablefmt='fancy_grid')

with open('ppb.txt', 'w') as f:
    f.write(table + '\n')
    f.write(f"λ = 0.579")

plt.rcParams.update({'font.size': 14})
plt.figure()
plt.xlabel('n')
plt.scatter(*zip(*ppb.items()), color='blue', label=r'$Pr[S_{L, n}]$')
x_axis = np.linspace(0, 1024, 512)
y_axis = [0.579 for x in x_axis]
plt.plot(x_axis, y_axis, color='green', label=r'$\lambda$')
plt.legend(loc='upper right')
plt.savefig('ppb.png')
