# Minimum Swaps to Sort by Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3551 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-swaps-to-sort-by-digit-sum](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/).

### Goal
Given an array of integers, determine the minimum number of swaps required to sort the array such that elements are ordered primarily by the sum of their digits (in non-decreasing order). If two numbers have the same digit sum, their relative order should be preserved based on their original indices (stable sort behavior).

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the minimum number of swaps required to reach the target sorted state.

### Examples
**Example 1**

- Input: `nums = [13, 22, 31]`
- Output: `0`
- Explanation: Digit sums are 4, 4, 4. They are already in stable order.

**Example 2**

- Input: `nums = [15, 8, 2]`
- Output: `1`
- Explanation: Digit sums are 6, 8, 2. Sorted order of sums: 2, 6, 8. Target array: [2, 15, 8]. One swap (15 and 2) achieves this.

**Example 3**

- Input: `nums = [10, 20, 30]`
- Output: `0`
- Explanation: Digit sums are 1, 2, 3. Already sorted.

---

## Solution
### Approach
The problem is solved by first determining the target permutation of the array indices based on the custom sorting criteria (digit sum, then original index). Once the target positions are known, the problem reduces to finding the minimum number of swaps to transform the current permutation into the target permutation. This is equivalent to counting the number of cycles in the permutation graph: `swaps = N - number_of_cycles`.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where `N` is the length of the array. The cycle decomposition takes `O(N)`.
- **Space Complexity**: `O(N)` to store the target indices and the visited array for cycle detection.

### Reference Implementations
<details>
<summary>python</summary>

```python
def get_digit_sum(n: int) -> int:
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve(nums: list[int]) -> int:
    n = len(nums)
    # Create pairs of (digit_sum, original_index, value)
    # We use original_index to ensure stability
    indexed_nums = []
    for i, val in enumerate(nums):
        indexed_nums.append((get_digit_sum(val), i, val))

    # Sort based on digit sum, then original index
    indexed_nums.sort(key=lambda x: (x[0], x[1]))

    # target_pos[i] is the index where the element currently at i should go
    target_pos = [0] * n
    for new_idx, (d_sum, old_idx, val) in enumerate(indexed_nums):
        target_pos[old_idx] = new_idx

    # Count cycles in the permutation
    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or target_pos[i] == i:
            continue

        cycle_size = 0
        curr = i
        while not visited[curr]:
            visited[curr] = True
            curr = target_pos[curr]
            cycle_size += 1

        if cycle_size > 1:
            swaps += (cycle_size - 1)

    return swaps
```
</details>
