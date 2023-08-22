#!/usr/bin/env python3
"""
Defines the FIFOCache class
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using FIFO algorithm.
        If key or item is None, nothing is done.
        If the number of items in self.cache_data exceeds
        BaseCaching.MAX_ITEMS,
        the oldest item (first item added) is removed.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the first key added (oldest) and remove it from cache
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.
        If key is None or not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
