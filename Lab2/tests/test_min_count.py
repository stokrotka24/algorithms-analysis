import unittest

from min_count import MinCount
from min_count_non_uniform_hash import MinCountNonUniformHash
from min_count_trunc_hash import MinCountTruncHash


class TestMinCount(unittest.TestCase):
    def test_get_hash(self):
        # hash_func = ['md5', 'sha256', 'sha3_224']
        no_iterations = 1000000
        hash_sum = 0
        m = MinCount(hash_func='md5', k=200, multiset=[1])
        for i in range(0, no_iterations):
            hash_sum += m.get_hash(elem=i)

        self.assertAlmostEqual(float(hash_sum) / no_iterations, 0.5, places=4)

    def test_get_hash_trunc_hash(self):
        no_iterations = 1000000
        hash_sum = 0
        m = MinCountTruncHash(hash_func='md5', k=200, multiset=[1])
        for i in range(0, no_iterations):
            hash_sum += m.get_hash(elem=i)

        print(float(hash_sum) / no_iterations)
        self.assertAlmostEqual(float(hash_sum) / no_iterations, 0.5, places=4)

    def test_get_hash_non_uniform_hash(self):
        no_iterations = 1000000
        hash_sum = 0
        m = MinCountNonUniformHash(hash_func='md5', k=200, multiset=[1])
        for i in range(0, no_iterations):
            hash_sum += m.get_hash(elem=i)

        print(float(hash_sum) / no_iterations)
        self.assertAlmostEqual(float(hash_sum) / no_iterations, 0.65, places=1)




if __name__ == '__main__':
    unittest.main()
