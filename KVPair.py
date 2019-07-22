class KVPair:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def key(self):
        return self.__key

    def value(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value