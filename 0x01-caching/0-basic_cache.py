#!/usr/bin/env python3
"""
Defines the BasicCache class
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, nothing is done.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.
        If key is None or not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
