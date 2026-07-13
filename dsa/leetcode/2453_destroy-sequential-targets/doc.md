# Destroy Sequential Targets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2453 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [destroy-sequential-targets](https://leetcode.com/problems/destroy-sequential-targets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/destroy-sequential-targets/).

### Goal
Given a list of target values and a common difference `space`, we want to identify a starting value `s` such that the sequence `s, s + space, s + 2*space, ...` hits the maximum number of targets present in the input array. If multiple starting values yield the same maximum count, return the smallest such `s`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the target values.
- `space`: An integer representing the constant difference between sequential targets.

**Return value**

- An integer representing the smallest starting value `s` that maximizes the number of destroyed targets.

### Examples
**Example 1**

- Input: `nums = [3, 7, 8, 1, 1, 5], space = 2`
- Output: `1`
- Explanation: Targets are 1, 3, 5, 7. Starting at 1 hits 1, 3, 5, 7 (4 targets). Starting at 3 hits 3, 5, 7 (3 targets). 1 is the smallest.

**Example 2**

- Input: `nums = [1, 3, 5, 2, 4, 6], space = 2`
- Output: `1`
- Explanation: Starting at 1 hits 1, 3, 5. Starting at 2 hits 2, 4, 6. Both hit 3 targets, 1 is smaller.

**Example 3**

- Input: `nums = [1, 5, 1, 4], space = 4`
- Output: `1`
- Explanation: Starting at 1 hits 1, 5. Starting at 4 hits 4. 1 is the smallest.

---

## Solution
### Approach
The problem relies on the property of modular arithmetic: two numbers `a` and `b` belong to the same sequence with common difference `space` if and only if `a % space == b % space`. By grouping all numbers by their remainder modulo `space`, we can count how many numbers fall into each sequence. The optimal starting value for a remainder `r` is the minimum value in the input array that satisfies `val % space == r`.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of elements in `nums`. We iterate through the array once to count remainders and once to find the minimum value for each remainder.
- **Space Complexity**: `O(K)`, where `K` is the number of unique remainders (at most `space`), used to store the counts and the minimum values for each remainder group.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], space: int) -> int:
    # Map remainder -> count of numbers with that remainder
    remainder_counts = defaultdict(int)
    # Map remainder -> smallest number found with that remainder
    min_val_for_remainder = {}

    for num in nums:
        rem = num % space
        remainder_counts[rem] += 1

        if rem not in min_val_for_remainder or num < min_val_for_remainder[rem]:
            min_val_for_remainder[rem] = num

    max_targets = -1
    best_start = float('inf')

    for rem in remainder_counts:
        count = remainder_counts[rem]
        start_val = min_val_for_remainder[rem]

        if count > max_targets:
            max_targets = count
            best_start = start_val
        elif count == max_targets:
            if start_val < best_start:
                best_start = start_val

    return best_start
```
</details>
