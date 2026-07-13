# Collecting Chocolates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2735 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [collecting-chocolates](https://leetcode.com/problems/collecting-chocolates/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/collecting-chocolates/).

### Goal
Given a 0-indexed integer array `nums` of size `n` representing the initial cost of collecting different types of chocolates, and an integer `x` representing the cost of performing a cyclic shift operation, find the minimum total cost to collect all `n` types of chocolates.

In one operation, you can rotate the chocolates such that the chocolate at index `i` becomes the chocolate at index `(i + 1) % n`. You can perform this operation any number of times. If you perform `k` operations, the cost to collect chocolate of type `i` is the minimum cost of that chocolate type across all the shifted configurations it has been in (i.e., the minimum of `nums[(i - j) % n]` for all `0 <= j <= k`). The total cost is the sum of the collection costs for all types plus the operation cost `k * x`.

### Function Contract
**Inputs**
- `nums`: `List[int]` - A list of integers representing the initial costs of the chocolates.
- `x`: `int` - The cost to perform a single cyclic shift operation.

**Return value**
- `int` - The minimum total cost to collect all types of chocolates.

### Examples
**Example 1**
- Input: `nums = [20, 1, 15]`, `x = 5`
- Output: `13`
- Explanation:
  - With 0 operations, the cost is `20 + 1 + 15 = 36`.
  - With 1 operation, the cost is `5 + min(20, 15) + min(1, 20) + min(15, 1) = 5 + 15 + 1 + 1 = 22`.
  - With 2 operations, the cost is `10 + min(20, 15, 1) + min(1, 20, 15) + min(15, 1, 20) = 10 + 1 + 1 + 1 = 13`.
  - The minimum total cost is 13.

**Example 2**
- Input: `nums = [1, 2, 3]`, `x = 4`
- Output: `6`
- Explanation:
  - With 0 operations, the cost is `1 + 2 + 3 = 6`.
  - With 1 operation, the cost is `4 + min(1, 3) + min(2, 1) + min(3, 2) = 4 + 1 + 1 + 2 = 8`.
  - With 2 operations, the cost is `8 + min(1, 3, 2) + min(2, 1, 3) + min(3, 2, 1) = 8 + 1 + 1 + 1 = 11`.
  - The minimum total cost is 6.

---

## Solution
### Approach
The problem can be solved using **Enumeration** and **Dynamic Programming / Array Manipulation**.

Since the array size `n` is at most `2000`, rotating the array more than `n - 1` times is redundant because the chocolates will return to their original positions, and any further operations will only increase the total cost by `x` without offering any new minimum costs. Thus, we can enumerate the number of operations `k` from `0` to `n - 1`.

We maintain an array `min_costs` of size `n`, where `min_costs[i]` stores the minimum cost to collect chocolate `i` using at most `k` operations.
- Initially, for `k = 0`, `min_costs[i] = nums[i]`.
- For each step `k` from `1` to `n - 1`, we update `min_costs[i] = min(min_costs[i], nums[(i - k) % n])`.
- The total cost for a given `k` is `k * x + sum(min_costs)`.
- We return the minimum total cost found across all possible values of `k`.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` where `n` is the number of elements in `nums`. We run an outer loop `n` times (for `k` from `0` to `n - 1`) and an inner loop of size `n` to update the minimum costs.
- **Space Complexity**: `O(n)` to store the `min_costs` array of size `n`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], x: int) -> int:
    n = len(nums)
    # min_costs[i] will store the minimum cost to collect chocolate i so far
    min_costs = list(nums)
    ans = sum(min_costs)

    # Enumerate the number of operations k from 1 to n - 1
    for k in range(1, n):
        for i in range(n):
            # Python's negative indexing automatically handles (i - k) % n
            if nums[i - k] < min_costs[i]:
                min_costs[i] = nums[i - k]

        # Calculate the total cost with k operations
        ans = min(ans, k * x + sum(min_costs))

    return ans
```
</details>
