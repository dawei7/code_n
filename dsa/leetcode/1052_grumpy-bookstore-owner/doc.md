# Grumpy Bookstore Owner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1052 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [grumpy-bookstore-owner](https://leetcode.com/problems/grumpy-bookstore-owner/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/grumpy-bookstore-owner/).

### Goal
For each minute, customers enter a bookstore and the owner is either grumpy or not. Non-grumpy minutes always satisfy customers. Choose one contiguous window of length `minutes` during which grumpiness is suppressed to maximize satisfied customers.

### Function Contract
**Inputs**

- `customers`: List[int]
- `grumpy`: List[int] where `1` means grumpy
- `minutes`: int length of the suppression window

**Return value**

int - maximum satisfied customers

### Examples
**Example 1**

- Input: `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`
- Output: `16`

**Example 2**

- Input: `customers = [1], grumpy = [0], minutes = 1`
- Output: `1`

**Example 3**

- Input: `customers = [4, 10, 10], grumpy = [1, 1, 0], minutes = 2`
- Output: `24`

---

## Solution
### Approach
Sliding window over extra recoverable customers.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1052: Grumpy Bookstore Owner."""


def solve(customers: list[int], grumpy: list[int], minutes: int) -> int:
    base = sum(c for c, g in zip(customers, grumpy) if g == 0)
    extra = 0
    best_extra = 0
    for i, (customer, is_grumpy) in enumerate(zip(customers, grumpy)):
        if is_grumpy:
            extra += customer
        if i >= minutes and grumpy[i - minutes]:
            extra -= customers[i - minutes]
        best_extra = max(best_extra, extra)
    return base + best_extra
```
</details>
