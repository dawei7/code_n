# The Two Sneaky Numbers of Digitville

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3289 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-two-sneaky-numbers-of-digitville](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/).

### Goal
Given an array containing $n+2$ elements where each element is an integer between $0$ and $n-1$ inclusive, identify the two numbers that appear exactly twice in the array. Every other number in the range $[0, n-1]$ appears exactly once.

### Function Contract
**Inputs**

- `nums`: A list of integers of length $n+2$, where each integer is in the range $[0, n-1]$.

**Return value**

- A list containing the two integers that appear twice in the input array.

### Examples
**Example 1**

- Input: `nums = [0, 1, 1, 0]`
- Output: `[0, 1]`

**Example 2**

- Input: `nums = [0, 3, 2, 1, 3, 2]`
- Output: `[2, 3]`

**Example 3**

- Input: `nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]`
- Output: `[4, 5]`

---

## Solution
### Approach
The problem can be solved efficiently using a frequency counting approach. Since the range of numbers is constrained, a hash set or a frequency array (or a boolean array) can track occurrences. As we iterate through the input, we check if the current number has been seen before; if so, it is one of the "sneaky" numbers.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the number of elements in the array, as we perform a single pass through the input.
- **Space Complexity**: $O(n)$ to store the set of seen numbers. (Note: This can be optimized to $O(1)$ if the input array is mutable and we use index-based marking, but $O(n)$ is standard for clarity).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for num in nums:
        if num in seen:
            result.append(num)
        else:
            seen.add(num)
    return result
```
</details>
