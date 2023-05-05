from random import uniform


def pbb_adv_win(n: int, q: float, no_attacks: int=10000) -> float:
    print(f"\tq={q}")
    successful_attacks = 0
    for i in range(no_attacks):
        successful_attacks += double_spending_attack(n=n, q=q)
    return successful_attacks/no_attacks


def double_spending_attack(n: int, q: float, max_blocks: int=5000) -> int:
    adversary_blocks: int = 0
    fair_users_blocks: int = 0
    blocks_after_n: int = 0

    while True:
        if uniform(0, 1) <= q:
           adversary_blocks += 1
        else:
           fair_users_blocks += 1

        if fair_users_blocks >= n:
            blocks_after_n += 1

            if adversary_blocks >= fair_users_blocks:
                return 1
            if blocks_after_n >= max_blocks:
                return 0