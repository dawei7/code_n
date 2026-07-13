# Average Value of Even Numbers That Are Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2455 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [average-value-of-even-numbers-that-are-divisible-by-three](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/).

### Goal
Given an array of integers, identify all elements that are both even and divisible by three (i.e., divisible by six). Calculate the integer average of these specific elements by summing them and dividing by the count of such elements. If no such numbers exist, return zero.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the floor average of the filtered numbers, or `0` if the filtered set is empty.

### Examples
**Example 1**

- Input: `nums = [1, 3, 6, 10, 12, 15]`
- Output: `9`
- Explanation: The numbers divisible by 6 are 6 and 12. (6 + 12) / 2 = 9.

**Example 2**

- Input: `nums = [1, 2, 4, 7, 10]`
- Output: `0`
- Explanation: No numbers are divisible by 6.

**Example 3**

- Input: `nums = [6, 12, 18, 24]`
- Output: `15`
- Explanation: (6 + 12 + 18 + 24) / 4 = 15.

---

## Solution
### Approach
The problem utilizes a linear scan (filtering) approach. We iterate through the array once, maintaining a running sum and a counter for elements that satisfy the condition `x % 6 == 0`. Finally, we perform integer division.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass over the data.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    total_sum = 0
    count = 0

    for num in nums:
        if num % 6 == 0:
            total_sum += num
            count += 1

    return total_sum // count if count > 0 else 0
```
</details>
