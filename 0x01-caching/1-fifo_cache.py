#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system with no limit """

    def __init__(self):
        """ overloaded init method """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first key and pop it
            first_key = next(iter(self.cache_data))

            # Remove the first item
            self.cache_data.pop(first_key)
            print("DISCARD:", first_key)

    def get(self, key):
        """ Get an item by key
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data
        return None.
        """
        return self.cache_data.get(key, None)
