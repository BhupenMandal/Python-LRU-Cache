# LRU Cache

## Task Description
 The goal will be to design a data structure known as a Least Recently Used (LRU) cache.
 An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
 For the current problem, consider both get and set operations as an use operation.

## Explaination
To maintain the time and space complexity of O(1), I believed that using OrderedDict() structure was necessary. 
This type of Dictionary has methods which makes moving data inside the Dictionary easier and more efficient compared to the traditional dictionary. 
Since the amount of data doesn’t matter as increase in data wouldn’t affect the efficiency of the code, both Time and Space complexity would maintain a Big O(1). 
Also, the Get and Set operations will run in constant time.