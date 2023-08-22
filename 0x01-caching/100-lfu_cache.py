#!/usr/bin/env python3
"""
Defines the LFUCache class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the LFUCache instance
        """
        super().__init__()
        self.frequency = {}  # To track the frequency of item usage

    def put(self, key, item):
        """
        Add an item to the cache using LFU algorithm.
        If key or item is None, nothing is done.
        If the number of items in self.cache_data exceeds BaseCaching.MAX_ITEMS
        the least frequency used item (LFU algorithm) is removed.
        If there are multiple least frequency used items, the LRU algorithm
        is used
        to choose the least recently used item among them.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequency used keys
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                        k for k, v in self.frequency.items() if v == min_freq]

                # Choose the least recently used key among the least
                # frequency used keys
                lru_key = min(least_freq_keys, key=lambda k: self.frequency[k])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]

            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """
        Get an item from the cache by key using LFU algorithm.
        If key is None or not in the cache, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        return self.cache_data[key]
