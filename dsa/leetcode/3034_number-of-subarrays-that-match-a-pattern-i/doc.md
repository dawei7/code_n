# Number of Subarrays That Match a Pattern I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3034 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-subarrays-that-match-a-pattern-i](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/).

### Goal
Given an array of integers `nums` and a pattern array `pattern` consisting of elements {-1, 0, 1}, determine how many contiguous subarrays of `nums` of length `m + 1` (where `m` is the length of `pattern`) satisfy the specified relationship sequence. A relationship is defined as: 1 if `nums[i+1] > nums[i]`, 0 if `nums[i+1] == nums[i]`, and -1 if `nums[i+1] < nums[i]`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to search within.
- `pattern`: A list of integers (values -1, 0, or 1) representing the target relationship sequence.

**Return value**

- An integer representing the total count of subarrays in `nums` that match the provided `pattern`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5, 6]`, `pattern = [1, 1]`
- Output: `4`

**Example 2**

- Input: `nums = [1, 4, 4, 1, 3, 5, 5, 3]`, `pattern = [1, 0, -1]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 3, 2, 1]`, `pattern = [1, -1]`
- Output: `2`

---

## Solution
### Approach
The problem is a variation of the string matching problem. We first transform the `nums` array into a sequence of relationships (differences) of length `n-1`. Once transformed, the problem reduces to finding the number of occurrences of the `pattern` array within this new sequence, which can be solved using a sliding window approach or string matching algorithms like KMP.

### Complexity Analysis
- **Time Complexity**: `O(n * m)`, where `n` is the length of `nums` and `m` is the length of `pattern`. In each window of the transformed array, we compare `m` elements.
- **Space Complexity**: `O(n)`, used to store the transformed relationship array. This can be optimized to `O(1)` if we compute relationships on-the-fly.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], pattern: list[int]) -> int:
    n = len(nums)
    m = len(pattern)

    # Transform nums into a relationship sequence
    # rels[i] represents the relationship between nums[i] and nums[i+1]
    rels = []
    for i in range(n - 1):
        if nums[i+1] > nums[i]:
            rels.append(1)
        elif nums[i+1] == nums[i]:
            rels.append(0)
        else:
            rels.append(-1)

    count = 0
    # We need to find how many subarrays of length m in rels match pattern
    # The number of possible starting positions is len(rels) - m + 1
    if len(rels) < m:
        return 0

    for i in range(len(rels) - m + 1):
        match = True
        for j in range(m):
            if rels[i + j] != pattern[j]:
                match = False
                break
        if match:
            count += 1

    return count
```
</details>
