import collections


class LRU_Cache:

    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = collections.OrderedDict()

    def set(self, key, value):
        if self.max_size == 0:
            return

        if key in self.cache:
            self.cache.move_to_end(key, last=True)

        else:
            if len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)

        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return -1

        else:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print("\nTest Case 1")
print(our_cache.cache)
print("", our_cache.get(1))  # Should return 1 because 1 exists
print(our_cache.cache)  # Should return (2,2) at the first position as 1 is used and that makes 2 Least recently used
print("", our_cache.get(2))  # Should return 2 because 2 exists
print(our_cache.cache)  # Should return (3,3) at the first position as 2 is used and that makes 3 Least recently used
print(our_cache.get(9))  # Should return -1 because 9 doesn't exist in the cache
print(our_cache.cache)  # No change in OrderedDict as 9 never existed

print("\nTest Case 2")

our_cache.set(5, 5)

our_cache.set(6, 6)

print(our_cache.get(3))  # Should return -1 because maximum size has been reached
print(our_cache.cache)  # As maxsize has been reached, (3,3) was removed, making (4,4) Least Recently Used

print("\nTest Case 3")
our_cache = LRU_Cache(0)
our_cache.set(8, 8)
print(our_cache.get(8))  # Should return -1 because cache is set to 0 and hence empty
print(our_cache.cache)  # No elements because dict is empty

print("\nTest Case 4")
our_cache = LRU_Cache(1)
our_cache.set(8, 4)
print(our_cache.get(8))  # Should return 4 because cache is set to (8, 4)
print(our_cache.cache)
our_cache.set(8, 3)
print(our_cache.cache)  # As the maxsize of the dict here is only 1, (8,4) is replaced by (8,3)
