## Examples

**Example 1**

- Input: `operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]`
- Output: `[null, null, null, 1, null, -1, null, -1, 3, 4]`
- Explanation:
  1. `LRUCache(2)` constructs a cache that can hold two keys.
  2. `put(1, 1)` stores `{1=1}`.
  3. `put(2, 2)` stores `{1=1, 2=2}`; key `2` is now the most recently used.
  4. `get(1)` returns `1` and makes key `1` the most recently used.
  5. `put(3, 3)` evicts key `2`, leaving `{1=1, 3=3}`.
  6. `get(2)` returns `-1` because key `2` is absent.
  7. `put(4, 4)` evicts key `1`, leaving `{4=4, 3=3}`.
  8. `get(1)` returns `-1` because key `1` is absent.
  9. `get(3)` returns `3`.
  10. `get(4)` returns `4`.
