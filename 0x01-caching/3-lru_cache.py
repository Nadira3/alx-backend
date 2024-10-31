#!/usr/bin/python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a caching system with an LRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.lru_order = []  # This will keep track of the LRU order of keys

    def put(self, key, item):
        """ Add an item in the cache following the LRU policy """
        if key is None or item is None:
            return

        # If key already exists, update the value
        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the item to the cache and update the LRU order
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key and update the LRU order """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the LRU order
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
