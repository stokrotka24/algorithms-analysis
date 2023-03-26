import hashlib
from _decimal import Decimal

from min_count import MinCount


class MinCountTruncHash(MinCount):
    def get_hash(self, elem: int) -> Decimal:
        h = hashlib.new(self.hash_func)
        h.update(elem.to_bytes(length=4, byteorder='little', signed=False))
        # hex_digest = h.hexdigest()[:(len(h.hexdigest()) // 2)]
        # digest_size = h.digest_size // 2
        # int_val = int(hex_digest, 16)
        # divisor = 2 ** (digest_size * 8)
        # int_val = int(h.hexdigest(), 16) % (2**64)
        # divisor = 2**64
        # hex_digest = 'a' + h.hexdigest()[1:]
        # int_val = int(hex_digest, 16)
        # divisor = 2 ** (h.digest_size * 8)
        hex_digest = h.hexdigest()[:4]
        int_val = int(hex_digest, 16)
        divisor = 2 ** 16
        return Decimal(int_val) / Decimal(divisor)
