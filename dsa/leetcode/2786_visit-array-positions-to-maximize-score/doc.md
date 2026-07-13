# Visit Array Positions to Maximize Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2786 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [visit-array-positions-to-maximize-score](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/visit-array-positions-to-maximize-score/).

### Goal
Given an array of integers and a penalty value, you start at the first element of the array. You must traverse the array from left to right, choosing a subsequence of indices starting at index 0. If you move from an element with a different parity (even vs. odd) to another, you incur a penalty. The objective is to maximize the total sum of the values of the chosen indices.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the values at each position.
- `x`: An integer representing the penalty incurred when switching between odd and even numbers.

**Return value**

- An integer representing the maximum possible score achievable by selecting a valid subsequence of indices.

### Examples
**Example 1**

- Input: `nums = [2, 3, 6, 1, 9, 2], x = 5`
- Output: `13`
- Explanation: We choose indices 0, 2, 4. Values: 2 + 6 + 9 = 17. Parity changes: 2(even) to 6(even) [no penalty], 6(even) to 9(odd) [penalty 5]. Total: 17 - 5 = 12. Alternatively, choosing 0, 1, 4 gives 2+3+9 - 5 - 5 = 4. The optimal path is 13.

**Example 2**

- Input: `nums = [2, 4, 6], x = 3`
- Output: `12`
- Explanation: All numbers are even, so no penalty is incurred. Sum = 2 + 4 + 6 = 12.

**Example 3**

- Input: `nums = [1], x = 2`
- Output: `1`

---

## Solution
### Approach
Dynamic Programming. We maintain two states: the maximum score ending with an even number and the maximum score ending with an odd number. For each new number, we update these states based on whether the current number is even or odd, considering the penalty `x` if the parity differs from the previous state.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store two variables to track the maximum scores for even and odd parities.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], x: int) -> int:
    # Initialize DP states with a very small number to represent unreachable states.
    # even_max: max score ending in an even number
    # odd_max: max score ending in an odd number
    even_max = float('-inf')
    odd_max = float('-inf')

    # Base case: the first element
    if nums[0] % 2 == 0:
        even_max = nums[0]
    else:
        odd_max = nums[0]

    for i in range(1, len(nums)):
        val = nums[i]
        if val % 2 == 0:
            # Current is even:
            # 1. Stay even: even_max + val
            # 2. Switch from odd: odd_max + val - x
            even_max = max(even_max + val, odd_max + val - x)
        else:
            # Current is odd:
            # 1. Stay odd: odd_max + val
            # 2. Switch from even: even_max + val - x
            odd_max = max(odd_max + val, even_max + val - x)

    return max(even_max, odd_max)
```
</details>
