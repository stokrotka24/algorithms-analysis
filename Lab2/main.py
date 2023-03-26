import math
from collections import defaultdict

from helpers import generate_multiset, calc_ratio
from min_count import MinCount
from min_count_non_uniform_hash import MinCountNonUniformHash
from min_count_trunc_hash import MinCountTruncHash

n_range = range(1, 10001)
hash_functions = ['md5', 'sha256', 'sha512', 'sha3_256', 'sha3_512']


def task5a():
    results_s_n = dict()
    results_t_n = dict()

    for n in n_range:
        s_n = generate_multiset(n)
        m = MinCount(hash_func='sha3_256', k=10, multiset=s_n)
        results_s_n[n] = m.run() / n

        t_n = s_n + s_n
        m = MinCount(hash_func='sha3_256', k=10, multiset=t_n)
        results_t_n[n] = m.run() / n

    with open("results/task5a.txt", "w") as f:
        f.write(f"n S_n T_n\n")
        for n in n_range:
            f.write(f"{n} {results_s_n[n]} {results_t_n[n]}\n")


def task5b():
    k_values = [2, 3, 10, 100, 400]
    results = defaultdict(dict)
    for n in n_range:
        if n % 100 == 0:
            print(n)
        s_n = generate_multiset(n)
        for k in k_values:
            m = MinCount(hash_func='md5', k=k, multiset=s_n)
            results[k][n] = m.run() / n

    for k in k_values:
        with open(f"results/task5b_{k}.txt", "w") as f:
            for n in n_range:
                f.write(f"{results[k][n]}\n")


def min_count_md5(k):
    print(f"k = {k}")
    results = []

    for n in n_range:
        if n % 100 == 0:
            print(f"\tn = {n}")
        s_n = generate_multiset(n)
        m = MinCount(hash_func='md5', k=k, multiset=s_n)
        results.append(m.run() / n)
    return results


def binary_search_k(start: int, end: int, ratio: float) -> int | None:
    if start < end:
        k = math.floor((start + end) / 2)
        ratio_k = calc_ratio(min_count_md5(k))
        print(f"k = {k}, ratio_k = {ratio_k}")
        if ratio_k < ratio:
            return binary_search_k(k + 1, end, ratio)
        elif ratio_k > ratio:
            return binary_search_k(start, k - 1, ratio)
        return k
    return None


def task5c():
    with open("results/task5b_100.txt") as f_100:
        results_100 = f_100.readlines()
    results_100 = list(map(lambda x: float(x.strip()), results_100))
    ratio_100 = calc_ratio(results_100)

    with open("results/task5b_400.txt") as f_400:
        results_400 = f_400.readlines()
    results_400 = list(map(lambda x: float(x.strip()), results_400))
    ratio_400 = calc_ratio(results_400)

    assert (ratio_100 <= 0.95 <= ratio_400)
    print(binary_search_k(start=100, end=400, ratio=0.95))


def task6():
    results = defaultdict(dict)
    results_trunc_hash = defaultdict(dict)
    results_non_uniform_hash = defaultdict(dict)

    for n in n_range:
        if n % 100 == 0:
            print(f"n = {n}")
        s_n = generate_multiset(n)

        for hash_func in hash_functions:
            m = MinCount(hash_func=hash_func, k=400, multiset=s_n)
            results[hash_func][n] = m.run() / n

            m = MinCountTruncHash(hash_func=hash_func, k=400, multiset=s_n)
            results_trunc_hash[hash_func][n] = m.run() / n

            m = MinCountNonUniformHash(hash_func=hash_func, k=400, multiset=s_n)
            results_non_uniform_hash[hash_func][n] = m.run() / n

    for hash_func in hash_functions:
        with open(f"results/task6_{hash_func}.txt", "w") as f:
            for n in n_range:
                f.write(f"{results[hash_func][n]}\n")

        with open(f"results/task6_{hash_func}_trunc.txt", "w") as f:
            for n in n_range:
                f.write(f"{results_trunc_hash[hash_func][n]}\n")

        with open(f"results/task6_{hash_func}_non_uniform.txt", "w") as f:
            for n in n_range:
                f.write(f"{results_non_uniform_hash[hash_func][n]}\n")


if __name__ == "__main__":
    task5a()
    task5b()
    task5c()
    task6()
