#!/usr/bin/python3
""" Basic_Cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache """
    def put(self, key, item):
        """
        assigning to dictionionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return value of key in self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
