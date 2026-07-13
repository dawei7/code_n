# Find if Digit Game Can Be Won

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-if-digit-game-can-be-won](https://leetcode.com/problems/find-if-digit-game-can-be-won/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-if-digit-game-can-be-won/).

### Goal
Determine if Alice can win a game where she can remove either all single-digit numbers (1-9) or all double-digit numbers (10-99) from a list, provided the sum of the removed numbers is strictly greater than the sum of the remaining numbers.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element is between 1 and 99 inclusive.

**Return value**

- `bool`: Returns `True` if Alice can win by choosing either the single-digit set or the double-digit set, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 10]`
- Output: `False`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 14]`
- Output: `True`

**Example 3**

- Input: `nums = [5, 5, 5, 25]`
- Output: `True`

---

## Solution
### Approach
The problem is a simple partitioning and summation task. By categorizing numbers into two groups (single-digit and double-digit), we can calculate the total sum of each group. Alice wins if the sum of the single-digit numbers is greater than the sum of the double-digit numbers, or vice versa.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list once to calculate the sums.
- **Space Complexity**: `O(1)`, as we only store two integer variables for the sums regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if Alice can win by removing either all single-digit numbers
    or all double-digit numbers.
    """
    single_digit_sum = 0
    double_digit_sum = 0

    for num in nums:
        if num < 10:
            single_digit_sum += num
        else:
            double_digit_sum += num

    # Alice wins if she can remove a set such that the sum of the removed
    # numbers is strictly greater than the sum of the remaining numbers.
    # This is equivalent to saying the sum of the removed set is greater
    # than the sum of the other set.
    return single_digit_sum != double_digit_sum
```
</details>
