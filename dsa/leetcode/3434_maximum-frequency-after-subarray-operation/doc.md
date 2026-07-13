# Maximum Frequency After Subarray Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3434 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Greedy, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-frequency-after-subarray-operation](https://leetcode.com/problems/maximum-frequency-after-subarray-operation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-frequency-after-subarray-operation/).

### Goal
Given an array of integers and a target integer `k`, you are allowed to perform exactly one operation: choose a single subarray and replace all its elements with a chosen integer `x`. The objective is to maximize the total frequency of `k` in the array after performing this operation optimally.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the target value whose frequency we want to maximize.

**Return value**

- An integer representing the maximum possible frequency of `k` after replacing one subarray with some value `x`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], k = 2`
- Output: `2`
- Explanation: Replace the subarray `[1]` with `2` to get `[2, 2, 3, 4]`. The frequency of 2 becomes 2.

**Example 2**

- Input: `nums = [1, 1, 1, 1], k = 1`
- Output: `4`
- Explanation: No operation needed, the frequency is already 4.

**Example 3**

- Input: `nums = [1, 2, 1, 2], k = 1`
- Output: `3`
- Explanation: Replace the subarray `[2]` with `1` to get `[1, 1, 1, 2]`. The frequency of 1 becomes 3.

---

## Solution
### Approach
The problem can be solved using a variation of Kadane's Algorithm. For every distinct integer `x` present in the array (other than `k`), we want to find a subarray where the net gain of replacing `x` with `k` is maximized. The gain for each element is `+1` if the element is `x` (because it becomes `k`) and `-1` if the element is `k` (because it is overwritten). We calculate the maximum subarray sum of these gains for each `x` and add it to the initial frequency of `k`.

### Complexity Analysis
- **Time Complexity**: `O(N * U)`, where `N` is the length of the array and `U` is the number of unique elements in the array. In the worst case, this is `O(N^2)` if all elements are unique, but practically efficient for typical constraints.
- **Space Complexity**: `O(N)` to store the frequency map or the unique elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # Initial frequency of k
    initial_k_count = nums.count(k)

    # Identify all unique numbers in the array
    unique_elements = set(nums)

    max_gain = 0

    # For each candidate x, we want to maximize the gain:
    # Gain = (count of x in subarray) - (count of k in subarray)
    # This is equivalent to finding the maximum subarray sum where:
    # x contributes +1 and k contributes -1
    for x in unique_elements:
        if x == k:
            continue

        current_gain = 0
        for num in nums:
            if num == x:
                current_gain += 1
            elif num == k:
                current_gain -= 1

            if current_gain < 0:
                current_gain = 0

            if current_gain > max_gain:
                max_gain = current_gain

    return initial_k_count + max_gain
```
</details>
