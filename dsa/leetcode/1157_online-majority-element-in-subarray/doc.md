# Online Majority Element In Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1157 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Design, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [online-majority-element-in-subarray](https://leetcode.com/problems/online-majority-element-in-subarray/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/online-majority-element-in-subarray/).

### Goal
Design a structure that answers range queries asking for a value that appears at least `threshold` times in `arr[left:right+1]`.

### Function Contract
**Inputs**

- `arr`: array passed to the constructor.
- `queries`: list of `[left, right, threshold]` range queries.

**Return value**

List of query results. Each result is a value meeting the threshold inside the range, or `-1` if no such value exists.

### Examples
**Example 1**

- Input: `arr = [1,1,2,2,1,1], queries = [[0,5,4]]`
- Output: `[1]`

**Example 2**

- Input: `arr = [1,1,2,2,1,1], queries = [[0,3,3]]`
- Output: `[-1]`

**Example 3**

- Input: `arr = [2,2,1,1,1,2,2], queries = [[2,4,2]]`
- Output: `[1]`

---

## Solution
### Approach
Segment tree with majority-candidate merging and binary-search verification.

### Complexity Analysis
- **Time Complexity**: constructor `O(n log n)` including position indexes, each query `O(log n + log f)` where `f` is the candidate's global frequency.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left, bisect_right
from collections import defaultdict


class MajorityChecker:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.positions = defaultdict(list)
        for index, value in enumerate(arr):
            self.positions[value].append(index)

        size = 1
        while size < self.n:
            size *= 2
        self.size = size
        self.tree = [(0, 0)] * (2 * size)
        for index, value in enumerate(arr):
            self.tree[size + index] = (value, 1)
        for index in range(size - 1, 0, -1):
            self.tree[index] = self._merge(self.tree[index * 2], self.tree[index * 2 + 1])

    def _merge(self, left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        left_value, left_count = left
        right_value, right_count = right
        if left_value == right_value:
            return left_value, left_count + right_count
        if left_count > right_count:
            return left_value, left_count - right_count
        return right_value, right_count - left_count

    def _candidate(self, left: int, right: int) -> int:
        left += self.size
        right += self.size
        left_result = (0, 0)
        right_result = (0, 0)
        while left <= right:
            if left % 2 == 1:
                left_result = self._merge(left_result, self.tree[left])
                left += 1
            if right % 2 == 0:
                right_result = self._merge(self.tree[right], right_result)
                right -= 1
            left //= 2
            right //= 2
        return self._merge(left_result, right_result)[0]

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate = self._candidate(left, right)
        indexes = self.positions[candidate]
        count = bisect_right(indexes, right) - bisect_left(indexes, left)
        return candidate if count >= threshold else -1


def solve(arr, queries):
    checker = MajorityChecker(arr)
    return [checker.query(left, right, threshold) for left, right, threshold in queries]
```
</details>
