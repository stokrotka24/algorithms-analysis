import hashlib
from _decimal import Decimal

from min_count import MinCount


class MinCountNonUniformHash(MinCount):
    def get_hash(self, elem: int) -> Decimal:
        h = hashlib.new(self.hash_func)
        h.update(elem.to_bytes(length=4, byteorder='little', signed=False))
        hex_digest = 'a' + h.hexdigest()[1:]
        int_val = int(hex_digest, 16)
        divisor = 2 ** (h.digest_size * 8)
        return Decimal(int_val) / Decimal(divisor)