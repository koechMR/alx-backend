#!/usr/bin/python3
"""Cache implementation Class """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    basic cache implementaion class attributes and methods
    """
    def put(self, key, item):
        """item in the cache with the key"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
