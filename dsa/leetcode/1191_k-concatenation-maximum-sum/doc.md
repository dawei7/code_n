# K-Concatenation Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [k-concatenation-maximum-sum](https://leetcode.com/problems/k-concatenation-maximum-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/k-concatenation-maximum-sum/).

### Goal
Concatenate `arr` with itself `k` times and find the maximum sum of a non-empty subarray, returning the value modulo `1_000_000_007`. A negative best sum is reported as `0`.

### Function Contract
**Inputs**

- `arr`: integer array.
- `k`: number of concatenations.

**Return value**

The maximum subarray sum in the concatenated array, modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `arr = [1,2]`, `k = 3`
- Output: `9`

**Example 2**

- Input: `arr = [1,-2,1]`, `k = 5`
- Output: `2`

**Example 3**

- Input: `arr = [-1,-2]`, `k = 7`
- Output: `0`

---

## Solution
### Approach
Kadane's algorithm with prefix/suffix reasoning.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr, k):
    mod = 1_000_000_007

    def kadane(values):
        best = current = 0
        for value in values:
            current = max(0, current + value)
            best = max(best, current)
        return best

    if k == 1:
        return kadane(arr) % mod
    best_twice = kadane(arr * 2)
    total = sum(arr)
    if total > 0:
        best_twice += (k - 2) * total
    return best_twice % mod
```
</details>
