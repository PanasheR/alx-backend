#!/usr/bin/python3
""" LRU_Cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache """

    def __init__(self):
        """ first constructor """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        assignning to the dictionary
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lru_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.lru_order[0]]
                    print("DISCARD:", self.lru_order[0])
                    self.lru_order.pop(0)
                self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """
        return value of key in self.cache_data
        """
        if key in self.cache_data:
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
