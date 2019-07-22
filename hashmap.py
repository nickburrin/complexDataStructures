from KVPair import KVPair
## TODO: How would you delete a key-value pair from this hash map?
## TODO: Parts of the code are a little repetitive, how would you factor these roles differently?
## TODO: What should your hash map do if a key-value is added and the array is full? How does this hash map handle that?

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions
    
    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        index = self.compressor(self.hash(key))
        currentValue = self.array[index]
        if currentValue is None:
            self.array[index] = KVPair(key, value)
        else:
            if currentValue.key() == key:
                self.array[index].setValue(value)
            else:
                # Collision occurred
                number_collisions = 1
                while(currentValue.key() != key):
                    new_hash_code = self.hash(key, number_collisions)
                    new_array_index = self.compressor(new_hash_code)
                    currentValue = self.array[new_array_index]

                    if currentValue is None:
                        self.array[new_array_index] = KVPair(key, value)
                        return

                    if currentValue.key() == key:
                        self.array[new_array_index].setValue(value)
                        return

                    number_collisions += 1 


    def retrieve(self, key):
        index = self.compressor(self.hash(key))
        possible_item = self.array[index]
        if possible_item is None:
            return None
        else:
            if possible_item.key() == key:
                return possible_item.value()
            else:
                retrieval_collisions = 1
                while possible_item.key() != key:
                    new_hash_code = self.hash(key, retrieval_collisions)
                    retrieving_array_index = self.compressor(new_hash_code)
                    possible_item = self.array[retrieving_array_index]

                    if possible_item is None:
                        return None

                    if possible_item.key() == key:
                        return possible_item.value()

                    retrieval_collisions += 1 

