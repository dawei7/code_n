# Smallest Missing Non-negative Integer After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2598 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-missing-non-negative-integer-after-operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/).

### Goal
Given an array of integers and an integer `value`, you are allowed to repeatedly add or subtract `value` from any element in the array. The objective is to determine the smallest non-negative integer (MEX - Minimum Excluded value) that cannot be formed by any element in the array after performing any number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `value`: An integer representing the step size for allowed modifications.

**Return value**

- An integer representing the smallest non-negative integer that cannot be represented in the modified array.

### Examples
**Example 1**

- Input: `nums = [1, -10, 7, 13, 6, 8], value = 5`
- Output: `4`

**Example 2**

- Input: `nums = [1, -10, 7, 13, 6, 8], value = 7`
- Output: `2`

**Example 3**

- Input: `nums = [3, 0, 3, 2, 4, 2, 1, 1, 0, 4], value = 5`
- Output: `10`

---

## Solution
### Approach
The problem relies on modular arithmetic. Since we can add or subtract `value` infinitely, any number `x` is equivalent to `x % value`. We can map every number in the input to its remainder modulo `value`. By counting the frequency of each remainder, we can determine how many times each remainder class can "fill" a slot in the sequence 0, 1, 2, ... . We greedily fill the sequence by checking which remainder class has the fewest occurrences, effectively finding the first gap in the sequence.

### Complexity Analysis
- **Time Complexity**: `O(n + value)`, where `n` is the length of the input array. We iterate through the array once to count remainders and then iterate up to `value` to find the MEX.
- **Space Complexity**: `O(value)`, used to store the frequency counts of the remainders.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums: list[int], value: int) -> int:
    # Calculate the remainder of each number modulo 'value'.
    # Since we can add/subtract 'value' infinitely, any number x
    # can be transformed into any number y such that y % value == x % value.
    # We use (n % value) to handle negative numbers correctly in Python.
    counts = Counter(n % value for n in nums)

    # We want to find the smallest non-negative integer 'mex'
    # such that we cannot form 'mex'.
    # We can form 'mex' if we have at least one number with remainder (mex % value).
    # Specifically, if we have 'k' numbers with remainder 'r', we can form
    # the values r, r + value, r + 2*value, ..., r + (k-1)*value.

    mex = 0
    while True:
        remainder = mex % value
        if counts[remainder] > 0:
            counts[remainder] -= 1
            mex += 1
        else:
            return mex
```
</details>
