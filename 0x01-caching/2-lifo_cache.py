#!/usr/bin/env python3
"""
Defines the LIFOCache class
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm.
        If key or item is None, nothing is done.
        If the number of items in self.cache_data
        exceeds BaseCaching.MAX_ITEMS,
        the last item added (newest) is removed.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last key added (newest) and remove it from cache
            newest_key = list(self.cache_data.keys())[-1]
            del self.cache_data[newest_key]
            print("DISCARD:", newest_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.
        If key is None or not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
