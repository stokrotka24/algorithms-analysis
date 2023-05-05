import math
import zlib

import mmh3
from cityhash import CityHash32
from farmhash import FarmHash32


def get_alpha(m: int) -> float | None:
    if m == 16:
        return 0.673
    elif m == 32:
        return 0.697
    elif m == 64:
        return 0.709
    elif m >= 128:
        return 0.7213 / (1 + 1.079 / m)
    return None


def fst_one_position(w: str) -> int:
    try:
        return w.index('1') + 1
    except ValueError:
        return len(w) + 1


class HyperLogLog:
    def __init__(self, hash_name: str, b: int, multiset: list[int]):
        self.hash_name = hash_name
        self.b = b
        self.m = 2**b
        self.multiset = multiset
        self.registers = [0] * self.m

    def get_hash(self, elem: int) -> int:
        elem_to_bytes = elem.to_bytes(length=4, byteorder='big', signed=False)
        match self.hash_name:
            case "mmh":
                return mmh3.hash(elem_to_bytes, signed=False)
            case "city":
                return CityHash32(elem_to_bytes)
            case "farm":
                return FarmHash32(elem_to_bytes)
            case "crc32":
                return zlib.crc32(elem_to_bytes)

    def run(self) -> float:
        for elem in self.multiset:
            x = self.get_hash(elem)
            x = '{:032b}'.format(x)
            j = int(x[:self.b], 2)
            w = x[self.b:]
            self.registers[j] = max(self.registers[j], fst_one_position(w))

        E = get_alpha(self.m) * (self.m ** 2) * (1 / sum(map(lambda val: 2 ** (-val), self.registers)))

        if E <= 5 / 2 * self.m:
            V = self.registers.count(0)
            if V != 0:
                return self.m * math.log(self.m / V)

        if E > (2 ** 32) / 30:
            H = 2 ** 32
            return -H * math.log(1 - E / H)

        return E

# x = 12345
# x_bytes = x.to_bytes(length=4, byteorder='big', signed=False)
#
# a = mmh3.hash(x_bytes, signed=False)
# b = CityHash32(x_bytes)
# c = FarmHash32(x_bytes)
# d = zlib.crc32(x_bytes)
# print(a)
# # a_bytes = a.to_bytes(length=4, byteorder='big', signed=False)
# print(len('{:032b}'.format(a)))
# print(b)
# b_bytes = b.to_bytes(length=4, byteorder='big', signed=False)
# print(len('{:032b}'.format(b)))
# print(c)
# c_bytes = c.to_bytes(length=4, byteorder='big', signed=False)
# print(len('{:032b}'.format(c)))
# print(d)
# c_bytes = c.to_bytes(length=4, byteorder='big', signed=False)
# print(len('{:032b}'.format(d)))
# x = 7
# a = mmh3.hash(x.to_bytes(length=4, byteorder='big', signed=False), signed=False)
# print(a)
# # a += 1
# # a=2
# # print(a.to_bytes(length=4, byteorder='big', signed=False))
# # print(mmh3.hash_bytes("foo"))
# b = FarmHash32("abc").to_bytes(length=4, byteorder='big', signed=False)
# print(FarmHash32("abc"))
# # print(b)
# b = CityHash32("abc").to_bytes(length=4, byteorder='big', signed=False)
# print(CityHash32("atttfffddddddddddddddvbbbbdddddddbc"))
# # print(b)
# x = 7
# z = '{:032b}'.format(2 ** 30 + 2 ** 29)
# print(z)
# print(z[:2])
# print(z[2:])
# print(type(z))
# print(len(z))
# n = 999
# hyp = HyperLogLog(hash_name="mmh", m=128, multiset=generate_multiset(n))
# print(hyp.run())
# hyp = HyperLogLog(hash_name="city", m=128, multiset=generate_multiset(n))
# print(hyp.run())
# hyp = HyperLogLog(hash_name="farm", m=128, multiset=generate_multiset(n))
# print(hyp.run())
