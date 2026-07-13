# Maximum Strong Pair XOR I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2932 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Trie, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-strong-pair-xor-i](https://leetcode.com/problems/maximum-strong-pair-xor-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-strong-pair-xor-i/).

### Goal
Given an array of integers, identify all "strong pairs" (x, y) such that the absolute difference between the two numbers is less than or equal to the smaller of the two values (i.e., |x - y| ≤ min(x, y)). Among all such pairs, return the maximum possible result of the bitwise XOR operation (x ^ y).

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the maximum XOR value found among all valid strong pairs.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `7`
- Explanation: The strong pairs include (2, 3) where |2-3|=1 <= 2, and (4, 5) where |4-5|=1 <= 4. The pair (2, 5) is not strong because |2-5|=3 > 2. The maximum XOR is 2^5 = 7.

**Example 2**

- Input: `nums = [10, 20]`
- Output: `0`
- Explanation: |10-20|=10, which is not <= min(10, 20)=10. No strong pairs exist.

**Example 3**

- Input: `nums = [5, 6, 25, 30]`
- Output: `7`
- Explanation: The pair (5, 6) is strong (|5-6|=1 <= 5), 5^6=3. The pair (25, 30) is strong (|25-30|=5 <= 25), 25^30=7. Max is 7.

---

## Solution
### Approach
The problem is solved using a brute-force approach with nested iteration. Since the constraints for this specific version (Maximum Strong Pair XOR I) are small (n ≤ 50), an O(n²) approach is optimal and sufficient. We iterate through all possible pairs (i, j), verify the strong pair condition, and track the maximum XOR value encountered.

### Complexity Analysis
- **Time Complexity**: O(n²), where n is the length of the input array, as we compare every pair of elements.
- **Space Complexity**: O(1), as we only store the maximum XOR value and loop indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    max_xor = 0
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            x = nums[i]
            y = nums[j]

            # Check the strong pair condition: |x - y| <= min(x, y)
            if abs(x - y) <= min(x, y):
                current_xor = x ^ y
                if current_xor > max_xor:
                    max_xor = current_xor

    return max_xor
```
</details>
