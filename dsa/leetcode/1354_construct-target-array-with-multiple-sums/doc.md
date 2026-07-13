# Construct Target Array With Multiple Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1354 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [construct-target-array-with-multiple-sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/construct-target-array-with-multiple-sums/).

### Goal
Start from an array of all ones. In one move, choose an index and replace that value with the current total sum of the array. Decide whether some sequence of moves can produce the given `target` array.

### Function Contract
**Inputs**

- `target`: a list of positive integers.

**Return value**

`true` if `target` can be constructed from all ones, otherwise `false`.

### Examples
**Example 1**

- Input: `target = [9,3,5]`
- Output: `true`

**Example 2**

- Input: `target = [1,1,1,2]`
- Output: `false`

**Example 3**

- Input: `target = [8,5]`
- Output: `true`

---

## Solution
### Approach
Reverse greedy with a max-heap. Repeatedly reduce the largest value back to the value it had before it was replaced by the array sum, using modulo by the sum of the remaining elements to skip repeated identical reverse moves.

### Complexity Analysis
- **Time Complexity**: `O(n log n + k log n)`, where `k` is the number of reverse heap reductions after modulo compression.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1354: Construct Target Array With Multiple Sums."""

from heapq import heapify, heappop, heappush


def solve(target: list[int]) -> bool:
    if len(target) == 1:
        return target[0] == 1

    total = sum(target)
    heap = [-value for value in target]
    heapify(heap)

    while True:
        largest = -heappop(heap)
        rest = total - largest
        if largest == 1 or rest == 1:
            return True
        if rest == 0 or rest >= largest:
            return False
        previous = largest % rest
        if previous == 0:
            return False
        total = rest + previous
        heappush(heap, -previous)
```
</details>
