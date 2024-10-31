#!/usr/bin/python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with an LFU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.lfu_order = []  # This will keep track of the LFU order of keys

    def put(self, key, item):
        """ Add an item in the cache following the LFU policy """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the last item
            print(self.lfu_order)
            lfu_key = self.lfu_order.pop(0)
            del self.cache_data[lfu_key]
            print(f"DISCARD: {lfu_key}")

        # Insert the item at the front of the LFU order list
        if key not in self.cache_data:
            self.lfu_order.insert(0, key)

        # Add the item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key and update the LFU order """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
