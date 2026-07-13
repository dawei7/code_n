# Make Array Elements Equal to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3354 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [make-array-elements-equal-to-zero](https://leetcode.com/problems/make-array-elements-equal-to-zero/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/make-array-elements-equal-to-zero/).

### Goal
Given an array of integers, determine how many valid selections can reduce every element to zero. A selection chooses an index whose value is already `0` and an initial direction, either left or right. During the process, zeros are passed through in the current direction; positive values are decremented, the direction is reversed, and the pointer moves one step in the new direction. The process ends when the pointer leaves the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array state.

**Return value**

- An integer representing the number of valid `(zero index, initial direction)` selections.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2, 0, 3]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 3, 4, 0, 4, 1, 0]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 0, 2]`
- Output: `2`

---

## Solution
### Approach
The problem can be solved by observing that the simulation only succeeds if the sum of elements to the left of the starting index equals the sum of elements to the right (or differs by exactly 1 if the starting element is non-zero). By pre-calculating the total sum and using a prefix sum approach, we can evaluate each potential starting index in constant time.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array to calculate sums and then once more to check each index.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    valid = 0

    for value in nums:
        right = total - left - value
        if value == 0:
            if left == right:
                valid += 2
            elif abs(left - right) == 1:
                valid += 1
        left += value

    return valid
```
</details>
