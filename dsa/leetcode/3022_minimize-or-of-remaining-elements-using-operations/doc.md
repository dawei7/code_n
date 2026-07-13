# Minimize OR of Remaining Elements Using Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3022 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-or-of-remaining-elements-using-operations](https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/).

### Goal
Given an array of integers and an integer `k`, you are allowed to perform an operation at most `k` times: choose any two adjacent elements and replace them with their bitwise AND. The objective is to minimize the bitwise OR of all elements remaining in the array after performing at most `k` operations.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum number of operations allowed.

**Return value**

- An integer representing the minimum possible bitwise OR of the array after at most `k` operations.

### Examples
**Example 1**

- Input: `nums = [3, 5, 3, 2, 7], k = 2`
- Output: `3`

**Example 2**

- Input: `nums = [7, 3, 15, 14, 2, 8], k = 4`
- Output: `2`

**Example 3**

- Input: `nums = [10, 12], k = 2`
- Output: `10`

---

## Solution
### Approach
The problem is solved using a **Greedy approach combined with Bit Manipulation**. Since we want to minimize the final OR sum, we attempt to set each bit from most significant (30) to least significant (0) to 0. For each bit, we check if it is possible to make the final OR result have a 0 at that position while keeping all previously decided 0-bits as 0, using at most `k` operations. This is done by iterating through the array and greedily merging adjacent elements whenever the current running AND result contains bits we want to eliminate.

### Complexity Analysis
- **Time Complexity**: `O(n * log(max(nums)))`, where `n` is the length of the array. We iterate through 30 bits, and for each bit, we perform a linear scan of the array.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the state during the greedy checks.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    def can_achieve(target_or: int) -> bool:
        ops = 0
        current_and = -1  # All bits set to 1

        for x in nums:
            if current_and == -1:
                current_and = x
            else:
                current_and &= x

            # If current_and only contains bits allowed in target_or
            if (current_and | target_or) == target_or:
                current_and = -1
            else:
                ops += 1

        return ops <= k

    ans = 0
    # Iterate from most significant bit to least significant
    for i in range(30, -1, -1):
        # Try to see if we can keep the i-th bit as 0
        # We assume all bits higher than i are already fixed in 'ans'
        target = ans | ((1 << i) - 1)

        # If we cannot force the i-th bit to be 0, we must accept it as 1
        if not can_achieve(target):
            ans |= (1 << i)

    return ans
```
</details>
