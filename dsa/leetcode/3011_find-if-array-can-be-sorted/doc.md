# Find if Array Can Be Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3011 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-if-array-can-be-sorted](https://leetcode.com/problems/find-if-array-can-be-sorted/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-if-array-can-be-sorted/).

### Goal
Determine whether a given array of integers can be transformed into a non-decreasing sorted sequence by repeatedly swapping adjacent elements that share the same number of set bits (binary 1s).

### Function Contract
**Inputs**

- `nums`: A list of positive integers.

**Return value**

- `bool`: Returns `True` if the array can be sorted under the given constraints, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [8, 4, 2, 30, 15]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `True`

**Example 3**

- Input: `nums = [3, 16, 8, 4, 2]`
- Output: `False`

---

## Solution
### Approach
The problem relies on the property that elements with the same number of set bits form "exchangeable groups." Within these groups, elements can be reordered arbitrarily. The array is sortable if and only if, when partitioning the array into contiguous segments of elements with the same bit count, the maximum value of a preceding segment is less than or equal to the minimum value of the succeeding segment.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array once to identify segments and compare their bounds.
- **Space Complexity**: `O(1)`, as we only store a few variables to track the current segment's bounds and the previous segment's maximum.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> bool:
    def count_set_bits(n: int) -> int:
        return bin(n).count('1')

    if not nums:
        return True

    prev_max = -1
    curr_min = nums[0]
    curr_max = nums[0]
    prev_bits = count_set_bits(nums[0])

    for i in range(1, len(nums)):
        curr_bits = count_set_bits(nums[i])

        if curr_bits == prev_bits:
            curr_min = min(curr_min, nums[i])
            curr_max = max(curr_max, nums[i])
        else:
            if prev_max > curr_min:
                return False
            prev_max = curr_max
            curr_min = nums[i]
            curr_max = nums[i]
            prev_bits = curr_bits

    return prev_max <= curr_min
```
</details>
