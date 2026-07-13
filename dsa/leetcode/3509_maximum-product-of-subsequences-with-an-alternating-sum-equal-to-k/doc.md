# Maximum Product of Subsequences With an Alternating Sum Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3509 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k](https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/).

### Goal
Given an array of integers `nums` and an integer `k`, find the maximum product of a subsequence of `nums` such that the alternating sum of the subsequence equals `k`. The alternating sum is defined as the sum of elements at odd indices minus the sum of elements at even indices (0-indexed) of the subsequence. If no such subsequence exists, return -1. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available elements.
- `k`: An integer representing the target alternating sum.

**Return value**

- An integer representing the maximum product modulo 10^9 + 7, or -1 if no valid subsequence exists.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1, 2, 3, 4], k = 1`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, 3, 4], k = 5`
- Output: `-1`

---

## Solution
### Approach
Dynamic Programming with state compression. The state is defined by `(index, current_sum, length_parity)`, where we track the maximum product for a given alternating sum. Because the product can be large, we use logarithms or careful tracking of signs and magnitudes to handle the "maximum" requirement before applying the modulo.

### Complexity Analysis
- **Time Complexity**: `O(n * k * L)`, where `n` is the length of `nums`, `k` is the target sum, and `L` is the maximum possible length of the subsequence.
- **Space Complexity**: `O(k * L)` using space optimization on the DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(nums: list[int], k: int, limit: int) -> int:
    if abs(k) > sum(nums):
        return -1

    over_limit = limit + 1
    states: list[dict[int, set[int]]] = [defaultdict(set), defaultdict(set)]

    for value in nums:
        updated: list[dict[int, set[int]]] = [
            defaultdict(set, {total: set(products) for total, products in states[0].items()}),
            defaultdict(set, {total: set(products) for total, products in states[1].items()}),
        ]

        if value <= limit:
            updated[1][value].add(value)

        for parity in (0, 1):
            sign = 1 if parity == 0 else -1
            next_parity = 1 - parity
            for total, products in states[parity].items():
                next_total = total + sign * value
                target = updated[next_parity][next_total]
                for product in products:
                    next_product = product * value
                    target.add(next_product if next_product <= limit else over_limit)
        states = updated

    candidates = states[0].get(k, set()) | states[1].get(k, set())
    valid = [product for product in candidates if product <= limit]
    return max(valid) if valid else -1
```
</details>
