# Minimum Operations to Make Array Values Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3375 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-array-values-equal-to-k](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/).

### Goal
Given an array of integers and a target value `k`, determine the minimum number of operations required to make every element in the array equal to `k`. In one operation, you can choose any value `x` present in the array and replace all occurrences of `x` with any value `y` that is strictly less than `x`. If it is impossible to transform all elements to `k`, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the target value that all elements must eventually become.

**Return value**

- An integer representing the minimum number of operations, or -1 if the transformation is impossible.

### Examples
**Example 1**

- Input: `nums = [5, 2, 5, 4, 5], k = 2`
- Output: `2`

**Example 2**

- Input: `nums = [2, 1, 2], k = 2`
- Output: `-1`

**Example 3**

- Input: `nums = [9, 7, 5, 3], k = 2`
- Output: `-1`

---

## Solution
### Approach
The problem relies on set theory and greedy logic. First, any element smaller than `k` cannot be transformed into `k` because operations only allow decreasing values. If any element in the array is less than `k`, the task is impossible. If the array contains elements greater than `k`, each unique value greater than `k` must be reduced. Since we can reduce any value `x` to any `y < x`, we can greedily reduce the largest unique values down to the next largest unique values until we reach `k`. Thus, the number of operations is simply the count of unique values in the array that are greater than `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array once to identify unique elements and check against `k`.
- **Space Complexity**: `O(u)`, where `u` is the number of unique elements in the array, used to store the set of unique values.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    unique_elements = set(nums)

    # If any element is smaller than k, it's impossible to reach k
    # because we can only decrease values.
    for val in unique_elements:
        if val < k:
            return -1

    # If k is not in the array, we need one extra operation to
    # transform the smallest value (which is > k) into k.
    # If k is in the array, we just need to transform all values > k.
    if k in unique_elements:
        return len(unique_elements) - 1
    else:
        return len(unique_elements)
```
</details>
