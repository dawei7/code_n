## Description

Design a data structure that follows the constraints of a **<a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a>**.

Implement the `LRUCache` class:

<ul>
	<li>`LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.</li>
	<li>`int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.</li>
	<li>`void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.</li>
</ul>

The functions `get` and `put` must each run in `O(1)` average time complexity.
