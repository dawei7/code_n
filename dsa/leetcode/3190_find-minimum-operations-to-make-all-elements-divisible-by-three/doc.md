# Find Minimum Operations to Make All Elements Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3190 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-minimum-operations-to-make-all-elements-divisible-by-three](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/).

### Goal
Given an array of integers, determine the minimum number of operations required to make every element in the array divisible by three. In one operation, you can either increment or decrement an element by exactly one.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the total count of increment or decrement operations needed.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `3`
- Explanation: 1 becomes 3 (2 ops), 2 becomes 3 (1 op), 3 is already divisible, 4 becomes 3 (1 op). Total: 2+1+0+1 = 4? No, 1->0 (1 op), 2->3 (1 op), 3->3 (0 ops), 4->3 (1 op). Total: 3.

**Example 2**

- Input: `nums = [3, 6, 9]`
- Output: `0`

**Example 3**

- Input: `nums = [10, 11, 12]`
- Output: `2`

---

## Solution
### Approach
The problem relies on modular arithmetic. For any integer `n`, the distance to the nearest multiple of 3 is determined by `n % 3`. If `n % 3 == 0`, the cost is 0. If `n % 3 == 1`, we can either subtract 1 (1 operation) or add 2 (2 operations); the minimum is 1. If `n % 3 == 2`, we can either add 1 (1 operation) or subtract 2 (2 operations); the minimum is 1. Thus, for any number not divisible by 3, exactly 1 operation is required.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a single integer variable to track the running total of operations.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum operations to make all elements divisible by 3.
    For any number x:
    - If x % 3 == 0, cost is 0.
    - If x % 3 == 1, we can subtract 1 to reach a multiple of 3 (cost 1).
    - If x % 3 == 2, we can add 1 to reach a multiple of 3 (cost 1).
    """
    operations = 0
    for num in nums:
        if num % 3 != 0:
            operations += 1
    return operations
```
</details>
