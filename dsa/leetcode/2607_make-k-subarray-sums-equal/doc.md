# Make K-Subarray Sums Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2607 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [make-k-subarray-sums-equal](https://leetcode.com/problems/make-k-subarray-sums-equal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/make-k-subarray-sums-equal/).

### Goal
Given an integer array `arr` and an integer `k`, determine the minimum number of operations required to make the sum of every contiguous subarray of length `k` equal. In one operation, you can increment or decrement any element of the array by 1.

### Function Contract
**Inputs**

- `arr`: A list of integers representing the initial array.
- `k`: An integer representing the length of the subarrays that must have equal sums.

**Return value**

- An integer representing the minimum total operations (sum of absolute differences) to satisfy the condition.

### Examples
**Example 1**

- Input: `arr = [1, 4, 1, 3], k = 2`
- Output: `1`
- Explanation: We can change the array to `[1, 3, 1, 3]`. Subarrays of length 2 are `[1, 3]` (sum 4) and `[3, 1]` (sum 4) and `[1, 3]` (sum 4).

**Example 2**

- Input: `arr = [2, 5, 5, 7], k = 3`
- Output: `5`
- Explanation: We can change the array to `[5, 5, 5, 5]`.

**Example 3**

- Input: `arr = [4, 3, 2, 1], k = 4`
- Output: `0`

---

## Solution
### Approach
The problem implies that `arr[i] == arr[i + k]` must hold for all `i` to ensure all subarrays of length `k` have the same sum. This partitions the array into `gcd(n, k)` independent cycles. For each cycle, we collect the elements and find the median. The minimum operations to make all elements in a cycle equal to a target value is achieved when the target is the median of those elements.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the array, due to sorting the elements within each cycle.
- **Space Complexity**: `O(n)` to store the elements of the cycles.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(arr: list[int], k: int) -> int:
    n = len(arr)
    k = math.gcd(k, n)
    visited = [False] * n
    total_ops = 0

    for i in range(n):
        if not visited[i]:
            # Extract all elements belonging to the same cycle
            cycle = []
            curr = i
            while not visited[curr]:
                visited[curr] = True
                cycle.append(arr[curr])
                curr = (curr + k) % n

            # To minimize sum of absolute differences,
            # we transform all elements in the cycle to their median.
            cycle.sort()
            median = cycle[len(cycle) // 2]

            for val in cycle:
                total_ops += abs(val - median)

    return total_ops
```
</details>
