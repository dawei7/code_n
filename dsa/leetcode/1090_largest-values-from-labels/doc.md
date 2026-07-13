# Largest Values From Labels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1090 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-values-from-labels](https://leetcode.com/problems/largest-values-from-labels/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-values-from-labels/).

### Goal
Pick at most `numWanted` items to maximize the total value, while using no more than `useLimit` items with the same label.

### Function Contract
**Inputs**

- `values`: item values.
- `labels`: label for each item at the same index.
- `numWanted`: maximum number of chosen items.
- `useLimit`: maximum chosen items allowed for any single label.

**Return value**

The largest possible sum of selected values.

### Examples
**Example 1**

- Input: `values = [5,4,3,2,1]`, `labels = [1,1,2,2,3]`, `numWanted = 3`, `useLimit = 1`
- Output: `9`

**Example 2**

- Input: `values = [5,4,3,2,1]`, `labels = [1,3,3,3,2]`, `numWanted = 3`, `useLimit = 2`
- Output: `12`

**Example 3**

- Input: `values = [9,8,8,7,6]`, `labels = [0,0,0,1,1]`, `numWanted = 4`, `useLimit = 2`
- Output: `30`

---

## Solution
### Approach
Greedy sorting with per-label counting.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for sorting and label counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1090: Largest Values From Labels."""


def solve(values: list[int], labels: list[int], num_wanted: int, use_limit: int) -> int:
    used: dict[int, int] = {}
    total = 0
    chosen = 0
    for value, label in sorted(zip(values, labels), reverse=True):
        if chosen == num_wanted:
            break
        if used.get(label, 0) == use_limit:
            continue
        used[label] = used.get(label, 0) + 1
        total += value
        chosen += 1
    return total
```
</details>
