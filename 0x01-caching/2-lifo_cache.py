#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with an LIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_item = None

    def put(self, key, item):
        """ Add an item in the cache following the LIFO policy """
        if key is None or item is None:
            return

        if key not in self.cache_data.keys() and len(self.cache_data)\
                >= BaseCaching.MAX_ITEMS:
            # Remove the first item in the LIFO order
            del self.cache_data[self.last_item]

            # Add to the end of the LIFO order list
            print(f"DISCARD: {self.last_item}")

        # Add the item to the cache
        self.cache_data[key] = item
        self.last_item = key

    def get(self, key):
        """ Get an item by key and update the LIFO order """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
