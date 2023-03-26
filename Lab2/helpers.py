import math

import numpy as np


def generate_multiset(n: int) -> list[int]:
    start = sum(range(1, n))
    return [i + start for i in range(1, n + 1)]


def calc_ratio(li: list[float], delta=0.1) -> float:
    return len(list(filter(lambda x: abs(x - 1) < delta, li))) / len(li)


def binary_search_delta(li: list[float], start: float, end: float, ratio: float, precision=0.0001):
    if start < end:
        delta = (start + end) / 2
        ratio_delta = calc_ratio(li=li, delta=delta)
        # print(f"delta = {delta}, ratio_delta = {ratio_delta}")

        if ratio_delta <= ratio:
            return binary_search_delta(li, delta, end, ratio)

        if ratio_delta - ratio <= precision:
            return delta

        return binary_search_delta(li, start, delta, ratio)

    return None


def calc_chebyshev_delta(n, k, alpha):
    return np.sqrt((n - k + 1) / (n * alpha * (k - 2)))


def f_k(x: float, k: int):
    return math.exp(x * k) * pow((1 - x), k)


def calc_chernoff_bound(delta: float, k: int) -> float:
    eps1 = delta / (1 - delta)
    eps2 = delta / (1 + delta)
    return 1 - f_k(eps2, k) - f_k(-eps1, k)


def binary_search_chernoff_delta(li: list[float], start: float, end: float, bound: float, precision=0.0001):
    if start < end:
        delta = (start + end) / 2
        bound_delta = calc_chernoff_bound(delta=delta, k=400)
        # print(f"delta = {delta}, bound_delta = {bound_delta}")

        if bound_delta <= bound:
            return binary_search_chernoff_delta(li, delta, end, bound)

        if bound_delta - bound <= precision:
            return delta

        return binary_search_chernoff_delta(li, start, delta, bound)

    return None


# print(math.log2(generate_multiset(10000)[-1]))
