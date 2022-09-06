#!/usr/bin/python3
""" LFU_Cache """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache """

    def __init__(self):
        """ first constructor """
        super().__init__()
        self.lfu_order = []
        self.frequency = {}

    def put(self, key, item):
        """
        assignning to the dictionary
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.lfu_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_val = min(self.frequency.values())
                    min_kys = [k for k in self.frequency
                                if self.frequency[k] == min_val]
                    for i in range(len(self.lfu_order)):
                        if self.lfu_order[i] in min_kys:
                            break
                    del self.cache_data[self.lfu_order[i]]
                    del self.frequency[self.lfu_order[i]]
                    print("DISCARD:", self.lfu_order[i])
                    self.lfu_order.pop(i)
                self.cache_data[key] = item
                self.frequency[key] = 1
            self.lfu_order.append(key)

    def get(self, key):
        """
        return value of key in self.cache_data
        """
        if key in self.cache_data:
            self.lfu_order.remove(key)
            self.lfu_order.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
