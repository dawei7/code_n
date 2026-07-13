# Minimum Number of Operations to Make Arrays Similar

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2449 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-operations-to-make-arrays-similar](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/).

### Goal
Given two arrays of equal length, transform the first array into the second by repeatedly choosing two indices and adding 2 to one element while subtracting 2 from the other. Determine the minimum number of operations required to make the arrays identical, noting that the order of elements in the arrays does not matter.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `target`: A list of integers representing the desired final state.

**Return value**

- An integer representing the minimum number of operations required to make `nums` equal to `target`.

### Examples
**Example 1**

- Input: `nums = [8,12,6], target = [2,14,10]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,5], target = [4,1,3]`
- Output: `1`

**Example 3**

- Input: `nums = [1,1,1,1,1], target = [1,1,1,1,1]`
- Output: `0`

---

## Solution
### Approach
The problem relies on the observation that adding/subtracting 2 preserves the parity of each number. Therefore, we must sort the odd and even numbers of both arrays separately. Once sorted, the difference between corresponding elements in `nums` and `target` represents the total displacement needed. Since each operation reduces the total positive difference by 2 (by moving 2 from one index to another), the total number of operations is the sum of all positive differences divided by 2.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting of the arrays, where N is the length of the input arrays.
- **Space Complexity**: `O(N)` to store the partitioned odd and even elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], target: list[int]) -> int:
    # Separate numbers by parity because operations only affect numbers of the same parity
    nums_even = sorted([x for x in nums if x % 2 == 0])
    nums_odd = sorted([x for x in nums if x % 2 != 0])

    target_even = sorted([x for x in target if x % 2 == 0])
    target_odd = sorted([x for x in target if x % 2 != 0])

    def calculate_ops(n_list, t_list):
        ops = 0
        for n, t in zip(n_list, t_list):
            # If n < t, we need to add to n, which is half the difference
            if n < t:
                ops += (t - n) // 2
        return ops

    # The total operations is the sum of positive differences divided by 2.
    # Since the sum of differences is 0, the sum of positive differences
    # equals the absolute sum of negative differences.
    return calculate_ops(nums_even, target_even) + calculate_ops(nums_odd, target_odd)
```
</details>
