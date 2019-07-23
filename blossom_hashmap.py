from LinkedList import LinkedList
from Node import Node

class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [None for item in range(size)]
    
    def hash(self, key):
        encode = key.encode()
        return sum(encode)
    
    def compress(self, hashCode):
        return hashCode % self.size
        
    def assign(self, key, value):
        index = self.compress(self.hash(key))
        self.array[index] = [key, value]
        
    def retrieve(self, key):
        index = self.compress(self.hash(key))
        payload = self.array[index]
        if payload is None:
            return None
        elif payload[0] != key:
            return None
        else:
            return payload[1]
    