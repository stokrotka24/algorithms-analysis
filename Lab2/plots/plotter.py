from matplotlib import pyplot as plt
from helpers import binary_search_delta, calc_chebyshev_delta, binary_search_chernoff_delta
from main import n_range, hash_functions, hash_names, b_values


def task5a():
    with open('../results/task5a.txt') as f:
        lines = f.readlines()[1:]

    x = []
    results_s_n = []
    results_t_n = []
    for line in lines:
        print(line.split())
        data = line.split()
        x.append(int(data[0]))
        results_s_n.append(float(data[1]))
        results_t_n.append(float(data[2]))

    plt.figure()
    plt.rcParams.update({'font.size': 14})
    plt.title(r"$\frac{\hat{n}}{n}$ for $S_n$ and $T_n$, k = 10")
    plt.xlabel(r'$n$')
    plt.ylabel(r'$\frac{\hat{n}}{n}$')
    plt.scatter(x, results_t_n, label=r'$T_n$', s=0.5)
    plt.scatter(x, results_s_n, label=r'$S_n$', s=0.5)
    plt.grid()
    plt.legend(loc='upper left')
    plt.savefig('task5a.png')


def task5b():
    k_values = [2, 3, 10, 100, 400]
    for k in k_values:
        with open(f'../results/task5b_{k}.txt') as f:
            results = f.readlines()

        results = list(map(lambda x: float(x.strip()), results))
        plt.figure()
        plt.rcParams.update({'font.size': 12})
        title = r"$\frac{\hat{n}}{n}$ for $k=$" + str(k)
        plt.title(title)
        plt.xlabel(r'$n$')
        plt.ylabel(r'$\frac{\hat{n}}{n}$')
        plt.scatter(n_range, results, s=0.5)
        plt.grid()
        plt.savefig(f'task5b_{k}.png')


def task6():
    for hash_func in hash_functions:
        with open(f'../results/task6_{hash_func}.txt') as f:
            results = f.readlines()

        results = list(map(lambda x: float(x.strip()), results))
        plt.figure()
        plt.rcParams.update({'font.size': 12})
        title = r"$\frac{\hat{n}}{n},\;k=400,\;h=$" + hash_func
        plt.title(title)
        plt.xlabel(r'$n$')
        plt.ylabel(r'$\frac{\hat{n}}{n}$')
        plt.scatter(n_range, results, s=0.5)
        plt.grid()
        plt.savefig(f'task6_{hash_func}.png')

        with open(f'../results/task6_{hash_func}_trunc.txt') as f:
            results = f.readlines()

        results = list(map(lambda x: float(x.strip()), results))
        plt.figure()
        plt.rcParams.update({'font.size': 12})
        title = r"$\frac{\hat{n}}{n},\;k=400,\;h=$" + hash_func + " (last 16 bits)"
        plt.title(title)
        plt.xlabel(r'$n$')
        plt.ylabel(r'$\frac{\hat{n}}{n}$')
        plt.scatter(n_range, results, s=0.5)
        plt.grid()
        plt.savefig(f'task6_{hash_func}_trunc.png')

        with open(f'../results/task6_{hash_func}_non_uniform.txt') as f:
            results = f.readlines()

        results = list(map(lambda x: float(x.strip()), results))
        plt.figure()
        plt.rcParams.update({'font.size': 12})
        title = r"$\frac{\hat{n}}{n},\;k=400,\;h=$" + hash_func + " (1010 as first 4 bits)"
        plt.title(title)
        plt.xlabel(r'$n$')
        plt.ylabel(r'$\frac{\hat{n}}{n}$')
        plt.scatter(n_range, results, s=0.5)
        plt.grid()
        plt.savefig(f'task6_{hash_func}_non_uniform.png')


def task7():
    with open("../results/task5b_400.txt", "r") as f:
        li = f.readlines()

    li = list(map(lambda x: float(x.strip()), li))
    alpha_values = [0.05, 0.01, 0.005]
    for alpha in alpha_values:
        delta = binary_search_delta(li=li, start=0.0, end=0.2, ratio=1 - alpha)
        delta_chebyshev = calc_chebyshev_delta(n=10000, k=400, alpha=alpha)
        delta_chernoff = binary_search_chernoff_delta(li=li, start=0.0, end=1.0, bound=1 - alpha)

        plt.figure()
        plt.rcParams.update({'font.size': 10})
        title = r"$\frac{\hat{n}}{n},\;k=400,\;\alpha=$" + str(alpha * 100) + "%"
        plt.title(title)
        plt.xlabel(r'$n$')
        plt.ylabel(r'$\frac{\hat{n}}{n}$')
        plt.scatter(n_range, li, s=0.5)
        plt.plot(n_range, [1 - delta] * 10000, label=r'experimental', color='green')
        plt.plot(n_range, [1 + delta] * 10000, color='green')
        plt.plot(n_range, [1 - delta_chernoff] * 10000, label=r'Chernoff', color='orange')
        plt.plot(n_range, [1 + delta_chernoff] * 10000, color='orange')
        plt.plot(n_range, [1 - delta_chebyshev] * 10000, label=r'Chebyshev', color='red')
        plt.plot(n_range, [1 + delta_chebyshev] * 10000, color='red')
        plt.grid()
        plt.legend(loc='lower right')
        plt.savefig(f'task7_alpha{alpha}.png')


def task8():
    # for hash_name in hash_names:
    #     for b in b_values:
    #         with open(f'../results/task8_{hash_name}_{b}.txt') as f:
    #             results = f.readlines()
    #
    #         results = list(map(lambda x: float(x.strip()), results))
    #         plt.figure()
    #         plt.rcParams.update({'font.size': 12})
    #         title = r"$\frac{\hat{n}}{n}$ for hash=" + str(hash_name) + f" b={b}"
    #         plt.title(title)
    #         plt.xlabel(r'$n$')
    #         plt.ylabel(r'$\frac{\hat{n}}{n}$')
    #         plt.scatter(n_range, results, s=0.5)
    #         plt.grid()
    #         plt.savefig(f'task8_{hash_name}_{b}.png')
    #         plt.close()

    k_values = []
    for b in b_values:
        k_values.append(round(5 / 32 * 2 ** b))

    for k in k_values:
        with open(f'../results/task8_min_count_k{k}.txt') as f:
            results = f.readlines()

        results = list(map(lambda x: float(x.strip()), results))
        plt.figure()
        plt.rcParams.update({'font.size': 12})
        title = r"$\frac{\hat{n}}{n}$ for $k=$" + str(k)
        plt.title(title)
        plt.xlabel(r'$n$')
        plt.ylabel(r'$\frac{\hat{n}}{n}$')
        plt.scatter(n_range, results, s=0.5)
        plt.grid()
        plt.savefig(f'task8_min_count_k{k}.png')
        plt.close()


if __name__ == "__main__":
    # task5a()
    # task5b()
    # task6()
    # task7()
    task8()
