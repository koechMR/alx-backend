#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Lifo cache system class """
    def __init__(self):
        """Init the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item"""
        if key is None or item is None:
            return
        if key not in self.cache_data:

            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)

        self.cache_data[key] = item

        self.cache_data.move_to_end(key, last=True)

    def get(self, key):

        """Get an item by key"""

        return self.cache_data.get(key, None)
