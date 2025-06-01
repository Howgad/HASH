import unittest
from Hash_func import simple_hash

class TestHashFunction(unittest.TestCase):
    def test_empty_string(self):
        empty = b""
        result = simple_hash(empty)
        self.assertEqual(len(result), 32)
        self.assertIsInstance(result, bytes)

    def test_same_bytes(self):
        same_bytes = b"aaaa"
        result1 = simple_hash(same_bytes)
        result2 = simple_hash(same_bytes)
        self.assertEqual(result1, result2)
        self.assertEqual(len(result1), 32)

    def test_long_string(self):
        long_str = b"A" * 1000
        result = simple_hash(long_str)
        self.assertEqual(len(result), 32)

    def test_similar_strings(self):
        str1 = b"Hello, World!"
        str2 = b"Hello, world!"
        hash1 = simple_hash(str1)
        hash2 = simple_hash(str2)
        self.assertNotEqual(hash1, hash2)
        self.assertEqual(len(hash1), 32)
        self.assertEqual(len(hash2), 32)

    def test_binary_data(self):
        binary_data = bytes([x % 256 for x in range(50)])
        result = simple_hash(binary_data)
        self.assertEqual(len(result), 32)
        self.assertIsInstance(result, bytes)

if __name__ == '__main__':
    unittest.main(verbosity=2)