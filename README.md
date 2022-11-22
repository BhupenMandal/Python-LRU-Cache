# LRU Cache

## Task Description
 The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

## Explanation
To maintain the time and space complexity of O(1), I believed that using OrderedDict() structure was necessary. 
This type of Dictionary has methods which makes moving data inside the Dictionary easier and more efficient compared to the traditional dictionary. 
Since the amount of data doesn’t matter as increase in data wouldn’t affect the efficiency of the code, both Time and Space complexity would maintain a Big O(1). 
Also, the Get and Set operations will run in constant time.