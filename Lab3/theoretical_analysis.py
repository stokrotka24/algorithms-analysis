from numpy import exp
from scipy.special import binom, factorial


def q_m(q: float, p: float, m:int) -> float:
    return (q/p)**m

def pbb_adv_win_nakamoto(n: int, q: float) -> float:
    p: float = 1 - q
    l: float = n * q/p
    sum_pbb: float = 0
    for k in range(n):
        sum_pbb += exp(-l) * (l**k)/factorial(k) * (1 - q_m(q=q, p=p, m=n-k))
    return 1 - sum_pbb

def pbb_adv_win_grunspan(n: int, q:float) -> float:
    p: float = 1 - q
    sum_pbb: float = 0
    for k in range(n):
        sum_pbb += ((p**n) * (q**k) - (q**n) * (p**k)) * binom(k + n - 1, k)
    return 1 - sum_pbb

def find_n(pbb_adv_win: float, calc_pbb_method: str, q: float) -> int:
    calc_pbb = pbb_adv_win_nakamoto if calc_pbb_method == "nakamoto" else pbb_adv_win_grunspan
    n = 1
    while calc_pbb(n=n, q=q) >= pbb_adv_win:
        n += 1
    return n - 1
