# Alternating Groups III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3245 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [alternating-groups-iii](https://leetcode.com/problems/alternating-groups-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/alternating-groups-iii/).

### Goal
Given a circular binary array representing colors, determine the number of contiguous subarrays of length `k` that consist of alternating colors (0 and 1). Additionally, handle dynamic updates where specific indices in the array change their color, and query the total count of such alternating groups after each update.

### Function Contract
**Inputs**

- `colors`: A list of integers (0 or 1) representing the circular array.
- `queries`: A list of queries, where each query is either `[1, k]` (count alternating groups of length `k`) or `[2, i, c]` (update `colors[i]` to `c`).

**Return value**

- A list of integers containing the results for every type-1 query.

### Examples
**Example 1**

- Input: `colors = [0, 1, 0, 1, 0], queries = [[2, 1, 0], [1, 4]]`
- Output: `[2]`
- Explanation: After updating index 1 to 0, the array becomes `[0, 0, 0, 1, 0]`. The alternating groups of length 4 are checked.

**Example 2**

- Input: `colors = [0, 0, 1, 0, 1], queries = [[1, 3], [2, 3, 0], [1, 3]]`
- Output: `[2, 0]`

**Example 3**

- Input: `colors = [1, 0, 1, 0, 1], queries = [[1, 2], [2, 0, 0], [1, 2]]`
- Output: `[5, 4]`

---

## Solution
### Approach
The problem is solved by maintaining the "breaks" in the alternating pattern (where `colors[i] == colors[i+1]`). A Binary Indexed Tree (BIT) or Fenwick Tree is used to store the lengths of contiguous alternating segments. Specifically, we track the lengths of segments of alternating colors and use the BIT to calculate how many segments of length at least `k` exist, accounting for the circular nature of the array by duplicating the array or handling the wrap-around index.

### Complexity Analysis
- **Time Complexity**: `O((n + q) log n)`, where `n` is the length of the array and `q` is the number of queries. Each update and query operation takes logarithmic time using the BIT.
- **Space Complexity**: `O(n)`, required to store the BIT and the current state of the array.

### Reference Implementations
<details>
<summary>python</summary>

```python
class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class _Node:
    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key: int):
        self.key = key
        z = (key + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & ((1 << 64) - 1)
        self.priority = z ^ (z >> 31)
        self.left = None
        self.right = None


def _merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.priority < right.priority:
        left.right = _merge(left.right, right)
        return left
    right.left = _merge(left, right.left)
    return right


def _split(root, key: int):
    if root is None:
        return None, None
    if root.key < key:
        left, right = _split(root.right, key)
        root.right = left
        return root, right
    left, right = _split(root.left, key)
    root.left = right
    return left, root


def _insert(root, key: int):
    left, right = _split(root, key)
    return _merge(_merge(left, _Node(key)), right)


def _erase(root, key: int):
    if root is None:
        return None
    if key == root.key:
        return _merge(root.left, root.right)
    if key < root.key:
        root.left = _erase(root.left, key)
    else:
        root.right = _erase(root.right, key)
    return root


def _contains(root, key: int) -> bool:
    while root is not None:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False


def _predecessor(root, key: int):
    result = None
    while root is not None:
        if root.key < key:
            result = root.key
            root = root.right
        else:
            root = root.left
    return result


def _successor(root, key: int):
    result = None
    while root is not None:
        if root.key > key:
            result = root.key
            root = root.left
        else:
            root = root.right
    return result


def _minimum(root):
    while root.left is not None:
        root = root.left
    return root.key


def _maximum(root):
    while root.right is not None:
        root = root.right
    return root.key


def solve(colors, queries):
    n = len(colors)
    if n == 0:
        return []

    count_by_len = FenwickTree(n)
    sum_by_len = FenwickTree(n)
    root = None
    break_count = 0

    def dist(left: int, right: int) -> int:
        return (right - left) % n or n

    def add_len(length: int, delta: int) -> None:
        count_by_len.add(length, delta)
        sum_by_len.add(length, delta * length)

    def add_break(pos: int) -> None:
        nonlocal root, break_count
        if _contains(root, pos):
            return
        if break_count == 0:
            add_len(n, 1)
        else:
            prev_pos = _predecessor(root, pos)
            next_pos = _successor(root, pos)
            if prev_pos is None:
                prev_pos = _maximum(root)
            if next_pos is None:
                next_pos = _minimum(root)
            add_len(dist(prev_pos, next_pos), -1)
            add_len(dist(prev_pos, pos), 1)
            add_len(dist(pos, next_pos), 1)
        root = _insert(root, pos)
        break_count += 1

    def remove_break(pos: int) -> None:
        nonlocal root, break_count
        if not _contains(root, pos):
            return
        if break_count == 1:
            add_len(n, -1)
        else:
            prev_pos = _predecessor(root, pos)
            next_pos = _successor(root, pos)
            if prev_pos is None:
                prev_pos = _maximum(root)
            if next_pos is None:
                next_pos = _minimum(root)
            add_len(dist(prev_pos, pos), -1)
            add_len(dist(pos, next_pos), -1)
            add_len(dist(prev_pos, next_pos), 1)
        root = _erase(root, pos)
        break_count -= 1

    def is_break(pos: int) -> bool:
        return colors[pos] == colors[(pos + 1) % n]

    for i in range(n):
        if is_break(i):
            add_break(i)

    results = []
    for query in queries:
        if query[0] == 1:
            size = query[1]
            if size <= 1:
                results.append(n)
            elif size > n:
                results.append(0)
            elif break_count == 0:
                results.append(n)
            else:
                below_count = count_by_len.sum(size - 1)
                below_sum = sum_by_len.sum(size - 1)
                usable_count = break_count - below_count
                usable_sum = n - below_sum
                results.append(usable_sum - (size - 1) * usable_count)
        else:
            index, color = query[1], query[2]
            if colors[index] == color:
                continue
            affected = ((index - 1) % n, index)
            for pos in affected:
                if is_break(pos):
                    remove_break(pos)
            colors[index] = color
            for pos in affected:
                if is_break(pos):
                    add_break(pos)

    return results
```
</details>
