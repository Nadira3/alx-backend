#!/usr/bin/python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with an LFU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.lfu_order = {}
        self.lru_order = []  # This will keep track of the LRU order of keys

    def put(self, key, item):
        """ Add an item in the cache following the LFU policy """
        if key is None or item is None:
            return

        if key not in self.lru_order and len(self.cache_data)\
                >= BaseCaching.MAX_ITEMS:
            # Get the maximum frequency
            min_freq = min(self.lfu_order.values())

            # Get keys with max frequency
            min_used_keys = [key for key, value
                             in self.lfu_order.items() if value == min_freq]
            if len(min_used_keys) > 1:
                # Remove the least recently used item
                lru_key = self.get_lru(min_used_keys)
                del self.cache_data[lru_key]
                del (self.lfu_order[min_used_keys[0]])
                print(f"DISCARD: {lru_key}")
            else:
                del (self.cache_data[min_used_keys[0]])
                del (self.lfu_order[min_used_keys[0]])
                print("DISCARD:", min_used_keys[0])

        # Add the item to the cache
        self.cache_data[key] = item
        self.lru_add(key)
        self.lfu_add(key)

    def get(self, key):
        """ Get an item by key and update the LFU order """
        if key is None or key not in self.cache_data:
            return None

        self.lfu_add(key)
        self.lru_add(key)

        return self.cache_data[key]

    def lfu_add(self, key):
        """ add to lfu list """
        if key in self.lfu_order.keys():
            self.lfu_order[key] += 1
        else:
            self.lfu_order[key] = 0

    def lru_add(self, key):
        """ add to lru list """
        # If key already exists, update the order
        if key in self.lru_order:
            self.lru_order.remove(key)
            self.lru_order.append(key)
        else:
            self.lru_order.append(key)

    def get_lru(self, min_used_keys):
        """ get the least recently used key """
        for key in self.lru_order:
            if key in min_used_keys:
                return key
