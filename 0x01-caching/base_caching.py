#!/usr/bin/python3
""" BaseCaching module
"""

from BaseCaching import BaseCaching  # Import the BaseCaching class

class BasicCache(BaseCaching):
    def __init__(self):
        """ Initialize the BasicCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is not None:
            return self.cache_data.get(key)

# Testing the BasicCache
if __name__ == '__main__':
    my_cache = BasicCache()

    # Adding items to the cache
    my_cache.put("key1", "item1")
    my_cache.put("key2", "item2")

    # Retrieving items from the cache
    print(my_cache.get("key1"))  # Output: item1
    print(my_cache.get("key2"))  # Output: item2
    print(my_cache.get("non-existent-key"))  # Output: None
    print(my_cache.get(None))  # Output: None

    # Adding more items to the cache
    my_cache.put("key3", "item3")
    my_cache.put("key4", "item4")

    # Cache size can grow without limit
    my_cache.put("key5", "item5")

    # Print the cache
    my_cache.print_cache()

