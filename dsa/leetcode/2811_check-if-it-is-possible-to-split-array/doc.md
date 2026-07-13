# Check if it is Possible to Split Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2811 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-it-is-possible-to-split-array](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/).

### Goal
Determine if an array can be fully partitioned into individual elements (each of size 1) through a sequence of valid splits. A split is valid if the sum of the elements in the subarray being divided is at least `m`, unless the subarray already contains only one element.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array to be split.
- `m`: An integer representing the minimum sum threshold required for a valid split.

**Return value**

- A boolean value: `True` if the array can be reduced to single-element subarrays following the rules, `False` otherwise.

### Examples
**Example 1**

- Input: `nums = [2, 2, 1], m = 4`
- Output: `true`

**Example 2**

- Input: `nums = [2, 1, 3], m = 5`
- Output: `false`

**Example 3**

- Input: `nums = [2, 3, 3, 2, 3], m = 6`
- Output: `true`

---

## Solution
### Approach
The problem can be solved using a Greedy approach. If the array length is 2 or less, it is always possible to split (or it is already split). For larger arrays, the condition is satisfied if there exist any two adjacent elements whose sum is at least `m`. This is because if such a pair exists, we can always isolate the other elements one by one from the ends until we reach that pair.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we only need to check adjacent pairs.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], m: int) -> bool:
    """
    Determines if the array can be split into single elements given the threshold m.

    Logic:
    If the array length is <= 2, it is always possible to split.
    For length > 2, it is possible if and only if there exists at least one
    adjacent pair (nums[i], nums[i+1]) such that nums[i] + nums[i+1] >= m.
    """
    n = len(nums)

    # Arrays of length 1 or 2 can always be fully split.
    if n <= 2:
        return True

    # Check if any two adjacent elements sum to at least m.
    for i in range(n - 1):
        if nums[i] + nums[i + 1] >= m:
            return True

    return False
```
</details>
