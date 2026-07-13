# Subsequences with a Unique Middle Mode I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3395 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [subsequences-with-a-unique-middle-mode-i](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/).

### Goal
Given an array of integers, identify the number of subsequences of length 5 such that the middle element (the third element) is the unique mode of the subsequence. A unique mode is defined as the element that appears more frequently than any other element in the subsequence.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is at least 5.

**Return value**

- An integer representing the total count of subsequences of length 5 that satisfy the unique middle mode condition, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1, 1]`
- Output: `6`

**Example 2**

- Input: `nums = [1, 2, 2, 3, 3, 4]`
- Output: `4`

**Example 3**

- Input: `nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using combinatorics and prefix/suffix frequency tracking. For each element `nums[i]` acting as the potential middle element, we calculate the number of ways to choose two elements from the left (indices `0` to `i-1`) and two elements from the right (indices `i+1` to `n-1`) such that `nums[i]` appears more times than any other value in the 5-element subsequence. We use inclusion-exclusion to subtract cases where other elements appear with equal or greater frequency than the middle element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array a constant number of times using precomputed frequency maps.
- **Space Complexity**: `O(n)` to store frequency counts and prefix/suffix arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums: list[int]) -> int:
    mod = 10**9 + 7

    def choose2(count: int) -> int:
        return count * (count - 1) // 2 if count >= 2 else 0

    left = Counter()
    right = Counter(nums)
    left_pair_total = 0
    right_pair_total = sum(choose2(count) for count in right.values())
    answer = 0

    for index, middle in enumerate(nums):
        old_right = right[middle]
        right_pair_total -= old_right - 1
        right[middle] -= 1
        if right[middle] == 0:
            del right[middle]

        left_size = index
        right_size = len(nums) - index - 1
        left_middle = left[middle]
        right_middle = right.get(middle, 0)
        left_other = left_size - left_middle
        right_other = right_size - right_middle

        left_distinct_other_pairs = choose2(left_other) - (
            left_pair_total - choose2(left_middle)
        )
        right_distinct_other_pairs = choose2(right_other) - (
            right_pair_total - choose2(right_middle)
        )

        current = 0

        current += choose2(left_middle) * choose2(right_middle)
        current += choose2(left_middle) * right_middle * right_other
        current += left_middle * choose2(right_middle) * left_other
        current += choose2(left_middle) * choose2(right_other)
        current += choose2(right_middle) * choose2(left_other)
        current += left_middle * left_other * right_middle * right_other

        if left_middle:
            ways = 0
            for value, left_count in left.items():
                if value == middle:
                    continue
                right_count = right.get(value, 0)
                ways += left_count * (
                    right_distinct_other_pairs
                    - right_count * (right_other - right_count)
                )
            current += left_middle * ways

        if right_middle:
            ways = 0
            for value, right_count in right.items():
                if value == middle:
                    continue
                left_count = left.get(value, 0)
                ways += right_count * (
                    left_distinct_other_pairs
                    - left_count * (left_other - left_count)
                )
            current += right_middle * ways

        answer = (answer + current) % mod

        old_left = left[middle]
        left_pair_total += old_left
        left[middle] += 1

    return answer
```
</details>
