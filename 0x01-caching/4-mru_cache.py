#!/usr/bin/python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class for caching system using Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        super().__init__()
        self.head, self.tail = 'head', 'tail'
        self.next_node, self.prev_node = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """Add handle elements to the linked list."""
        self.next_node[head], self.prev_node[tail] = tail, head

    def _remove(self, key):
        """Remove an element from the cache."""
        self.handle(self.prev_node[key], self.next_node[key])
        del self.prev_node[key], self.next_node[key], self.cache_data[key]

    def _add(self, key, item):
        """MRU algorithm: add an element to the cache."""
        if len(self.cache_data) > self.MAX_ITEMS - 1:
            removed_key = self.prev_node[self.tail]
            print("DISCARD: {}".format(removed_key))
            self._remove(removed_key)
        self.cache_data[key] = item
        self.handle(self.prev_node[self.tail], key)
        self.handle(key, self.tail)

    def put(self, key, item):
        """Assign a key-value pair to the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """Retrieve the value for a given key."""
        if key is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value
        return None
