
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
    
    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        index = self.compressor(self.hash(key))
        self.array[index] = value

    def retrieve(self, key):
        index = self.compressor(self.hash(key))
        return self.array[index]