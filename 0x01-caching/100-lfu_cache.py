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
        Add a key-value pair to the cache.
        """
        if key is None or item is None:
            return

        self._remove_if_needed()
        self._add_to_cache(key, item)

    def get(self, key):
        """
        Retrieve the value for a given key.
        """
        if key in self.least_recently_used_cache:
            self.least_recently_used_cache.move_to_end(key)
            self._increment_lfu_count(key)
            return self.least_recently_used_cache[key]

    def _remove_if_needed(self):
        if len(self.least_recently_used_cache) > self.MAX_ITEMS - 1:
            min_lfu_count = min(self.least_frequently_used_cache.values())
            lfu_keys = [k for k, v in self.least_frequently_used_cache.items()
                        if v == min_lfu_count]

            discarded_key = next((k for k in self.least_recently_used_cache
                                  if k in lfu_keys), lfu_keys[0])

            self.least_recently_used_cache.pop(discarded_key)
            del self.least_frequently_used_cache[discarded_key]
            print("DISCARD:", discarded_key)

    def _add_to_cache(self, key, item):
        self.least_recently_used_cache[key] = item
        self.least_recently_used_cache.move_to_end(key)
        self._increment_lfu_count(key)

    def _increment_lfu_count(self, key):
        if key in self.least_frequently_used_cache:
            self.least_frequently_used_cache[key] += 1
        else:
            self.least_frequently_used_cache[key] = 1


if __name__ == '__main__':
    # Sample usage
    cache = LFUCache()
    cache.put(1, "A")
    cache.put(2, "B")
    print(cache.get(1))  # Output: "A"
    cache.put(3, "C")
    print(cache.get(2))  # Output: "B"
