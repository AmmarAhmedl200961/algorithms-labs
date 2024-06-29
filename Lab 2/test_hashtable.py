import unittest
from hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10)

    def test_insert(self):
        self.hash_table.insert('key', 'value')
        self.assertEqual(self.hash_table.get('key'), 'value')

    def test_get(self):
        self.hash_table.insert('key', 'value')
        self.assertEqual(self.hash_table.get('key'), 'value')

    def test_remove(self):
        self.hash_table.insert('key', 'value')
        self.hash_table.remove('key')
        self.assertIsNone(self.hash_table.get('key'))

    def test_contains(self):
        self.hash_table.insert('key', 'value')
        self.assertTrue(self.hash_table.contains('key'))
        self.assertFalse(self.hash_table.contains('nonexistent_key'))

if __name__ == '__main__':
    unittest.main()
