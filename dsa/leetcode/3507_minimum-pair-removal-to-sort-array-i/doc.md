# Minimum Pair Removal to Sort Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3507 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-pair-removal-to-sort-array-i](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/).

### Goal
Given an array of integers, determine the minimum number of adjacent pairs that must be removed such that the remaining elements form a non-decreasing sequence. A removal operation consists of deleting two adjacent elements simultaneously.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to be processed.

**Return value**

- An integer representing the minimum number of pair removals required to make the array sorted.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [5, 1, 2, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `1`

---

## Solution
### Approach
The problem can be solved using a Greedy approach. By iterating through the array and identifying the first instance where the non-decreasing property is violated (i.e., `nums[i] > nums[i+1]`), we can simulate the removal of that pair. Since we want to minimize removals, we prioritize removing pairs that resolve the immediate inversion.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform a single pass to identify and remove violating pairs.
- **Space Complexity**: `O(n)` in the worst case to store the modified array or a stack-based representation of the remaining elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    values = list(nums)
    operations = 0

    def is_sorted() -> bool:
        return all(values[i] <= values[i + 1] for i in range(len(values) - 1))

    while not is_sorted():
        best_index = 0
        best_sum = values[0] + values[1]
        for index in range(1, len(values) - 1):
            pair_sum = values[index] + values[index + 1]
            if pair_sum < best_sum:
                best_sum = pair_sum
                best_index = index
        values[best_index : best_index + 2] = [best_sum]
        operations += 1

    return operations
```
</details>
