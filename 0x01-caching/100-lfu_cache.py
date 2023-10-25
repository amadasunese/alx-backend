#!/usr/bin/python3
"""LFU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    A class that inherits from BaseCaching and implements LFU caching.
    """

    def __init__(self):
        super().__init__()
        self.least_recently_used_cache = OrderedDict()
        self.least_frequently_used_cache = {}

    def put(self, key, item):
        """
        Add a key-value pair to the cache
        """
        if key in self.least_recently_used_cache:
            del self.least_recently_used_cache[key]

        if len(self.least_recently_used_cache) > self.MAX_ITEMS - 1:
            min_value = min(self.least_frequently_used_cache.values())
            lfu_keys = [k for k, v in self.least_frequently_used_cache.items()
                        if v == min_value]

            if len(lfu_keys) == 1:
                discarded_key = lfu_keys[0]
            else:
                for k in self.least_recently_used_cache:
                    if k in lfu_keys:
                        discarded_key = k
                        break

            print("DISCARD:", discarded_key)
            self.least_recently_used_cache.pop(discarded_key)
            del self.least_frequently_used_cache[discarded_key]

        self.least_recently_used_cache[key] = item
        self.least_recently_used_cache.move_to_end(key)

        if key in self.least_frequently_used_cache:
            self.least_frequently_used_cache[key] += 1
        else:
            self.least_frequently_used_cache[key] = 1

        self.cache_data = dict(self.least_recently_used_cache)

    def get(self, key):
        """
        Retrieve the value for a given key.
        """
        if key in self.least_recently_used_cache:
            value = self.least_recently_used_cache[key]
            self.least_recently_used_cache.move_to_end(key)

            if key in self.least_frequently_used_cache:
                self.least_frequently_used_cache[key] += 1
            else:
                self.least_frequently_used_cache[key] = 1

            return value
