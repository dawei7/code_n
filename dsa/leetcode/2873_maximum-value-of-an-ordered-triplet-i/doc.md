# Maximum Value of an Ordered Triplet I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2873 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-value-of-an-ordered-triplet-i](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/).

### Goal
Given an array of integers, identify three indices (i, j, k) such that i < j < k, and calculate the value defined by the expression (nums[i] - nums[j]) * nums[k]. The objective is to find the maximum possible value resulting from this calculation. If all possible results are negative, the function should return 0.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 100 and 1 <= nums[i] <= 10^6.

**Return value**

- An integer representing the maximum value of (nums[i] - nums[j]) * nums[k] for any valid triplet, or 0 if no positive value can be formed.

### Examples
**Example 1**

- Input: `nums = [12, 6, 1, 2, 7]`
- Output: `77`
- Explanation: Choosing indices (0, 1, 4) gives (12 - 6) * 7 = 42. Choosing (0, 2, 4) gives (12 - 1) * 7 = 77.

**Example 2**

- Input: `nums = [1, 10, 3, 4, 19]`
- Output: `133`
- Explanation: Choosing indices (1, 2, 4) gives (10 - 3) * 19 = 133.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`
- Explanation: The result is (1 - 2) * 3 = -3. Since the result is negative, return 0.

---

## Solution
### Approach
Brute force iteration using three nested loops to evaluate every possible triplet (i, j, k) where 0 <= i < j < k < n.

### Complexity Analysis
- **Time Complexity**: O(n^3), where n is the length of the input array, due to the three nested loops.
- **Space Complexity**: O(1), as we only use a few variables to track the maximum value.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    n = len(nums)
    max_val = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_val = (nums[i] - nums[j]) * nums[k]
                if current_val > max_val:
                    max_val = current_val

    return max_val
```
</details>
