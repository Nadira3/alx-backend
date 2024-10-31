#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with an LIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.lifo_order = []  # This will keep track of the LIFO order of keys

    def put(self, key, item):
        """ Add an item in the cache following the LIFO policy """
        if key is None or item is None:
            return

        if key not in self.cache_data.keys() and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the first item in the LIFO order
            lifo_key = self.lifo_order.pop(0)
            del self.cache_data[lifo_key]

            # Add to the end of the LIFO order list
            self.lifo_order.append(key)
            print(f"DISCARD: {lifo_key}")

        # Insert the item at the front of the LIFO order list
        if key not in self.lifo_order:
            self.lifo_order.insert(0, key)

        # Add the item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key and update the LIFO order """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
