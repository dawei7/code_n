# Transform Array by Parity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3467 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [transform-array-by-parity](https://leetcode.com/problems/transform-array-by-parity/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/transform-array-by-parity/).

### Goal
Given an array of integers, transform the array such that all even numbers appear before all odd numbers. The relative order of the even numbers and the relative order of the odd numbers do not need to be preserved; the primary requirement is to categorize elements based on their parity (even vs. odd) and arrange them accordingly.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) where all even integers from the input are placed at the beginning, followed by all odd integers.

### Examples
**Example 1**

- Input: `nums = [4, 2, 5, 7]`
- Output: `[4, 2, 6, 8]` (Note: Parity transformation results in `[4, 2, 5, 7]` or similar depending on parity count)

**Example 2**

- Input: `nums = [3, 1, 2, 4]`
- Output: `[2, 4, 3, 1]`

**Example 3**

- Input: `nums = [0]`
- Output: `[0]`

---

## Solution
### Approach
The problem can be solved using a **Counting** approach or a **Two-Pointer** approach. By counting the number of even integers, we can determine the exact number of zeros (representing even parity) and ones (representing odd parity) to construct the result, or simply sort the array using a custom key based on the modulo 2 operation.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` if using sorting, or `O(n)` if using a single pass to count or partition.
- **Space Complexity**: `O(n)` to store the resulting array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List


def solve(nums: List[int]) -> List[int]:
    even_count = sum(1 for value in nums if value % 2 == 0)
    return [0] * even_count + [1] * (len(nums) - even_count)
```
</details>
