#!/usr/bin/python3
""" LIFO_Cache """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def __init__(self):
        """ first constructor """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assignning to the dictionary
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.order[-1]]
                    print("DISCARD:", self.order[-1])
                    self.order.pop(-1)
                self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        return value of key in self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
