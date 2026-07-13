# Find the XOR of Numbers Which Appear Twice

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3158 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-xor-of-numbers-which-appear-twice](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/).

### Goal
Given an array of integers where each number appears either once or twice, identify all numbers that occur exactly twice and compute their bitwise XOR sum. If no numbers appear twice, the result should be zero.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where each element is between 1 and 50.

**Return value**

- An integer representing the XOR sum of all elements that appear exactly twice in the input array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 3]`
- Output: `1`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 2, 1]`
- Output: `3`

---

## Solution
### Approach
The problem utilizes a frequency tracking mechanism, typically implemented via a Hash Set or a frequency array. By iterating through the input, we track seen elements; when an element is encountered for the second time, it is identified as a duplicate and included in the running XOR calculation.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass over the data.
- **Space Complexity**: `O(n)` in the worst case to store the set of seen numbers, or `O(1)` if considering the fixed constraint (numbers are between 1 and 50).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    seen = set()
    xor_sum = 0

    for num in nums:
        if num in seen:
            xor_sum ^= num
        else:
            seen.add(num)

    return xor_sum
```
</details>
