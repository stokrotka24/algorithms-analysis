import hashlib
from _decimal import Decimal
from decimal import Decimal


class MinCount:
    def __init__(self, hash_func, k, multiset: list[int]):
        self.hash_table = [Decimal(1)] * k
        self.hash_func = hash_func
        self.multiset = multiset
        self.k = k

    def get_hash(self, elem: int) -> Decimal:
        h = hashlib.new(self.hash_func)
        h.update(elem.to_bytes(length=4, byteorder='little', signed=False))
        int_val = int(h.hexdigest(), 16)
        divisor = 2 ** (h.digest_size * 8)
        return Decimal(int_val) / Decimal(divisor)

    def run(self) -> float:
        for elem in self.multiset:
            hash_val = self.get_hash(elem)

            if hash_val < self.hash_table[- 1] and hash_val not in self.hash_table:
                self.hash_table[- 1] = hash_val
                self.hash_table.sort()

        if self.hash_table[- 1] == Decimal(1):
            return self.k - self.hash_table.count(Decimal(1))

        return (self.k - 1) / self.hash_table[-1]
