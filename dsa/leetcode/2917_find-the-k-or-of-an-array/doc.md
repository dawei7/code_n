# Find the K-or of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2917 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-k-or-of-an-array](https://leetcode.com/problems/find-the-k-or-of-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-k-or-of-an-array/).

### Goal
Given an array of integers and an integer `k`, calculate a new integer (the "K-or") where the $i$-th bit is set to 1 if and only if at least `k` elements in the input array have their $i$-th bit set to 1. Otherwise, the $i$-th bit of the result is 0.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: An integer representing the threshold count for bit activation.

**Return value**

- An integer representing the calculated K-or value.

### Examples
**Example 1**

- Input: `nums = [7, 12, 9, 8, 9, 15], k = 4`
- Output: `9`

**Example 2**

- Input: `nums = [1, 2, 3], k = 1`
- Output: `3`

**Example 3**

- Input: `nums = [10, 8, 5, 9, 11, 6, 8], k = 1`
- Output: `15`

---

## Solution
### Approach
The problem utilizes bitwise manipulation and frequency counting. Since the input integers are typically within a 32-bit range, we can iterate through each bit position (0 to 31). For each position, we count how many numbers in the array have that specific bit set. If the count meets or exceeds `k`, we set the corresponding bit in our result using the bitwise OR operator.

### Complexity Analysis
- **Time Complexity**: $O(n \cdot \log(\max(nums)))$, where $n$ is the length of the array. Given the constraints (usually 32 bits), this simplifies to $O(n)$.
- **Space Complexity**: $O(1)$, as we only use a constant amount of extra space regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the K-or of an array by checking the frequency of set bits
    at each position from 0 to 31.
    """
    k_or_result = 0

    # Iterate through each bit position (assuming 32-bit integers)
    for i in range(32):
        count = 0
        mask = 1 << i

        # Count how many numbers have the i-th bit set
        for num in nums:
            if num & mask:
                count += 1

        # If the count meets the threshold k, set the i-th bit in the result
        if count >= k:
            k_or_result |= mask

    return k_or_result
```
</details>
