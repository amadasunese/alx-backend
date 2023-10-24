#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the first item that was added (FIFO)
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}\n")
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

