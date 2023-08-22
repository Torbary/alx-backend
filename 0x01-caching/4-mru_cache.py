#!/usr/bin/env python3
"""
Defines the MRUCache class
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the MRUCache instance
        """
        super().__init__()
        self.used_order = []  # To track the order of item usage

    def update_usage_order(self, key):
        """
        Update the usage order of a key by moving it to the end
        (most recently used)
        """
        if key in self.used_order:
            self.used_order.remove(key)
        self.used_order.append(key)

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm.
        If key or item is None, nothing is done.
        If the number of items in self.cache_data exceeds BaseCaching.MAX_ITEMS
        the most recently used item (last item in used_order) is removed.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the most recently used key (last item) and remove it
            # from cache
            mru_key = self.used_order[-1]
            del self.cache_data[mru_key]
            self.used_order.pop()
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.update_usage_order(key)

    def get(self, key):
        """
        Get an item from the cache by key using MRU algorithm.
        If key is None or not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.update_usage_order(key)
        return self.cache_data[key]
