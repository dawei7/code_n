## Examples

**Example 1**

- Input: `operations = ["LFUCache","put","put","get","put","get","get","put","get","get","get"], arguments = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]`
- Output: `[null,null,null,1,null,-1,3,null,-1,3,4]`
- **Explanation:** Let `cnt(x)` be key `x`'s use counter. In the cache-order displays below, the leftmost key is the most recently used among tied keys.
  1. `LFUCache(2)` constructs a cache with room for two keys.
  2. `put(1, 1)` gives `cache = [1, _]` and `cnt(1) = 1`.
  3. `put(2, 2)` gives `cache = [2, 1]`, with `cnt(2) = 1` and `cnt(1) = 1`.
  4. `get(1)` returns `1`; now `cache = [1, 2]`, `cnt(1) = 2`, and `cnt(2) = 1`.
  5. `put(3, 3)` evicts key `2`, the unique least frequently used key, leaving `cache = [3, 1]` with `cnt(3) = 1` and `cnt(1) = 2`.
  6. `get(2)` returns `-1` because key `2` is absent.
  7. `get(3)` returns `3`; now `cache = [3, 1]` and both resident keys have frequency `2`.
  8. `put(4, 4)` sees that keys `1` and `3` tie in frequency, but key `1` is less recent, so it evicts `1`. The cache becomes `[4, 3]`, with `cnt(4) = 1` and `cnt(3) = 2`.
  9. `get(1)` returns `-1` because key `1` is absent.
  10. `get(3)` returns `3`; the cache order is `[3, 4]`, with `cnt(3) = 3` and `cnt(4) = 1`.
  11. `get(4)` returns `4`; the cache order is `[4, 3]`, with `cnt(4) = 2` and `cnt(3) = 3`.
