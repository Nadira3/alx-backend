#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system with an MRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.mru_order = []  # This will keep track of the MRU order of keys

    def put(self, key, item):
        """ Add an item in the cache following the MRU policy """
        if key is None or item is None:
            return

        # If key already exists, update the value and move key
        if key in self.cache_data:
            self.mru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            mru_key = self.mru_order.pop(-1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the item to the cache and update the MRU order
        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """ Get an item by key and update the MRU order """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the MRU order
        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]
