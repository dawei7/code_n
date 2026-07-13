# Number of Arithmetic Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2367 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-arithmetic-triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-arithmetic-triplets/).

### Goal
Given a strictly increasing array of integers and a difference value, identify the total number of unique triplets (i, j, k) such that the indices satisfy i < j < k and the values satisfy nums[j] - nums[i] == diff and nums[k] - nums[j] == diff.

### Function Contract
**Inputs**

- `nums`: A list of integers sorted in strictly increasing order.
- `diff`: An integer representing the required constant difference between consecutive elements of the triplet.

**Return value**

- An integer representing the count of valid arithmetic triplets found in the array.

### Examples
**Example 1**

- Input: `nums = [0, 1, 4, 6, 7, 10], diff = 3`
- Output: `2`
- Explanation: The triplets are (1, 4, 7) and (4, 7, 10).

**Example 2**

- Input: `nums = [4, 5, 6, 7, 8, 9], diff = 2`
- Output: `2`
- Explanation: The triplets are (4, 6, 8) and (5, 7, 9).

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5], diff = 1`
- Output: `3`

---

## Solution
### Approach
The problem can be solved efficiently using a Hash Set for O(1) lookups. Since we need to find if `nums[j] - diff` and `nums[j] + diff` exist in the array for every element `nums[j]`, storing all elements in a set allows us to verify the existence of the required triplet components in linear time.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the array once and perform constant-time set lookups.
- **Space Complexity**: O(n) to store the elements of the array in a hash set for efficient retrieval.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], diff: int) -> int:
    """
    Calculates the number of arithmetic triplets in a strictly increasing array.
    Uses a set for O(1) average time complexity lookups.
    """
    num_set = set(nums)
    count = 0

    for x in nums:
        # Check if the preceding and succeeding elements of the triplet exist
        if (x - diff) in num_set and (x + diff) in num_set:
            count += 1

    return count
```
</details>
