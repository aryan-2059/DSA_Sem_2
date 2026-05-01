class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_fn(self, key): return key % self.size
    def insert(self, key, val):
        idx = self.hash_fn(key)
        self.table[idx].append((key, val))
    def get(self, key):
        idx = self.hash_fn(key)
        for k, v in self.table[idx]:
            if k == key: return v
        return None

ht = HashTable(5); ht.insert(10, "Ten"); print(ht.get(10))