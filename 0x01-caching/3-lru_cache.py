#!/usr/bin/env python3
"""
Defines the LRUCache class
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the LRUCache instance
        """
        super().__init__()
        self.used_order = []  # To track the order of item usage

    def update_usage_order(self, key):
        """
        Update the usage order of a key by
        moving it to the end (most recently used)
        """
        if key in self.used_order:
            self.used_order.remove(key)
        self.used_order.append(key)

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm.
        If key or item is None, nothing is done.
        If the number of items in self.cache_data exceeds
        BaseCaching.MAX_ITEMS,
        the least recently used item (first item in used_order) is removed.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the least recently used key (first item) and remove
            # it from cache
            lru_key = self.used_order[0]
            del self.cache_data[lru_key]
            self.used_order.pop(0)
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.update_usage_order(key)

    def get(self, key):
        """
        Get an item from the cache by key using LRU algorithm.
        If key is None or not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.update_usage_order(key)
        return self.cache_data[key]
