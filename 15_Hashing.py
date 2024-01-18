class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def __str__(self):
        items = [f"{str(self.keys[i])}: {str(self.values[i])}" for i in range(self.size) if self.keys[i] is not None]
        return "{" + ", ".join(items) + "}"
        
    def hash_func(self, key):
        return hash(key) % self.size
        
    def insert(self, key, value):
        hash_value = self.hash_func(key)
        i = hash_value
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.values[i] = value
                return
            i = (i + 1) % self.size
            if i == hash_value:
                raise Exception("Hash table is full")
        self.keys[i] = key
        self.values[i] = value
        
    def search(self, key):
        hash_value = self.hash_func(key)
        i = hash_value
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.values[i]
            i = (i + 1) % self.size
            if i == hash_value:
                return None
        return None
        
    def delete(self, key):
        hash_value = self.hash_func(key)
        i = hash_value
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.keys[i] = None
                self.values[i] = None
                j = (i + 1) % self.size
                while self.keys[j] is not None:
                    next_hash = self.hash_func(self.keys[j])
                    if (j < next_hash <= i) or (i < j < next_hash) or (next_hash <= i < j):
                        self.keys[i] = self.keys[j]
                        self.values[i] = self.values[j]
                        self.keys[j] = None
                        self.values[j] = None
                        i = j
                    j = (j + 1) % self.size
                return
            i = (i + 1) % self.size
            if i == hash_value:
                return None



ht = HashTable(10)
ht.insert(1, "value1")
ht.insert(11, "value2")
ht.insert(21, "value3")
ht.insert(31, "value4")
ht.insert(41, "value5")
ht.insert(53, "value6")
ht.insert(65, "value6")

print(ht.search(11)) # Output: value2

ht.delete(11)
print(ht.search(11)) # Output: None