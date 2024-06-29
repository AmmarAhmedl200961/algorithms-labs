
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next
            
            
    def contains(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

# Test driver
if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable(10)

    # Insert key-value pairs
    hash_table.insert("apple", 5)
    hash_table.insert("banana", 10)
    hash_table.insert("cherry", 15)

    # Get values by keys
    print(hash_table.get("apple"))  # Output: 5
    print(hash_table.get("banana"))  # Output: 10
    print(hash_table.get("cherry"))  # Output: 15

    # Remove a key-value pair
    hash_table.remove("banana")

    # Verify removal
    print(hash_table.get("banana"))  # Output: None
    
    print(hash_table.contains("banana"))  # Output: False
