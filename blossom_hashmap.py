from LinkedList import LinkedList
from Node import Node

class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [LinkedList() for item in range(size)]
    
    def hash(self, key):
        encode = key.encode()
        return sum(encode)
    
    def compress(self, hashCode):
        return hashCode % self.size
        
    def assign(self, key, value):
        index = self.compress(self.hash(key))
        payload = Node([key, value])
        listAtIndex = self.array[index]
        for item in listAtIndex:
            if item[0] == key:
                item[1] = value

        listAtIndex.insert(payload)
        
    def retrieve(self, key):
        index = self.compress(self.hash(key))
        listAtIndex = self.array[index]
        for item in listAtIndex:
            if item[0] == key:
                return item[1]
        
        return None