# Count the Number of Good Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2963 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-the-number-of-good-partitions](https://leetcode.com/problems/count-the-number-of-good-partitions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-the-number-of-good-partitions/).

### Goal
Given an array of integers, a partition is considered "good" if every element present in one subarray does not appear in any other subarray. We need to determine the total number of ways to partition the array into one or more such good subarrays. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 10^5 and 1 <= nums[i] <= 10^9.

**Return value**

- An integer representing the number of valid partitions modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `8`

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 2, 1, 3]`
- Output: `2`

---

## Solution
### Approach
The problem relies on identifying "boundaries" where a partition can occur. An element's range is defined by its first and last occurrence. If two ranges overlap, they must belong to the same partition. By calculating the last occurrence of every element, we can iterate through the array and maintain a `max_reach` pointer. Whenever our current index matches `max_reach`, we have completed a valid, independent block. If there are `k` such independent blocks, there are `k-1` possible cut points, leading to `2^(k-1)` total ways to partition the array.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the length of the array. We traverse the array twice: once to map the last indices and once to identify the partition boundaries.
- **Space Complexity**: `O(N)` to store the hash map of the last occurrence indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7

    # Map each number to its last occurrence index
    last_occurrence = {val: i for i, val in enumerate(nums)}

    num_blocks = 0
    max_reach = 0

    # Iterate through the array to find independent segments
    for i, val in enumerate(nums):
        # Update the furthest index we need to reach to satisfy the current partition
        max_reach = max(max_reach, last_occurrence[val])

        # If the current index is the end of a block
        if i == max_reach:
            num_blocks += 1

    # If there are k blocks, there are k-1 places to cut,
    # resulting in 2^(k-1) possible ways to partition.
    return pow(2, num_blocks - 1, MOD)
```
</details>
